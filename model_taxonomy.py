import os
import re
import json

def parse_effort(name_lower, is_reasoning_flag=None):
    """
    Extracts reasoning effort level from model name.
    Returns (effort_name, effort_rank) where:
      Max = 6.0
      Xhigh = 5.0
      High = 4.0
      Medium = 3.0
      Low = 2.0
      Minimal = 1.5
      Reasoning (generic thinking) = 3.5
      Non-Reasoning / Standard = 1.0
    """
    s = name_lower
    if any(k in s for k in ['non-reasoning', 'no think', 'no-think', 'nothink', 'instruct']):
        if 'thinking' not in s and '(reasoning)' not in s:
            return ('Non-Reasoning', 1.0)
    if re.search(r'\b(max|max effort|max-effort)\b', s) and not re.search(r'qwen[0-9.]*[- ]max|minimax|uni-1\.1-max|flux-2-max', s):
        return ('Max', 6.0)
    if re.search(r'(\(max[,)]|-max-effort|-max$|\bmax effort\b)', s) and not any(s.endswith(x) for x in ['qwen3.8-max', 'qwen3.7-max', 'qwen2.5-max', 'uni-1.1-max', 'flux-2-max']):
        return ('Max', 6.0)
    if re.search(r'\b(xhigh|x-high)\b', s):
        return ('Xhigh', 5.0)
    if re.search(r'\b(high|high effort|high-effort|32k think|64k|thinking-32k|thinking-64k)\b', s) and 'high-fidelity' not in s:
        return ('High', 4.0)
    if re.search(r'\b(medium|medium effort|medium-effort|default think)\b', s) and not re.search(r'(mistral|magistral)[- ]medium', s):
        return ('Medium', 3.0)
    if re.search(r'\((medium|medium with fallback|medium, default fallback)\)', s):
        return ('Medium', 3.0)
    if re.search(r'\b(low|low effort|low-effort)\b', s):
        return ('Low', 2.0)
    if re.search(r'\b(minimal)\b', s):
        return ('Minimal', 1.5)
    if re.search(r'\b(thinking|reasoner|reasoning|think)\b', s):
        return ('Reasoning', 3.5)
    if is_reasoning_flag is True:
        return ('Reasoning', 3.5)
    return ('Standard', 1.0)

