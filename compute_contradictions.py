import os
import json
import csv
import re
from model_taxonomy import parse_model

CACHE_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_rsc_json(html):
    chunks = re.findall(r'self\.__next_f\.push\(\[1,\"(.*?)\"\]\)', html)
    full_rsc = ''
    for c in chunks:
        try:
            full_rsc += json.loads('"' + c + '"')
        except Exception:
            pass
    return full_rsc

def parse_simple_yml_list(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        txt = f.read()
    entries = []
    curr = {}
    for line in txt.splitlines():
        if line.startswith('- '):
            if curr: entries.append(curr)
            curr = {}
            line = line[2:]
        if ':' in line and not line.startswith('  -'):
            k, v = line.split(':', 1)
            k = k.strip()
            v = v.strip()
            if '#' in v:
                v = v.split('#')[0].strip()
            try:
                if '.' in v: v = float(v)
                else: v = int(v)
            except Exception:
                pass
            curr[k] = v
    if curr: entries.append(curr)
    return entries

def _run_pairwise(enriched, metric_type, higher_is_better, canonical_mode, include_version_axis=True):
    comparable_pairs = []
    contradictions = []
    n = len(enriched)
    for i in range(n):
        for j in range(i + 1, n):
            m1 = enriched[i]
            m2 = enriched[j]
            p1 = m1['parsed']
            p2 = m2['parsed']
            if not p1 or not p2:
                continue
            if p1['family'] != p2['family']:
                continue

            same_v = (p1['version'] == p2['version'])
            same_s = (p1['tier_rank'] == p2['tier_rank'] and p1['tier'] == p2['tier'])
            same_r = (p1['effort_rank'] == p2['effort_rank'])

            axis = None
            larger_or_newer = None
            smaller_or_older = None

            if canonical_mode:
                # Rule 1: Same-generation tier comparison (same version, different size tier)
                if same_v and not same_s and p1['tier_rank'] != p2['tier_rank']:
                    if metric_type in ('latency', 'cost'):
                        if (p1['effort_rank'] == 1.0 and p2['effort_rank'] >= 3.5) or (p2['effort_rank'] == 1.0 and p1['effort_rank'] >= 3.5):
                            continue
                    if p1['tier_rank'] > p2['tier_rank']:
                        larger_or_newer, smaller_or_older = m1, m2
                    else:
                        larger_or_newer, smaller_or_older = m2, m1
                    pa, pb = larger_or_newer['parsed'], smaller_or_older['parsed']
                    if pa['effort_rank'] > 1.0 and pb['effort_rank'] > 1.0 and pa['effort_rank'] < pb['effort_rank']:
                        continue
                    axis = 'tier'
                # Rule 2: Cross-generation same-tier comparison (same size tier, different version)
                elif include_version_axis and same_s and not same_v:
                    if metric_type == 'quality':
                        if (p1['effort_rank'] == 1.0 and p2['effort_rank'] >= 3.5) or (p2['effort_rank'] == 1.0 and p1['effort_rank'] >= 3.5):
                            continue
                        if p1['version'] > p2['version']:
                            larger_or_newer, smaller_or_older = m1, m2
                        else:
                            larger_or_newer, smaller_or_older = m2, m1
                        pa, pb = larger_or_newer['parsed'], smaller_or_older['parsed']
                        if pa['effort_rank'] > 1.0 and pb['effort_rank'] > 1.0 and pa['effort_rank'] < pb['effort_rank']:
                            continue
                        axis = 'version'
            else:
                # Same-effort Top-K leaderboard comparison on Rule 1 (tier) and Rule 2 (version)
                if same_v and same_r and not same_s and p1['tier_rank'] != p2['tier_rank']:
                    axis = 'tier'
                    if p1['tier_rank'] > p2['tier_rank']:
                        larger_or_newer, smaller_or_older = m1, m2
                    else:
                        larger_or_newer, smaller_or_older = m2, m1
                elif include_version_axis and same_s and same_r and not same_v:
                    if metric_type == 'quality':
                        axis = 'version'
                        if p1['version'] > p2['version']:
                            larger_or_newer, smaller_or_older = m1, m2
                        else:
                            larger_or_newer, smaller_or_older = m2, m1

            if not axis:
                continue

            if metric_type == 'quality':
                exp_high = larger_or_newer
                exp_low = smaller_or_older
                is_contradicted = (exp_low['score'] > exp_high['score'] + 1e-9)
                expected_str = f"{exp_high['name']} >= {exp_low['name']}"
            elif metric_type == 'latency':
                exp_fast = smaller_or_older
                exp_slow = larger_or_newer
                if higher_is_better:
                    is_contradicted = (exp_slow['score'] > exp_fast['score'] + 1e-9)
                    expected_str = f"{exp_fast['name']} >= {exp_slow['name']} (Speed)"
                else:
                    is_contradicted = (exp_slow['score'] < exp_fast['score'] - 1e-9)
                    expected_str = f"{exp_fast['name']} <= {exp_slow['name']} (Latency)"
            elif metric_type == 'cost':
                exp_more_expensive = larger_or_newer
                exp_cheaper = smaller_or_older
                is_contradicted = (exp_cheaper['score'] > exp_more_expensive['score'] + 1e-9)
                expected_str = f"Cost({exp_more_expensive['name']}) >= Cost({exp_cheaper['name']})"

            rank_diff = abs(larger_or_newer['rank'] - smaller_or_older['rank'])
            pair_record = {
                'axis': axis,
                'family': p1['family'],
                'model_a': larger_or_newer['name'],
                'rank_a': larger_or_newer['rank'],
                'score_a': round(larger_or_newer['score'], 4),
                'class_a': f"{larger_or_newer['parsed']['version_str']} {larger_or_newer['parsed']['tier']} ({larger_or_newer['parsed']['effort']})",
                'model_b': smaller_or_older['name'],
                'rank_b': smaller_or_older['rank'],
                'score_b': round(smaller_or_older['score'], 4),
                'class_b': f"{smaller_or_older['parsed']['version_str']} {smaller_or_older['parsed']['tier']} ({smaller_or_older['parsed']['effort']})",
                'rank_displacement': rank_diff,
                'contradicted': is_contradicted,
                'expected': expected_str
            }
            comparable_pairs.append(pair_record)
            if is_contradicted:
                contradictions.append(pair_record)

    return comparable_pairs, contradictions

def evaluate_ranking(items, metric_type='quality', higher_is_better=True, top_k=100, deduplicate_canonical=True, include_version_axis=True, include_effort_axis=False):
    """
    Evaluates the Top-K (default Top 100) ranked models on a benchmark using the two strict intra-family rules:
      1. Same-generation tier rule (e.g. GPT 6.1 Sol > GPT 6.1 Terra > GPT 6.1 Luna)
      2. Cross-generation same-tier rule (e.g. GPT 6.1 Sol > GPT 6.0 Sol)
    """
    valid_items = []
    for x in items:
        sc = x.get('score')
        if sc is None or isinstance(sc, str):
            continue
        try:
            sc_f = float(sc)
        except Exception:
            continue
        p = parse_model(x['name'], x.get('is_reasoning'))
        if p and p.get('variant_tag') in ('Fast', 'Ultrafast', 'Flex'):
            continue
        valid_items.append({
            'name': x['name'],
            'score': sc_f,
            'parsed': p,
            'is_first_party': bool(x.get('is_first_party', True))
        })

    # 1. Build deduplicated exact-name list for raw Top-K
    by_name = {}
    for x in valid_items:
        by_name.setdefault(x['name'], []).append(x)
    raw_items = []
    for nm, grp in by_name.items():
        grp.sort(key=lambda item: (1 if item['is_first_party'] else 0, item['score'] if higher_is_better else -item['score']), reverse=True)
        raw_items.append(dict(grp[0]))
    raw_items.sort(key=lambda x: x['score'], reverse=higher_is_better)
    raw_enriched = raw_items[:top_k]
    for idx, item in enumerate(raw_enriched):
        item['rank'] = idx + 1

    # 2. Build canonical (family, version, tier) flagship list for canonical Top-K
    groups = {}
    for x in valid_items:
        p = x['parsed']
        key = (p['family'], p['version'], p['tier']) if p else ('__unparsed__', x['name'])
        groups.setdefault(key, []).append(x)

    deduped = []
    for key, grp in groups.items():
        if key[0] == '__unparsed__':
            grp.sort(key=lambda item: item['score'], reverse=higher_is_better)
            deduped.append(dict(grp[0]))
        else:
            grp.sort(key=lambda item: (
                1 if item['is_first_party'] else 0,
                item['parsed']['effort_rank'],
                item['score'] if higher_is_better else -item['score']
            ), reverse=True)
            deduped.append(dict(grp[0]))
    deduped.sort(key=lambda x: x['score'], reverse=higher_is_better)
    can_enriched = deduped[:top_k]
    # If deduplication yielded fewer than top_k unique tuples, top off with remaining highest-scoring raw models
    target_count = min(top_k, len(raw_items))
    if len(can_enriched) < target_count:
        seen_names = {x['name'] for x in can_enriched}
        for item in raw_items:
            if item['name'] not in seen_names:
                can_enriched.append(dict(item))
                seen_names.add(item['name'])
                if len(can_enriched) == target_count:
                    break
        can_enriched.sort(key=lambda x: x['score'], reverse=higher_is_better)
    for idx, item in enumerate(can_enriched):
        item['rank'] = idx + 1

    if deduplicate_canonical:
        can_comp, _ = _run_pairwise(can_enriched, metric_type, higher_is_better, canonical_mode=True, include_version_axis=include_version_axis)
        raw_comp, _ = _run_pairwise(raw_enriched, metric_type, higher_is_better, canonical_mode=False, include_version_axis=include_version_axis)

        # Merge canonical Top-50 pairs with any additional same-effort Top-50 pairs (deduplicated by model names)
        seen_pair_keys = set()
        comparable_pairs = []
        for p in can_comp + raw_comp:
            pk = (p['model_a'], p['model_b'])
            if pk not in seen_pair_keys:
                seen_pair_keys.add(pk)
                comparable_pairs.append(p)
        contradictions = [p for p in comparable_pairs if p['contradicted']]
        enriched = can_enriched
    else:
        comparable_pairs, contradictions = _run_pairwise(raw_enriched, metric_type, higher_is_better, canonical_mode=False, include_version_axis=include_version_axis)
        enriched = raw_enriched

    total_comp = len(comparable_pairs)
    total_contra = len(contradictions)
    contra_score = (total_contra / total_comp * 100.0) if total_comp > 0 else 0.0

    total_disp = sum(p['rank_displacement'] for p in comparable_pairs)
    contra_disp = sum(p['rank_displacement'] for p in contradictions)
    weighted_score = (contra_disp / total_disp * 100.0) if total_disp > 0 else 0.0

    by_axis = {}
    for ax in ('tier', 'version'):
        ax_comp = [p for p in comparable_pairs if p['axis'] == ax]
        ax_con = [p for p in contradictions if p['axis'] == ax]
        by_axis[ax] = {
            'comparable': len(ax_comp),
            'contradicted': len(ax_con),
            'score': round(len(ax_con) / len(ax_comp) * 100.0, 2) if ax_comp else 0.0
        }

    return {
        'top_k_count': len(enriched),
        'comparable_pairs_count': total_comp,
        'contradictions_count': total_contra,
        'contradiction_score': round(contra_score, 2),
        'weighted_contradiction_score': round(weighted_score, 2),
        'by_axis': by_axis,
        'contradictions': contradictions,
        'valid_pairs': [p for p in comparable_pairs if not p['contradicted']],
        'top25': [
            {
                'rank': x['rank'],
                'name': x['name'],
                'score': round(x['score'], 4),
                'family': x['parsed']['family'] if x['parsed'] else None,
                'version': x['parsed']['version_str'] if x['parsed'] else None,
                'tier': x['parsed']['tier'] if x['parsed'] else None,
                'effort': x['parsed']['effort'] if x['parsed'] else None,
            }
            for x in enriched
        ]
    }