def parse_model(raw_name, is_reasoning_flag=None):
    if not raw_name:
        return None
    s = raw_name.strip()
    sl = s.lower()

    # Ignore multi-model ensembles unless "Agent + Single Model"
    if ' + ' in s:
        parts = [p.strip() for p in s.split('+')]
        if len(parts) == 2 and any(k in parts[1].lower() for k in ['claude', 'gemini', 'gpt', 'deepseek', 'qwen', 'grok']) and not any(k in parts[0].lower() for k in ['claude', 'gemini', 'gpt', 'deepseek', 'qwen', 'grok', 'o1', 'o3']):
            s = parts[1]
            sl = s.lower()
        else:
            return None

    variant_tag = None
    if '(fast)' in sl: variant_tag = 'Fast'
    elif '(ultrafast)' in sl: variant_tag = 'Ultrafast'
    elif '(flex)' in sl: variant_tag = 'Flex'

    effort_name, effort_rank = parse_effort(sl, is_reasoning_flag)

    # 1. ANTHROPIC CLAUDE & CLAUDE FABLE
    if 'claude' in sl:
        if 'fable' in sl:
            m = re.search(r'fable[- ]*(\d+(?:[.-]\d+)?)', sl)
            ver = float(m.group(1).replace('-', '.')) if m else 5.0
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            return {
                'raw': raw_name, 'family': 'Anthropic Claude Fable',
                'version': ver, 'version_str': v_str,
                'tier': 'Fable', 'tier_rank': 3.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        tier, tier_rank = None, None
        if 'opus' in sl: tier, tier_rank = 'Opus', 3.0
        elif 'sonnet' in sl: tier, tier_rank = 'Sonnet', 2.0
        elif 'haiku' in sl: tier, tier_rank = 'Haiku', 1.0
        elif 'instant' in sl: tier, tier_rank = 'Instant', 0.5

        if tier:
            sl_nodate = re.sub(r'202[3456]\d{4}', '', sl)
            sl_nodate = re.sub(r'\b(16k|32k|64k|100k|200k)\b', '', sl_nodate)
            m = re.search(r'(?:claude[- ]*(?:opus|sonnet|haiku)[- ]*|claude[- ]*)(\d+(?:[.-]\d+)?)(?:[- ]*(?:opus|sonnet|haiku))?', sl_nodate)
            if m:
                ver_raw = m.group(1).replace('-', '.')
                ver = float(ver_raw)
                v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
                if ('-max' in sl or '(max' in sl) and effort_rank < 6.0:
                    effort_name, effort_rank = 'Max', 6.0
                return {
                    'raw': raw_name, 'family': 'Anthropic Claude',
                    'version': ver, 'version_str': v_str,
                    'tier': tier, 'tier_rank': tier_rank,
                    'effort': effort_name, 'effort_rank': effort_rank,
                    'variant_tag': variant_tag
                }
        m2 = re.search(r'claude[- ]*([12](?:\.\d+)?)', sl)
        if m2 and not tier:
            ver = float(m2.group(1))
            return {
                'raw': raw_name, 'family': 'Anthropic Claude',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': 'Base', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 2. OPENAI GPT / O-SERIES / GPT-OSS / GPT-IMAGE / SORA
    if 'gpt-oss' in sl and 'based on gpt-oss' not in sl:
        m = re.search(r'gpt-oss-(\d+)b', sl)
        if m:
            b = float(m.group(1))
            return {
                'raw': raw_name, 'family': 'OpenAI gpt-oss',
                'version': 1.0, 'version_str': '1.0',
                'tier': f"{int(b)}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'gpt-image' in sl:
        m = re.search(r'gpt-image-(\d+(?:\.\d+)?)', sl)
        if m:
            ver = float(m.group(1))
            tier, tier_rank = 'Base', 2.0
            if 'sunburst' in sl: tier, tier_rank = 'Sunburst', 3.0
            elif 'flare' in sl: tier, tier_rank = 'Flare', 2.0
            return {
                'raw': raw_name, 'family': 'OpenAI GPT-Image',
                'version': ver, 'version_str': f"{ver:g}",
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if re.search(r'\bsora[- ]*(\d+)', sl):
        m = re.search(r'\bsora[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(m.group(1))
        tier, tier_rank = ('Pro', 3.0) if 'pro' in sl else ('Base', 2.0)
        return {
            'raw': raw_name, 'family': 'OpenAI Sora',
            'version': ver, 'version_str': f"{ver:g}",
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    mo = re.search(r'\bo([134])(?:-?(pro|preview|mini))?\b', sl)
    if mo and 'molmo' not in sl and 'olmo' not in sl and 'mimo' not in sl and 'nova' not in sl:
        ver = float(mo.group(1))
        sub = mo.group(2) or 'base'
        if sub == 'preview':
            ver = ver - 0.1
            v_str = f"o{int(mo.group(1))}-preview"
            tier, tier_rank = 'Base', 3.0
        else:
            v_str = f"o{int(ver)}"
            tier_map = {'pro': ('Pro', 4.0), 'base': ('Base', 3.0), 'mini': ('Mini', 2.0)}
            tier, tier_rank = tier_map[sub]
        return {
            'raw': raw_name, 'family': 'OpenAI o-Series',
            'version': ver, 'version_str': v_str,
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    mg = re.search(r'\bgpt[- ]*(\d+(?:\.\d+)?)(o)?\b', sl)
    if mg:
        ver = float(mg.group(1))
        is_o = bool(mg.group(2))
        if is_o and ver == 4.0:
            ver = 4.05
            v_str = '4o'
        elif ver == 4.0 and any(k in sl for k in ['turbo', '1106-preview', '0125-preview']):
            ver = 4.02
            v_str = '4-Turbo'
        else:
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"

        if 'codex' in sl and 'codex-harness' not in sl:
            return {
                'raw': raw_name, 'family': 'OpenAI GPT Codex',
                'version': ver, 'version_str': v_str,
                'tier': 'Codex', 'tier_rank': 3.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        tier, tier_rank = 'Base', 3.0
        if 'astra' in sl: tier, tier_rank = 'Astra', 4.0
        elif 'sol' in sl: tier, tier_rank = 'Sol', 3.0
        elif 'terra' in sl: tier, tier_rank = 'Terra', 2.0
        elif 'luna' in sl: tier, tier_rank = 'Luna', 1.0
        elif re.search(r'\bpro\b', sl): tier, tier_rank = 'Pro', 4.0
        elif re.search(r'\b(mini|instant)\b', sl): tier, tier_rank = 'Mini', 2.0
        elif re.search(r'\bnano\b', sl): tier, tier_rank = 'Nano', 1.0

        if ('-max' in sl or '(max' in sl) and effort_rank < 6.0:
            effort_name, effort_rank = 'Max', 6.0

        return {
            'raw': raw_name, 'family': 'OpenAI GPT',
            'version': ver, 'version_str': v_str,
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 3. GOOGLE GEMINI / GEMMA / VEO
    if 'gemma' in sl and 'diffusiongemma' not in sl:
        mgm = re.search(r'gemma[- ]*(\d+(?:\.\d+)?)', sl)
        if mgm:
            ver = float(mgm.group(1))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            is_moe = bool(re.search(r'\ba\d+b\b', sl))
            mp = re.search(r'(?:e)?(\d+(?:\.\d+)?)(b|m)\b', sl)
            if mp:
                val = float(mp.group(1))
                if mp.group(2) == 'm': val /= 1000.0
                t_label = f"{mp.group(1).upper()}{mp.group(2).upper()}"
                return {
                    'raw': raw_name, 'family': 'Google Gemma MoE' if is_moe else 'Google Gemma',
                    'version': ver, 'version_str': v_str,
                    'tier': t_label, 'tier_rank': val,
                    'effort': effort_name, 'effort_rank': effort_rank,
                    'variant_tag': variant_tag
                }

    if 'gemini' in sl:
        if 'image' in sl or 'banana' in sl:
            mgi = re.search(r'gemini[- ]*(\d+(?:\.\d+)?)', sl)
            ver = float(mgi.group(1)) if mgi else 3.0
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            tier, tier_rank = 'Pro', 3.0
            if 'flash-lite' in sl or 'lite' in sl: tier, tier_rank = 'Flash-Lite', 1.0
            elif 'flash' in sl: tier, tier_rank = 'Flash', 2.0
            return {
                'raw': raw_name, 'family': 'Google Gemini Image',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        if 'omni' in sl:
            mgo = re.search(r'omni[- ]*(\d+(?:\.\d+)?)', sl)
            ver = float(mgo.group(1)) if mgo else 1.0
            return {
                'raw': raw_name, 'family': 'Google Gemini Omni',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': 'Flash', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        mgem = re.search(r'gemini[- ]*(\d+(?:[.-]\d+)?)', sl)
        if mgem:
            ver = float(mgem.group(1).replace('-', '.'))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            tier, tier_rank = 'Pro', 3.0
            if 'carbon' in sl: tier, tier_rank = 'Carbon', 3.5
            elif 'argon' in sl: tier, tier_rank = 'Argon', 3.0
            elif 'ultra' in sl or 'deep think' in sl or 'deep-think' in sl: tier, tier_rank = 'Ultra', 4.0
            elif 'flash-lite' in sl or 'flash lite' in sl or '8b' in sl: tier, tier_rank = 'Flash-Lite', 1.0
            elif 'flash' in sl: tier, tier_rank = 'Flash', 2.0
            elif 'pro' in sl: tier, tier_rank = 'Pro', 3.0
            return {
                'raw': raw_name, 'family': 'Google Gemini',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if re.search(r'\bveo[- ]*(\d+)', sl):
        mv = re.search(r'\bveo[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(mv.group(1))
        tier, tier_rank = ('Fast', 1.0) if 'fast' in sl else ('Standard', 2.0)
        res = '1080p' if '1080p' in sl else '720p'
        return {
            'raw': raw_name, 'family': f'Google Veo ({res})',
            'version': ver, 'version_str': f"{ver:.1f}",
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 4. DEEPSEEK
    if 'deepseek' in sl and 'nemotron' not in sl:
        if 'r1' in sl:
            mp = re.search(r'(\d+(?:\.\d+)?)b', sl)
            b = float(mp.group(1)) if mp else 671.0
            return {
                'raw': raw_name, 'family': 'DeepSeek R1',
                'version': 1.0, 'version_str': '1.0',
                'tier': f"{b:g}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        mds = re.search(r'v(\d+(?:\.\d+)?)', sl)
        if mds:
            ver = float(mds.group(1))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            tier, tier_rank = 'Base', 2.5
            if 'flash' in sl: tier, tier_rank = 'Flash', 2.0
            elif 'pro' in sl: tier, tier_rank = 'Pro', 3.0
            elif 'coder' in sl and ver < 3.0: tier, tier_rank = 'Coder', 2.5
            if ('-max' in sl or '(max' in sl) and effort_rank < 6.0:
                effort_name, effort_rank = 'Max', 6.0
            return {
                'raw': raw_name, 'family': 'DeepSeek V-Series',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 5. ALIBABA QWEN
    if 'qwen' in sl and 'based on qwen' not in sl and 'distill' not in sl:
        if 'omni' in sl:
            mqo = re.search(r'qwen[- ]*(\d+(?:\.\d+)?)', sl)
            ver = float(mqo.group(1)) if mqo else 3.5
            tier, tier_rank = ('Plus', 3.0) if 'plus' in sl else (('Flash', 2.0) if 'flash' in sl else ('30B', 2.5))
            return {
                'raw': raw_name, 'family': 'Alibaba Qwen Omni',
                'version': ver, 'version_str': f"{ver:g}",
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        mq = re.search(r'qwen[- ]*(\d+(?:\.\d+)?)', sl)
        if mq:
            ver = float(mq.group(1))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            if re.search(r'\bmax\b', sl):
                return {
                    'raw': raw_name, 'family': 'Alibaba Qwen (Max/Plus/Flash)',
                    'version': ver, 'version_str': v_str,
                    'tier': 'Max', 'tier_rank': 3.0,
                    'effort': effort_name, 'effort_rank': effort_rank,
                    'variant_tag': variant_tag
                }
            elif re.search(r'\bplus\b', sl):
                return {
                    'raw': raw_name, 'family': 'Alibaba Qwen (Max/Plus/Flash)',
                    'version': ver, 'version_str': v_str,
                    'tier': 'Plus', 'tier_rank': 2.0,
                    'effort': effort_name, 'effort_rank': effort_rank,
                    'variant_tag': variant_tag
                }
            elif re.search(r'\b(flash|turbo)\b', sl):
                return {
                    'raw': raw_name, 'family': 'Alibaba Qwen (Max/Plus/Flash)',
                    'version': ver, 'version_str': v_str,
                    'tier': 'Flash', 'tier_rank': 1.0,
                    'effort': effort_name, 'effort_rank': effort_rank,
                    'variant_tag': variant_tag
                }
            elif '2.4t' in sl:
                tier, tier_rank = '2.4T', 2400.0
            else:
                mp = re.search(r'(\d+(?:\.\d+)?)b\b', sl)
                if mp:
                    b = float(mp.group(1))
                    tier, tier_rank = f"{b:g}B", b
                else:
                    return None
            q_fam = 'Alibaba Qwen'
            if 'coder' in sl:
                q_fam = 'Alibaba Qwen Coder'
            elif re.search(r'\bvl\b', sl):
                q_fam = 'Alibaba Qwen VL'
            return {
                'raw': raw_name, 'family': q_fam,
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 6. XAI GROK
    if 'grok' in sl and 'imagine' not in sl and 'build' not in sl:
        mgr = re.search(r'grok[- ]*(\d+(?:[.-]\d+)?)', sl)
        if mgr:
            ver_str_raw = mgr.group(1).replace('-', '.')
            ver = float(ver_str_raw)
            if ver == 4.20: v_str = '4.2'
            else: v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            tier, tier_rank = 'Base', 3.0
            if 'mini' in sl or 'fast' in sl: tier, tier_rank = 'Mini', 1.0
            return {
                'raw': raw_name, 'family': 'xAI Grok',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 7. META LLAMA & MUSE
    if 'muse' in sl and 'image' not in sl and 'video' not in sl:
        if 'wonder' in sl:
            ver = 1.0
            tier, tier_rank = ('Wonder Full', 4.5) if 'full' in sl else ('Wonder', 4.0)
            return {
                'raw': raw_name, 'family': 'Meta Muse',
                'version': ver, 'version_str': '1.0',
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        if 'spark' in sl:
            ms = re.search(r'spark[- ]*(\d+(?:\.\d+)?)', sl)
            ver = float(ms.group(1)) if ms else 1.0
            tier, tier_rank = ('Spark Open', 1.0) if 'open' in sl else ('Spark', 3.0)
            return {
                'raw': raw_name, 'family': 'Meta Muse Spark',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        if 'glimmer' in sl:
            return {
                'raw': raw_name, 'family': 'Meta Muse',
                'version': 1.0, 'version_str': '1.0',
                'tier': 'Glimmer', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'llama' in sl and 'nemotron' not in sl and 'hermes' not in sl and 'tulu' not in sl and 'openassistant' not in sl:
        mll = re.search(r'llama[- ]*(\d+(?:\.\d+)?)', sl)
        if mll:
            ver = float(mll.group(1))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            if 'behemoth' in sl: tier, tier_rank = 'Behemoth', 400.0
            elif 'maverick' in sl: tier, tier_rank = 'Maverick', 200.0
            elif 'scout' in sl: tier, tier_rank = 'Scout', 100.0
            else:
                mp = re.search(r'(\d+)b\b', sl)
                if not mp: return None
                b = float(mp.group(1))
                tier, tier_rank = f"{int(b)}B", b
            return {
                'raw': raw_name, 'family': 'Meta Llama',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 8. MISTRAL / MAGISTRAL / MINISTRAL
    if 'magistral' in sl:
        mm = re.search(r'(\d+(?:\.\d+)?)', sl)
        ver = float(mm.group(1)) if mm else 1.0
        tier, tier_rank = ('Medium', 2.0) if 'medium' in sl else ('Small', 1.0)
        return {
            'raw': raw_name, 'family': 'Mistral Magistral',
            'version': ver, 'version_str': f"{ver:.1f}",
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    if 'ministral' in sl:
        mp = re.search(r'(\d+)b\b', sl)
        if mp:
            b = float(mp.group(1))
            return {
                'raw': raw_name, 'family': 'Mistral Ministral',
                'version': 3.0, 'version_str': '3.0',
                'tier': f"{int(b)}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'mistral' in sl and 'hermes' not in sl:
        tier, tier_rank = None, None
        if 'large' in sl: tier, tier_rank = 'Large', 3.0
        elif 'medium' in sl: tier, tier_rank = 'Medium', 2.0
        elif 'small' in sl: tier, tier_rank = 'Small', 1.0
        if tier:
            mm = re.search(r'(?:large|medium|small)[- ]*(\d+(?:[.-]\d+)?)', sl)
            ver = float(mm.group(1).replace('-', '.')) if mm else 3.0
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            return {
                'raw': raw_name, 'family': 'Mistral',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 9. MOONSHOT KIMI
    if 'kimi' in sl:
        mk = re.search(r'k(\d+(?:\.\d+)?)', sl)
        if mk:
            ver = float(mk.group(1))
            v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
            tier, tier_rank = ('Pro', 3.0) if 'pro' in sl else ('Base', 2.0)
            if ('-max' in sl or '(max' in sl) and effort_rank < 6.0:
                effort_name, effort_rank = 'Max', 6.0
            return {
                'raw': raw_name, 'family': 'Moonshot Kimi',
                'version': ver, 'version_str': v_str,
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 10. Z.AI GLM
    if re.search(r'\bglm[- ]*(\d+(?:\.\d+)?)', sl) and 'based on glm' not in sl:
        mglm = re.search(r'\bglm[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(mglm.group(1))
        v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
        tier, tier_rank = 'Base', 3.0
        if 'flash' in sl: tier, tier_rank = 'Flash', 1.0
        elif 'air' in sl: tier, tier_rank = 'Air', 2.0
        if ('-max' in sl or '(max' in sl) and effort_rank < 6.0:
            effort_name, effort_rank = 'Max', 6.0
        return {
            'raw': raw_name, 'family': 'Z.AI GLM',
            'version': ver, 'version_str': v_str,
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 11. AMAZON NOVA
    if 'nova' in sl and 'hypernova' not in sl:
        mn = re.search(r'nova[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(mn.group(1)) if mn else 1.0
        v_str = f"{ver:.1f}"
        if 'omni' in sl:
            return {
                'raw': raw_name, 'family': 'Amazon Nova Omni',
                'version': ver, 'version_str': v_str,
                'tier': 'Omni', 'tier_rank': 3.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        tier, tier_rank = 'Lite', 2.0
        if 'premier' in sl: tier, tier_rank = 'Premier', 5.0
        elif 'pro' in sl: tier, tier_rank = 'Pro', 4.0
        elif 'lite' in sl: tier, tier_rank = 'Lite', 2.0
        elif 'micro' in sl: tier, tier_rank = 'Micro', 1.0
        return {
            'raw': raw_name, 'family': 'Amazon Nova',
            'version': ver, 'version_str': v_str,
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 12. XIAOMI MIMO
    if 'mimo' in sl:
        mm = re.search(r'v?(\d+(?:\.\d+)?)', sl)
        ver = float(mm.group(1)) if mm else 2.6
        tier, tier_rank = ('Pro', 3.0) if 'pro' in sl else ('Flash', 2.0)
        return {
            'raw': raw_name, 'family': 'Xiaomi MiMo',
            'version': ver, 'version_str': f"{ver:g}",
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 13. MINIMAX
    if 'minimax' in sl:
        mm = re.search(r'm(\d+(?:\.\d+)?)', sl)
        if mm:
            ver = float(mm.group(1))
            tier, tier_rank = ('Flash', 2.0) if 'flash' in sl else ('Base', 3.0)
            return {
                'raw': raw_name, 'family': 'MiniMax M-Series',
                'version': ver, 'version_str': f"{ver:g}",
                'tier': tier, 'tier_rank': tier_rank,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    # 14. NVIDIA NEMOTRON (exclude third-party fine-tunes like smaug-nemotron)
    if 'nemotron' in sl and 'smaug' not in sl and 'llama 3.1 nemotron' not in sl:
        if 'v2' in sl:
            ver = 2.0
        else:
            mn = re.search(r'nemotron[- ]*(?:super[- ]*vl[- ]*)?(\d+(?:\.\d+)?)', sl)
            ver = float(mn.group(1)) if mn else 3.0
        v_str = f"{ver:g}" if ver != int(ver) else f"{int(ver)}.0"
        tier, tier_rank = '30B', 30.0
        if 'ultra' in sl: tier, tier_rank = 'Ultra', 550.0
        elif 'super' in sl: tier, tier_rank = 'Super', 120.0
        elif '74b' in sl: tier, tier_rank = '74B', 74.0
        elif '30b' in sl or 'lightning' in sl: tier, tier_rank = '30B', 30.0
        elif '12b' in sl: tier, tier_rank = '12B', 12.0
        elif '9b' in sl: tier, tier_rank = '9B', 9.0
        elif 'nano' in sl: tier, tier_rank = 'Nano', 8.0
        elif '4b' in sl or 'e4b' in sl: tier, tier_rank = '4B', 4.0
        return {
            'raw': raw_name, 'family': 'NVIDIA Nemotron VL' if re.search(r'\bvl\b', sl) else 'NVIDIA Nemotron',
            'version': ver, 'version_str': v_str,
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 15. COHERE COMMAND
    if 'command' in sl:
        ver = 2.0 if 'command a' in sl else 1.0
        tier, tier_rank = ('Plus', 3.0) if '+' in sl or 'plus' in sl else ('Base', 2.0)
        return {
            'raw': raw_name, 'family': 'Cohere Command',
            'version': ver, 'version_str': f"{ver:.1f}",
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 16. THINKING MACHINES INKLING
    if 'inkling' in sl:
        tier, tier_rank = ('Small', 1.0) if 'small' in sl else ('Base', 2.0)
        return {
            'raw': raw_name, 'family': 'ThinkingMachines Inkling',
            'version': 1.0, 'version_str': '1.0',
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 17. ABACUS SMAUG
    if 'smaug' in sl and 'nemotron' not in sl:
        tier, tier_rank = 'Base', 2.0
        if 'agentic' in sl: tier, tier_rank = 'Agentic', 3.0
        elif 'flash' in sl: tier, tier_rank = 'Flash', 2.0
        elif 'mini' in sl: tier, tier_rank = 'Mini', 1.0
        return {
            'raw': raw_name, 'family': 'Abacus Smaug',
            'version': 1.0, 'version_str': '1.0',
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    # 18. OTHER PARAMETER/TIER FAMILIES
    if 'k2' in sl and ('horizon' in sl or 'k2-v2' in sl):
        mp = re.search(r'(\d+(?:\.\d+)?)b', sl)
        if mp:
            b = float(mp.group(1))
            return {
                'raw': raw_name, 'family': 'IFM K2 Horizon',
                'version': 2.0, 'version_str': '2.0',
                'tier': f"{b:g}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }
        if 'k2-v2' in sl:
            return {
                'raw': raw_name, 'family': 'IFM K2-V2',
                'version': 2.0, 'version_str': '2.0',
                'tier': 'Base', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'granite' in sl:
        mg = re.search(r'granite[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(mg.group(1)) if mg else 4.0
        mp = re.search(r'(\d+(?:\.\d+)?)(b|m)\b', sl)
        if mp:
            val = float(mp.group(1)) / (1000.0 if mp.group(2) == 'm' else 1.0)
            return {
                'raw': raw_name, 'family': 'IBM Granite',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': f"{mp.group(1)}{mp.group(2).upper()}", 'tier_rank': val,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'exaone' in sl and 'k-exaone' not in sl:
        me = re.search(r'exaone[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(me.group(1)) if me else 4.0
        mp = re.search(r'(\d+(?:\.\d+)?)b\b', sl)
        if mp:
            b = float(mp.group(1))
            return {
                'raw': raw_name, 'family': 'LG EXAONE',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': f"{b:g}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'olmo' in sl and 'molmo' not in sl:
        mo = re.search(r'olmo[- ]*(\d+(?:\.\d+)?)', sl)
        ver = float(mo.group(1)) if mo else 3.0
        mp = re.search(r'(\d+)b\b', sl)
        if mp:
            b = float(mp.group(1))
            return {
                'raw': raw_name, 'family': 'AllenAI Olmo',
                'version': ver, 'version_str': f"{ver:g}",
                'tier': f"{int(b)}B", 'tier_rank': b,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'phi-4' in sl:
        tier, tier_rank = ('Mini', 1.0) if 'mini' in sl else (('Multimodal', 2.0) if 'multimodal' in sl else ('Base', 3.0))
        return {
            'raw': raw_name, 'family': 'Microsoft Phi',
            'version': 4.0, 'version_str': '4.0',
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    if 'solar' in sl:
        tier, tier_rank = ('Pro', 3.0) if 'pro' in sl else (('Mini', 1.0) if 'mini' in sl else ('Open', 2.0))
        return {
            'raw': raw_name, 'family': 'Upstage Solar',
            'version': 4.0, 'version_str': '4.0',
            'tier': tier, 'tier_rank': tier_rank,
            'effort': effort_name, 'effort_rank': effort_rank,
            'variant_tag': variant_tag
        }

    if 'reve-' in sl:
        mr = re.search(r'reve-(\d+(?:\.\d+)?)', sl)
        if mr:
            ver = float(mr.group(1))
            return {
                'raw': raw_name, 'family': 'Reve Image',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': 'Base', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'mai-image' in sl:
        mm = re.search(r'mai-image-(\d+(?:\.\d+)?)', sl)
        if mm:
            ver = float(mm.group(1))
            return {
                'raw': raw_name, 'family': 'Microsoft MAI-Image',
                'version': ver, 'version_str': f"{ver:g}",
                'tier': 'Base', 'tier_rank': 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    if 'seedance' in sl:
        ms = re.search(r'seedance-(\d+(?:\.\d+)?)', sl)
        if ms:
            ver = float(ms.group(1))
            res = '1080p' if '1080p' in sl else '720p'
            return {
                'raw': raw_name, 'family': f'ByteDance Seedance ({res})',
                'version': ver, 'version_str': f"{ver:.1f}",
                'tier': 'Base', 'tier_rank': tier_rank if 'tier_rank' in locals() else 2.0,
                'effort': effort_name, 'effort_rank': effort_rank,
                'variant_tag': variant_tag
            }

    return None
