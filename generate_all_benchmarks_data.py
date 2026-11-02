import os
import json
import csv
import re
from compute_contradictions import evaluate_ranking, extract_rsc_json, parse_simple_yml_list

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CACHE_DIR = os.path.join(BASE_DIR, 'raw_data') if os.path.exists(os.path.join(BASE_DIR, 'raw_data')) else BASE_DIR

# Authoritative canonical "Popular" benchmarks tracked by labs and community
# Strictly benchmarks with >= 100 model submissions evaluated across Top 100 models (4,950 candidate pairs)
POPULAR_BENCHMARK_IDS = {
    # 1. LMSYS Chatbot Arena / Human Preference (>= 100 models)
    'lmsys_sub_overall',             # LMSYS Chatbot Arena — Overall (243 models)
    'lmsys_sub_hard_6',              # LMSYS Chatbot Arena — Hard (Arena-Hard) (243 models)
    'lmsys_sub_coding',              # LMSYS Chatbot Arena — Coding (243 models)
    'lmsys_sub_math',                # LMSYS Chatbot Arena — Math (243 models)
    'arena_2026_aug_code',           # Arena.ai Coding (108-Model Full Table) (108 models)

    # 2. Frontier Reasoning & Hard Science/Math (>= 100 models)
    'aa_v5_gpqa_diamond',            # GPQA Diamond (617 models)
    'aa_v5_humanitys_last_exam',     # Humanity's Last Exam (Full HLE) (677 models)
    'aa_v5_hle_diamond',             # HLE-Diamond (Humanity's Last Exam) (138 models)
    'aa_v5_aime_2025',               # AIME 2025 Competition Math (270 models)
    'aa_v5_critpt',                  # CritPt Physics Reasoning (594 models)

    # 3. Coding & Software Engineering (>= 100 models)
    'aa_v5_livecodebench',           # LiveCodeBench (343 models)
    'swebench_verified_all',         # SWE-bench Verified (All Submissions) (180 models)
    'aa_v5_scicode',                 # SciCode Scientific Coding (244 models)
    'evalplus_humaneval_plus',       # EvalPlus HumanEval+ (80x Tests) (125 models)
    'aa_v5_terminalbench_4_0',       # Terminal-Bench 4.0 (236 models)

    # 4. Agentic & Tool-Use Workflows (>= 100 models)
    'aa_v5_tau2_bench',              # Tau2-Bench Tool-Use Agentic (440 models)
    'aa_v5_automationbench_aa',       # AutomationBench-AA SaaS Workflows (239 models)
    'aa_v5_gdpval_aa_normalized',    # GDPval-AA Professional Work Elo (308 models)
    'aa_v5_aa_briefcase',            # AA-Briefcase v1.1 Knowledge Work (245 models)

    # 5. Long-Context, Instruction Following & Multimodal (>= 100 models)
    'aa_v5_ifbench',                 # IFBench Instruction Following (451 models)
    'aa_v5_artificial_analysis_long_context_reasoning', # AA Long-Context Reasoning (LCR) (589 models)
    'aa_v5_omniscience_net',         # AA-Omniscience v1.1 Net Score (107 models)
    'aa_v5_mmmu_pro',                # MMMU-Pro Multimodal Understanding (298 models)
}

def build_all_benchmarks():
    benchmarks = []

    def add_bench(suite, category, name, slug, metric_type, higher_is_better, unit, items, description=''):
        # Keep only quality measuring benchmarks across all
        if metric_type != 'quality':
            return
        # Only add if at least 10 valid items
        valid_cnt = sum(1 for x in items if x.get('score') is not None and not isinstance(x.get('score'), str))
        if valid_cnt < 10:
            return
        if slug in POPULAR_BENCHMARK_IDS:
            assert valid_cnt >= 100, f"Popular benchmark '{slug}' has only {valid_cnt} models, but popular benchmarks must have >= 100!"
        res_canonical = evaluate_ranking(items, metric_type=metric_type, higher_is_better=higher_is_better, top_k=100, deduplicate_canonical=True)
        res_raw = evaluate_ranking(items, metric_type=metric_type, higher_is_better=higher_is_better, top_k=100, deduplicate_canonical=False)
        res_full = evaluate_ranking(items, metric_type=metric_type, higher_is_better=higher_is_better, top_k=250, deduplicate_canonical=True)
        benchmarks.append({
            'id': slug,
            'is_popular': slug in POPULAR_BENCHMARK_IDS,
            'suite': suite,
            'category': category,
            'name': name,
            'metric_type': metric_type, # 'quality' | 'latency' | 'cost'
            'higher_is_better': higher_is_better,
            'unit': unit,
            'total_models': valid_cnt,
            'description': description,
            'canonical_top25': res_canonical,
            'raw_top25': res_raw,
            'full_canonical': {
                'top_k_count': res_full['top_k_count'],
                'comparable_pairs_count': res_full['comparable_pairs_count'],
                'contradictions_count': res_full['contradictions_count'],
                'contradiction_score': res_full['contradiction_score'],
                'weighted_contradiction_score': res_full['weighted_contradiction_score'],
                'by_axis': res_full['by_axis'],
                'contradictions': res_full['contradictions'][:30],
            }
        })

    decoder = json.JSONDecoder()

    # =========================================================================
    # 1. ARTIFICIAL ANALYSIS v5.0 (Oct 2026 Live — Full 719-Model Evaluation Database)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'aa_leaderboards_models.html'), 'r', encoding='utf-8') as f:
        aa_lb_rsc = extract_rsc_json(f.read())
    idx = aa_lb_rsc.find('"initialModels":[')
    aa_lb_models, _ = decoder.raw_decode(aa_lb_rsc[idx + len('"initialModels":'):])

    aa_full_path = os.path.join(CACHE_DIR, 'aa_full_evaluations_719_models.json')
    if os.path.exists(aa_full_path):
        with open(aa_full_path, 'r', encoding='utf-8') as f:
            aa_all_models = json.load(f).get('models', [])
    else:
        aa_all_models = []

    skey_to_model_key = {
        'hle-diamond': 'hleDiamond',
        'humanitys-last-exam': 'hle',
        'gpqa-diamond': 'gpqa',
        'aime-2025': 'aime25',
        'critpt': 'critpt',
        'critpt-v2-hard': 'critptAgenticHard',
        'terminal-bench-science': 'terminalBenchScience',
        'frontiercode-2-0': 'frontierCode20',
        'frontiercode': 'frontierCode',
        'terminalbench-4-0': 'terminalBench40',
        'terminalbench-2-1': 'terminalBench21',
        'terminalbench-hard': 'terminalbenchHard',
        'scicode': 'scicode',
        'livecodebench': 'livecodebench',
        'code2video-aa': 'code2videoElo',
        'aa-briefcase': 'briefcaseElo',
        'gdpval-aa-normalized': 'gdpval',
        'gdp-pdf': 'gdpPdfAllPass',
        'automationbench-aa': 'automationBenchPartialScore',
        'tau2-bench': 'tau2',
        'tau3-banking': 'tauBanking',
        'aa-analyst-agent': 'analystAgent',
        'harvey-lab-aa': 'harveyLab',
        'enterprise-ops-gym-aa': 'enterpriseOpsGym',
        'itbench-aa': 'itbenchSre',
        'artificial-analysis-long-context-reasoning': 'lcr',
        'mlcr-aa': 'mlcrOverall',
        'ifbench': 'ifbench',
        'mmmu-pro': 'mmmuPro',
        'healthbench': 'healthbench',
        'healthbench-professional': 'healthbenchProfessional',
    }

    intel_source = aa_all_models if aa_all_models else aa_lb_models
    # Top-level metrics on aa_lb_models
    add_bench(
        'Artificial Analysis v5', 'Composite & Frontier', 'AA Intelligence Index v5.0', 'aa_v5_intelligence_index',
        'quality', True, 'Index (0-100)',
        [{'name': m['name'], 'score': m.get('intelligenceIndex'), 'is_reasoning': m.get('isReasoning')} for m in intel_source if m.get('intelligenceIndex') is not None],
        'Flagship composite intelligence index across reasoning, coding, knowledge, and agentic evaluations.'
    )
    add_bench(
        'Artificial Analysis v5', 'Knowledge & Hallucination', 'AA-Omniscience v1.1 Net Score', 'aa_v5_omniscience_net',
        'quality', True, 'Net Score',
        [{'name': m['name'], 'score': m.get('omniscience'), 'is_reasoning': m.get('isReasoning')} for m in intel_source if m.get('omniscience') is not None],
        '3,000-question knowledge & hallucination benchmark penalizing confident incorrect answers.'
    )

    aa_score_defs = [
        ('hle-diamond', 'Composite & Frontier', 'HLE-Diamond (Humanity\'s Last Exam)', 'quality', True, 'Accuracy', 'Diamond subset of Humanity\'s Last Exam frontier reasoning benchmark.'),
        ('humanitys-last-exam', 'Composite & Frontier', 'Humanity\'s Last Exam (Full HLE)', 'quality', True, 'Accuracy', 'Full Humanity\'s Last Exam frontier academic reasoning test.'),
        ('gpqa-diamond', 'Science & Math Reasoning', 'GPQA Diamond', 'quality', True, 'Accuracy', 'PhD-level Google-Proof Q&A across biology, physics, and chemistry.'),
        ('aime-2025', 'Science & Math Reasoning', 'AIME 2025 Competition Math', 'quality', True, 'Accuracy', 'American Invitational Mathematics Examination 2025 competition problems.'),
        ('critpt', 'Science & Math Reasoning', 'CritPt Physics Reasoning', 'quality', True, 'Accuracy', 'Unpublished university physics research reasoning problems.'),
        ('critpt-v2-hard', 'Science & Math Reasoning', 'CritPt v2 Agentic Hard', 'quality', True, 'Accuracy', 'Hard agentic physics research problems in CritPt v2.'),
        ('terminal-bench-science', 'Science & Math Reasoning', 'Terminal-Bench Science 0.1', 'quality', True, 'Pass Rate', 'Scientific computing and research tasks executed in a terminal environment.'),
        ('frontiercode-2-0', 'Coding & Software Eng', 'FrontierCode 2.0', 'quality', True, 'Pass Rate', 'Next-generation software engineering & rubric-graded code benchmark.'),
        ('frontiercode', 'Coding & Software Eng', 'FrontierCode 1.0', 'quality', True, 'Pass Rate', 'Frontier software engineering and repository coding benchmark.'),
        ('terminalbench-4-0', 'Coding & Software Eng', 'Terminal-Bench 4.0', 'quality', True, 'Pass Rate', 'Interactive command-line and terminal engineering benchmark v4.0.'),
        ('terminalbench-2-1', 'Coding & Software Eng', 'Terminal-Bench 2.1', 'quality', True, 'Pass Rate', 'Terminal command-line systems engineering benchmark v2.1.'),
        ('terminalbench-hard', 'Coding & Software Eng', 'Terminal-Bench Hard', 'quality', True, 'Pass Rate', 'Hard subset of Terminal-Bench command-line engineering tasks.'),
        ('scicode', 'Coding & Software Eng', 'SciCode Scientific Coding', 'quality', True, 'Pass Rate', 'Research-level scientific computing coding synthesis across natural sciences.'),
        ('livecodebench', 'Coding & Software Eng', 'LiveCodeBench', 'quality', True, 'Pass Rate', 'Contamination-free competitive programming benchmark from LeetCode/AtCoder/Codeforces.'),
        ('code2video-aa', 'Coding & Software Eng', 'Code2Video-AA Elo', 'quality', True, 'Elo', 'Programmatic motion graphics and HTML/animation synthesis benchmark.'),
        ('aa-3d', 'Coding & Software Eng', 'AA-3D Interactive WebGL Elo', 'quality', True, 'Elo', 'Interactive 3D scene and Three.js/WebGL generation Elo leaderboard.'),
        ('aa-briefcase', 'Agentic & Enterprise', 'AA-Briefcase v1.1 Knowledge Work', 'quality', True, 'Elo', 'End-to-end agentic professional knowledge work deliverables.'),
        ('gdpval-aa-normalized', 'Agentic & Enterprise', 'GDPval-AA Professional Work Elo', 'quality', True, 'Elo', 'Normalized Elo rating across high-GDP professional knowledge workflows.'),
        ('gdp-pdf', 'Agentic & Enterprise', 'GDP.pdf Document Deliverable', 'quality', True, 'All-Pass Rate', 'Long-context PDF and professional document generation benchmark.'),
        ('automationbench-aa', 'Agentic & Enterprise', 'AutomationBench-AA SaaS Workflows', 'quality', True, 'Score', 'Multi-step enterprise SaaS automation and tool orchestration benchmark.'),
        ('tau2-bench', 'Agentic & Enterprise', 'Tau2-Bench Tool-Use Agentic', 'quality', True, 'Pass Rate', 'Dual-control conversational customer service and tool-use agent benchmark.'),
        ('tau3-banking', 'Agentic & Enterprise', 'Tau3-Banking Agentic Benchmark', 'quality', True, 'Pass Rate', 'Multi-step financial and banking policy compliance agent benchmark.'),
        ('aa-analyst-agent', 'Agentic & Enterprise', 'AA-AnalystAgent Data Analyst', 'quality', True, 'Pass Rate', 'Autonomous business intelligence and data analysis agent benchmark.'),
        ('harvey-lab-aa', 'Agentic & Enterprise', 'Harvey LAB-AA v1.1 Legal Agent', 'quality', True, 'Score', 'Legal workflow and hallucination-checked contract deliverable benchmark.'),
        ('enterprise-ops-gym-aa', 'Agentic & Enterprise', 'EnterpriseOps-Gym-AA', 'quality', True, 'Pass Rate', 'ServiceNow enterprise IT & workflow operations agent benchmark.'),
        ('itbench-aa', 'Agentic & Enterprise', 'ITBench-AA SRE & Root Cause', 'quality', True, 'Pass Rate', 'Kubernetes site reliability engineering and root-cause analysis benchmark.'),
        ('artificial-analysis-long-context-reasoning', 'Long-Context & Instruction', 'AA Long-Context Reasoning (LCR)', 'quality', True, 'Accuracy', 'Long-context multi-hop reasoning across extended context windows.'),
        ('mlcr-aa', 'Long-Context & Instruction', 'MLCR-AA Medical Long-Context', 'quality', True, 'Accuracy', 'Medical claims and clinical record long-context reasoning benchmark.'),
        ('ifbench', 'Long-Context & Instruction', 'IFBench Instruction Following', 'quality', True, 'Accuracy', 'Strict verifiable constraint and instruction-following benchmark.'),
        ('mmmu-pro', 'Multimodal & Vision', 'MMMU-Pro Multimodal Understanding', 'quality', True, 'Accuracy', 'Massive Multi-discipline Multimodal Understanding professional vision benchmark.'),
        ('omniscience-accuracy', 'Knowledge & Hallucination', 'AA-Omniscience Raw Accuracy', 'quality', True, 'Accuracy', 'Raw factual accuracy on AA-Omniscience 3,000-question suite.'),
        ('omniscience-non-hallucination', 'Knowledge & Hallucination', 'AA-Omniscience Non-Hallucination Rate', 'quality', True, 'Rate', 'Proportion of unknown questions where model abstains rather than hallucinating.'),
        ('healthbench', 'Science & Math Reasoning', 'OpenAI HealthBench Medical Reasoning', 'quality', True, 'Score', 'Physician-graded clinical and medical reasoning benchmark.'),
        ('healthbench-professional', 'Science & Math Reasoning', 'HealthBench Professional Clinical', 'quality', True, 'Score', 'Professional clinician-level medical case reasoning benchmark.'),
    ]
    for skey, cat, title, mtype, hib, unit, desc in aa_score_defs:
        if aa_all_models and skey in skey_to_model_key:
            mkey = skey_to_model_key[skey]
            items = [
                {'name': m['name'], 'score': m[mkey], 'is_reasoning': m.get('isReasoning')}
                for m in aa_all_models
                if m.get(mkey) is not None and not isinstance(m.get(mkey), (bool, str, dict, list))
            ]
        else:
            items = [
                {'name': m['name'], 'score': (m.get('scores') or {}).get(skey), 'is_reasoning': m.get('isReasoning')}
                for m in aa_lb_models
            ]
        add_bench('Artificial Analysis v5', cat, title, f"aa_v5_{skey.replace('-', '_')}", mtype, hib, unit, items, desc)

    # AA v5 Cost & Reasoning Latency on /leaderboards/models
    add_bench(
        'Artificial Analysis v5', 'Cost & Pricing', 'AA API Input Price ($/1M Tokens)', 'aa_v5_price_input',
        'cost', True, '$/1M Tokens',
        [{'name': m['name'], 'score': m.get('price1mInputTokens'), 'is_reasoning': m.get('isReasoning')} for m in aa_lb_models if (m.get('price1mInputTokens') or 0) > 0],
        'API input token price per 1M tokens (sorted descending so Sol >= Terra >= Luna is expected top-to-bottom order).'
    )
    add_bench(
        'Artificial Analysis v5', 'Cost & Pricing', 'AA API Output Price ($/1M Tokens)', 'aa_v5_price_output',
        'cost', True, '$/1M Tokens',
        [{'name': m['name'], 'score': m.get('price1mOutputTokens'), 'is_reasoning': m.get('isReasoning')} for m in aa_lb_models if (m.get('price1mOutputTokens') or 0) > 0],
        'API output token price per 1M tokens (sorted descending so Sol >= Terra >= Luna is expected top-to-bottom order).'
    )
    add_bench(
        'Artificial Analysis v5', 'Cost & Pricing', 'AA API Blended Price (3:1 In:Out $/1M)', 'aa_v5_price_blended',
        'cost', True, '$/1M Tokens',
        [
            {'name': m['name'], 'score': (3.0 * m['price1mInputTokens'] + m['price1mOutputTokens']) / 4.0, 'is_reasoning': m.get('isReasoning')}
            for m in aa_lb_models
            if m.get('price1mInputTokens') is not None and m.get('price1mOutputTokens') is not None and (m['price1mInputTokens'] + m['price1mOutputTokens']) > 0
        ],
        'Blended 3:1 input/output API price per 1M tokens (Sol >= Terra >= Luna expected).'
    )
    add_bench(
        'Artificial Analysis v5', 'Latency & Speed', 'AA Median Reasoning Time (Seconds)', 'aa_v5_reasoning_time',
        'latency', False, 'Seconds',
        [{'name': m['name'], 'score': m.get('medianReasoningTimeSeconds'), 'is_reasoning': m.get('isReasoning')} for m in aa_lb_models if (m.get('medianReasoningTimeSeconds') or 0) > 0],
        'Median internal thinking/reasoning time in seconds before first answer token (smaller models expected faster).'
    )

    # =========================================================================
    # 2. ARTIFICIAL ANALYSIS v5 PROVIDERS & FRONTIER MODELS (/leaderboards/providers & /models)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'aa_leaderboards_providers.html'), 'r', encoding='utf-8') as f:
        aa_prov_rsc = extract_rsc_json(f.read())
    idx = aa_prov_rsc.find('"initialRows":[')
    aa_prov_rows, _ = decoder.raw_decode(aa_prov_rsc[idx + len('"initialRows":'):])

    # Identify first-party hosts vs third-party hosts
    first_party_slugs = {'openai', 'anthropic', 'google', 'alibaba_cloud', 'deepseek', 'mistral', 'xai', 'kimi', 'minimax', 'zhipu'}
    speed_items = []
    ttft_items = []
    ttfat_items = []
    e2e_items = []
    for r in aa_prov_rows:
        perf = r.get('performance') or {}
        m_obj = r.get('model') or {}
        is_fp = r.get('host', {}).get('slug') in first_party_slugs
        lbl = r.get('label', '')
        # Clean host suffixes like "AI Studio", "Vertex" so model parser groups cleanly while prioritizing first-party
        clean_lbl = re.sub(r'\s+(?:AI Studio|Vertex|\(Vertex\)|\(AI Studio\))$', '', lbl)
        if perf.get('medianOutputTokensPerSecond'):
            speed_items.append({'name': clean_lbl, 'score': perf['medianOutputTokensPerSecond'], 'is_reasoning': m_obj.get('reasoningModel'), 'is_first_party': is_fp})
        if perf.get('medianTimeToFirstTokenSeconds'):
            ttft_items.append({'name': clean_lbl, 'score': perf['medianTimeToFirstTokenSeconds'], 'is_reasoning': m_obj.get('reasoningModel'), 'is_first_party': is_fp})
        if perf.get('medianTimeToFirstAnswerTokenSeconds'):
            ttfat_items.append({'name': clean_lbl, 'score': perf['medianTimeToFirstAnswerTokenSeconds'], 'is_reasoning': m_obj.get('reasoningModel'), 'is_first_party': is_fp})
        if perf.get('medianEndToEndResponseTimeSeconds'):
            e2e_items.append({'name': clean_lbl, 'score': perf['medianEndToEndResponseTimeSeconds'], 'is_reasoning': m_obj.get('reasoningModel'), 'is_first_party': is_fp})

    add_bench('Artificial Analysis v5', 'Latency & Speed', 'AA Output Speed (Median Tokens/Sec)', 'aa_v5_output_speed', 'latency', True, 'Tokens/Sec', speed_items, 'Median output generation speed in tokens/sec (higher is faster; Luna > Terra > Sol expected).')
    add_bench('Artificial Analysis v5', 'Latency & Speed', 'AA Time to First Token (TTFT Seconds)', 'aa_v5_ttft_seconds', 'latency', False, 'Seconds', ttft_items, 'Median latency to first token in seconds (lower is faster; Luna < Terra < Sol expected).')
    add_bench('Artificial Analysis v5', 'Latency & Speed', 'AA Time to First Answer Token (Seconds)', 'aa_v5_ttfat_seconds', 'latency', False, 'Seconds', ttfat_items, 'Median time including reasoning until first visible answer token (lower is faster).')
    add_bench('Artificial Analysis v5', 'Latency & Speed', 'AA End-to-End Response Time (Seconds)', 'aa_v5_e2e_seconds', 'latency', False, 'Seconds', e2e_items, 'Median total end-to-end response latency in seconds (lower is faster; Luna < Terra < Sol expected).')

    # AA /models 28 Frontier Models (Total Cost to Run Benchmark & Time per Task)
    with open(os.path.join(CACHE_DIR, 'aa_models.html'), 'r', encoding='utf-8') as f:
        aa_mod_rsc = extract_rsc_json(f.read())
    idx = aa_mod_rsc.find('"initialModels":[')
    aa_mod_models, _ = decoder.raw_decode(aa_mod_rsc[idx + len('"initialModels":'):])

    add_bench(
        'Artificial Analysis v5', 'Cost & Pricing', 'AA Intelligence Index Total Run Cost ($ USD)', 'aa_v5_total_run_cost',
        'cost', True, 'USD ($)',
        [{'name': m['name'], 'score': (m.get('intelligenceIndexCost') or {}).get('total'), 'is_reasoning': m.get('isReasoning')} for m in aa_mod_models if (m.get('intelligenceIndexCost') or {}).get('total')],
        'Total dollar expenditure to run the full Artificial Analysis Intelligence Index suite (Sol expected to cost >= Terra >= Luna).'
    )
    add_bench(
        'Artificial Analysis v5', 'Cost & Pricing', 'AA-Briefcase Total Suite Cost ($ USD)', 'aa_v5_briefcase_total_cost',
        'cost', True, 'USD ($)',
        [{'name': m['name'], 'score': m.get('briefcaseTotalCost'), 'is_reasoning': m.get('isReasoning')} for m in aa_mod_models if m.get('briefcaseTotalCost')],
        'Total dollar expenditure to run the AA-Briefcase knowledge work evaluation.'
    )
    add_bench(
        'Artificial Analysis v5', 'Latency & Speed', 'AA Intelligence Index Time per Task (Seconds)', 'aa_v5_time_per_task',
        'latency', False, 'Seconds',
        [{'name': m['name'], 'score': m.get('intelligenceIndexTimePerTask'), 'is_reasoning': m.get('isReasoning')} for m in aa_mod_models if m.get('intelligenceIndexTimePerTask')],
        'Mean wall-clock execution time per Intelligence Index task in seconds (smaller models expected faster).'
    )

    # Sub-evaluation Total Cost per Task ($/Task) and Wall-Clock Time per Task (Seconds) from aa_models.html
    sub_eval_meta = [
        ('aa-briefcase', 'AA-Briefcase v1.1'),
        ('automationbench-aa', 'AutomationBench-AA'),
        ('terminalbench-4-0', 'Terminal-Bench 4.0'),
        ('frontiercode-2-0', 'FrontierCode 2.0'),
        ('omniscience', 'AA-Omniscience v1.1'),
        ('gdp-pdf', 'GDP.pdf Document'),
        ('hle-diamond', 'HLE-Diamond'),
        ('critpt-v2-hard', 'CritPt v2 Hard'),
        ('terminal-bench-science', 'Terminal-Bench Science'),
    ]
    for eslug, etitle in sub_eval_meta:
        c_items = []
        t_items = []
        for m in aa_mod_models:
            for e in (m.get('intelligenceIndexEvaluations') or []):
                if e.get('slug') == eslug:
                    if e.get('costPerTask') is not None and e['costPerTask'] > 0:
                        c_items.append({'name': m['name'], 'score': e['costPerTask'], 'is_reasoning': m.get('isReasoning')})
                    if e.get('timePerTask') is not None and e['timePerTask'] > 0:
                        t_items.append({'name': m['name'], 'score': e['timePerTask'], 'is_reasoning': m.get('isReasoning')})
        add_bench(
            'Artificial Analysis v5', 'Cost & Pricing', f"{etitle} — Total Cost per Task ($ USD)", f"aa_v5_eval_cost_{eslug.replace('-', '_')}",
            'cost', True, 'USD/Task', c_items,
            f"Average total API dollar expenditure per task on {etitle} (Sol expected to cost >= Terra >= Luna)."
        )
        add_bench(
            'Artificial Analysis v5', 'Latency & Speed', f"{etitle} — Wall-Clock Time per Task (Sec)", f"aa_v5_eval_time_{eslug.replace('-', '_')}",
            'latency', False, 'Seconds/Task', t_items,
            f"Average wall-clock completion time in seconds per task on {etitle} (smaller models expected faster)."
        )

    # =========================================================================
    # 3. ARTIFICIAL ANALYSIS v4.0 (Aug 2026 Historical Dataset — 595 Models)
    # =========================================================================
    hist_path = '/Users/sagar-sayali/ai-frontier-ratio-dashboard/benchmarks_historical_data.json'
    if os.path.exists(hist_path):
        with open(hist_path, 'r', encoding='utf-8') as f:
            hist_d = json.load(f)
        aa_v4_models = hist_d['artificialAnalysis']['models']
        v4_defs = [
            ('intelligenceIndex', 'Composite & Frontier', 'AA v4 Intelligence Index (Aug 2026)', 'quality', True, 'Index'),
            ('codingIndex', 'Coding & Software Eng', 'AA v4 Coding Index (Aug 2026)', 'quality', True, 'Index'),
            ('agenticIndex', 'Agentic & Enterprise', 'AA v4 Agentic Index (Aug 2026)', 'quality', True, 'Index'),
            ('tauBanking', 'Agentic & Enterprise', 'AA v4 Tau-Bench Banking (Aug 2026)', 'quality', True, 'Accuracy'),
            ('terminalbench', 'Coding & Software Eng', 'AA v4 Terminal-Bench (Aug 2026)', 'quality', True, 'Pass Rate'),
            ('scicode', 'Coding & Software Eng', 'AA v4 SciCode (Aug 2026)', 'quality', True, 'Pass Rate'),
            ('omniscience', 'Knowledge & Hallucination', 'AA v4 Omniscience (Aug 2026)', 'quality', True, 'Score'),
            ('gpqa', 'Science & Math Reasoning', 'AA v4 GPQA Diamond (Aug 2026)', 'quality', True, 'Accuracy'),
            ('hle', 'Composite & Frontier', 'AA v4 Humanity\'s Last Exam (Aug 2026)', 'quality', True, 'Accuracy'),
            ('critpt', 'Science & Math Reasoning', 'AA v4 CritPt Physics (Aug 2026)', 'quality', True, 'Accuracy'),
            ('tokensPerSec', 'Latency & Speed', 'AA v4 Output Speed (Tokens/Sec, Aug 2026)', 'latency', True, 'Tokens/Sec'),
            ('ttftSec', 'Latency & Speed', 'AA v4 Latency TTFT (Seconds, Aug 2026)', 'latency', False, 'Seconds'),
            ('price1mBlended', 'Cost & Pricing', 'AA v4 Blended API Price ($/1M, Aug 2026)', 'cost', True, '$/1M Tokens'),
        ]
        for k, cat, title, mtype, hib, unit in v4_defs:
            items = [{'name': m['name'], 'score': m.get(k), 'is_reasoning': m.get('isReasoning')} for m in aa_v4_models if m.get(k) is not None and (mtype != 'cost' or m.get(k) > 0)]
            add_bench('Artificial Analysis v4 (Aug 2026)', cat, title, f"aa_v4_{k.lower()}", mtype, hib, unit, items, f"595-model Artificial Analysis v4 snapshot ({title}).")

    # =========================================================================
    # 4. LIVEBENCH 2.0 (Oct 2026 Live — Quality & Task Cost)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'lb2_20261025_table.csv'), 'r', encoding='utf-8') as f:
        lb2_rows = list(csv.DictReader(f))
    with open(os.path.join(CACHE_DIR, 'lb2_20261025_categories.json'), 'r', encoding='utf-8') as f:
        lb2_cats = json.load(f)
    weights = lb2_cats.get('_overall_weights', {})

    # Compute LiveBench 2.0 weighted overall score
    lb2_overall_items = []
    lb2_cat_cols = ['long_agentic', 'reasoning', 'coding', 'browser', 'data_analysis', 'research', 'design']
    cat_name_map = {
        'long_agentic': 'Long Agentic', 'reasoning': 'Reasoning', 'coding': 'Coding',
        'browser': 'Browser', 'data_analysis': 'Data Analysis', 'research': 'Research', 'design': 'Design'
    }
    for r in lb2_rows:
        w_sum, w_tot = 0.0, 0.0
        for col in lb2_cat_cols:
            val = float(r[col])
            w = float(weights.get(cat_name_map[col], 1.0))
            w_sum += val * w
            w_tot += w
        lb2_overall_items.append({'name': r['model'], 'score': w_sum / w_tot})

    add_bench('LiveBench 2.0 (Oct 2026)', 'Composite & Frontier', 'LiveBench 2.0 Overall Score', 'lb2_overall', 'quality', True, 'Score (0-100)', lb2_overall_items, 'Contamination-free weighted overall score across 7 agentic, coding, research, and reasoning categories.')
    for col in lb2_cat_cols:
        cname = cat_name_map[col]
        cat_group = 'Coding & Software Eng' if col in ('coding', 'design') else ('Agentic & Enterprise' if col in ('long_agentic', 'browser', 'research', 'data_analysis') else 'Science & Math Reasoning')
        items = [{'name': r['model'], 'score': float(r[col])} for r in lb2_rows if r.get(col)]
        add_bench('LiveBench 2.0 (Oct 2026)', cat_group, f"LiveBench 2.0 — {cname}", f"lb2_{col}", 'quality', True, 'Score (0-100)', items, f"LiveBench 2.0 {cname} evaluation.")

    # LiveBench 2.0 Cost per Task (from cost.csv)
    with open(os.path.join(CACHE_DIR, 'lb2_20261025_cost.csv'), 'r', encoding='utf-8') as f:
        lb2_cost_rows = list(csv.DictReader(f))
    lb2_cost_cols = ['long_agentic', 'coding', 'browser', 'data_analysis', 'research', 'design']
    lb2_overall_cost_items = []
    for r in lb2_cost_rows:
        vals = []
        for col in lb2_cost_cols:
            try:
                v = float(r.get(col, ''))
                if v > 0:
                    vals.append(v)
            except Exception:
                pass
        if vals:
            lb2_overall_cost_items.append({'name': r['model'], 'score': sum(vals) / len(vals)})
    add_bench('LiveBench 2.0 (Oct 2026)', 'Cost & Pricing', 'LiveBench 2.0 Cost — Overall Mean ($/Task)', 'lb2_cost_overall', 'cost', True, 'USD/Task', lb2_overall_cost_items, 'Mean total API expenditure per task across all LiveBench 2.0 agentic and coding categories.')

    for col in lb2_cost_cols:
        cname = cat_name_map[col]
        items = []
        for r in lb2_cost_rows:
            try:
                v = float(r.get(col, ''))
                if v > 0:
                    items.append({'name': r['model'], 'score': v})
            except Exception:
                pass
        add_bench('LiveBench 2.0 (Oct 2026)', 'Cost & Pricing', f"LiveBench 2.0 Cost — {cname} ($/Task)", f"lb2_cost_{col}", 'cost', True, 'USD/Task', items, f"Total API cost per task on LiveBench 2.0 {cname} (Sol expected to cost >= Terra >= Luna).")

    # =========================================================================
    # 5. LIVEBENCH v1 (Latest Release 2026-06-25 — 71 Frontier Models)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'lb1_2026_06_25_table.csv'), 'r', encoding='utf-8') as f:
        lb1_rows = list(csv.DictReader(f))
    with open(os.path.join(CACHE_DIR, 'lb1_2026_06_25_categories.json'), 'r', encoding='utf-8') as f:
        lb1_cats = json.load(f)

    lb1_cat_scores_by_model = {r['model']: {} for r in lb1_rows}
    for cat_name, subtasks in lb1_cats.items():
        cat_items = []
        for r in lb1_rows:
            vals = []
            for st in subtasks:
                try:
                    vals.append(float(r[st]))
                except Exception:
                    pass
            if vals:
                avg_v = sum(vals) / len(vals)
                lb1_cat_scores_by_model[r['model']][cat_name] = avg_v
                cat_items.append({'name': r['model'], 'score': avg_v})
        cat_group = 'Coding & Software Eng' if 'Coding' in cat_name else ('Science & Math Reasoning' if cat_name in ('Reasoning', 'Mathematics') else 'Long-Context & Instruction')
        add_bench('LiveBench v1 (2026)', cat_group, f"LiveBench v1 — {cat_name}", f"lb1_{cat_name.lower().replace(' ', '_')}", 'quality', True, 'Score (0-100)', cat_items, f"LiveBench v1 category average across {', '.join(subtasks)}.")

    lb1_overall_items = []
    for m_name, cdict in lb1_cat_scores_by_model.items():
        if cdict:
            lb1_overall_items.append({'name': m_name, 'score': sum(cdict.values()) / len(cdict)})
    add_bench('LiveBench v1 (2026)', 'Composite & Frontier', 'LiveBench v1 Global Average', 'lb1_overall', 'quality', True, 'Score (0-100)', lb1_overall_items, 'Mean of 7 category averages across 23 objective contamination-free tasks.')

    # LiveBench v1 Cost & Output Verbosity
    with open(os.path.join(CACHE_DIR, 'lb1_2026_06_25_cost.csv'), 'r', encoding='utf-8') as f:
        lb1_cost_rows = list(csv.DictReader(f))
    add_bench(
        'LiveBench v1 (2026)', 'Cost & Pricing', 'LiveBench v1 Cost per Question ($ USD)', 'lb1_cost_per_question',
        'cost', True, 'USD/Question',
        [{'name': r['model'], 'score': float(r['cost_per_question'])} for r in lb1_cost_rows if r.get('cost_per_question') and float(r['cost_per_question']) > 0],
        'Average dollar cost per benchmark question across all 23 LiveBench v1 tasks (Sol/Opus expected >= Terra/Sonnet >= Luna/Haiku).'
    )
    add_bench(
        'LiveBench v1 (2026)', 'Cost & Pricing', 'LiveBench v1 Cost per Successful Task ($ USD)', 'lb1_cost_per_success',
        'cost', True, 'USD/Success',
        [{'name': r['model'], 'score': float(r['cost_per_successful_task'])} for r in lb1_cost_rows if r.get('cost_per_successful_task') and float(r['cost_per_successful_task']) > 0],
        'Total benchmark cost divided by number of solved tasks on LiveBench v1.'
    )

    # =========================================================================
    # 6. LMSYS CHATBOT ARENA / ARENA.AI (2026 Multi-Domain + Classic Sub-Leaderboards)
    # =========================================================================
    arena_2026_defs = [
        ('arena_2026-10-07_text.json', 'Composite & Frontier', 'Arena.ai Text Overall (Oct 2026)', 'arena_2026_oct_text'),
        ('arena_2026-06-25_text.json', 'Composite & Frontier', 'Arena.ai Text Overall (50-Model Snapshot)', 'arena_2026_jun_text'),
        ('arena_2026-10-07_code.json', 'Coding & Software Eng', 'Arena.ai Coding (Oct 2026)', 'arena_2026_oct_code'),
        ('arena_2026-08-01_code.json', 'Coding & Software Eng', 'Arena.ai Coding (108-Model Full Table)', 'arena_2026_aug_code'),
        ('arena_2026-07-15_agent.json', 'Agentic & Enterprise', 'Arena.ai Agentic Leaderboard', 'arena_2026_agent'),
        ('arena_2026-10-07_document.json', 'Long-Context & Instruction', 'Arena.ai Document Comprehension', 'arena_2026_document'),
        ('arena_2026-10-07_search.json', 'Knowledge & Hallucination', 'Arena.ai Search & Grounding', 'arena_2026_search'),
        ('arena_2026-10-07_vision.json', 'Multimodal & Vision', 'Arena.ai Vision Multimodal (Oct 2026)', 'arena_2026_oct_vision'),
        ('arena_2026-08-01_vision.json', 'Multimodal & Vision', 'Arena.ai Vision Multimodal (30-Model Table)', 'arena_2026_aug_vision'),
        ('arena_2026-08-01_text-to-image.json', 'Multimodal & Vision', 'Arena.ai Text-to-Image Generation', 'arena_2026_t2i'),
        ('arena_2026-10-07_image-edit.json', 'Multimodal & Vision', 'Arena.ai Image Editing', 'arena_2026_image_edit'),
        ('arena_2026-10-07_text-to-video.json', 'Multimodal & Vision', 'Arena.ai Text-to-Video Generation', 'arena_2026_t2v'),
        ('arena_2026-10-07_image-to-video.json', 'Multimodal & Vision', 'Arena.ai Image-to-Video Generation', 'arena_2026_i2v'),
    ]
    for fn, cat, title, slug in arena_2026_defs:
        p = os.path.join(CACHE_DIR, fn)
        if os.path.exists(p):
            with open(p, 'r', encoding='utf-8') as f:
                d = json.load(f)
            items = [{'name': m['model'], 'score': float(m['score'])} for m in d.get('models', []) if m.get('score') is not None]
            add_bench('LMSYS Arena.ai (2026)', cat, title, slug, 'quality', True, 'Elo', items, f"Blind crowdsourced human preference Elo leaderboard ({title}).")

    # Classic LMSYS Arena sub-categories from nakasyou_latest.json
    nak_path = os.path.join(CACHE_DIR, 'nakasyou_latest.json')
    if os.path.exists(nak_path):
        with open(nak_path, 'r', encoding='utf-8') as f:
            nak = json.load(f)['data']['text']
        nak_defs = [
            ('overall', 'Composite & Frontier', 'LMSYS Chatbot Arena — Overall'),
            ('overall_style_control', 'Composite & Frontier', 'LMSYS Chatbot Arena — Overall (Style-Controlled)'),
            ('hard_6', 'Composite & Frontier', 'LMSYS Chatbot Arena — Hard (Arena-Hard)'),
            ('hard_6_style_control', 'Composite & Frontier', 'LMSYS Chatbot Arena — Hard (Style-Controlled)'),
            ('coding', 'Coding & Software Eng', 'LMSYS Chatbot Arena — Coding'),
            ('coding_style_control', 'Coding & Software Eng', 'LMSYS Chatbot Arena — Coding (Style-Controlled)'),
            ('math', 'Science & Math Reasoning', 'LMSYS Chatbot Arena — Math'),
            ('math_style_control', 'Science & Math Reasoning', 'LMSYS Chatbot Arena — Math (Style-Controlled)'),
            ('if', 'Long-Context & Instruction', 'LMSYS Chatbot Arena — Instruction Following'),
            ('if_style_control', 'Long-Context & Instruction', 'LMSYS Chatbot Arena — Instruction Following (Style-Controlled)'),
            ('creative_writing', 'Long-Context & Instruction', 'LMSYS Chatbot Arena — Creative Writing'),
            ('multiturn', 'Long-Context & Instruction', 'LMSYS Chatbot Arena — Multi-Turn Dialogue'),
            ('long_user', 'Long-Context & Instruction', 'LMSYS Chatbot Arena — Longer Query'),
        ]
        for k, cat, title in nak_defs:
            if k in nak:
                items = [
                    {'name': m, 'score': float(v['rating'] if isinstance(v, dict) else v)}
                    for m, v in nak[k].items()
                    if (isinstance(v, (int, float)) or (isinstance(v, dict) and v.get('rating') is not None))
                ]
                add_bench('LMSYS Chatbot Arena (Sub-Tasks)', cat, title, f"lmsys_sub_{k}", 'quality', True, 'Elo', items, f"LMSYS Chatbot Arena {title} Elo rating.")

    # =========================================================================
    # 7. SWE-BENCH OFFICIAL LEADERBOARDS (Verified Bash-Only, All Systems, Lite, Test, Multimodal)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'swebench_leaderboards.json'), 'r', encoding='utf-8') as f:
        swebench = json.load(f)
    for lb in swebench.get('leaderboards', []):
        lb_name = lb.get('name')
        results = lb.get('results', [])
        if lb_name == 'Verified':
            mini = [r for r in results if any('Mini:' in t for t in r.get('tags', []))]
            add_bench(
                'SWE-bench', 'Coding & Software Eng', 'SWE-bench Verified (Bash-Only Standardized)', 'swebench_verified_bash',
                'quality', True, '% Resolved',
                [{'name': r['name'], 'score': float(r['resolved'])} for r in mini if r.get('resolved') is not None],
                'Standardized Mini-SWE-Agent 2.0 Bash-only scaffold across 500 human-verified GitHub issues.'
            )
            add_bench(
                'SWE-bench', 'Cost & Pricing', 'SWE-bench Verified Total Run Cost ($ USD)', 'swebench_verified_cost',
                'cost', True, 'USD ($)',
                [{'name': r['name'], 'score': float(r['cost'])} for r in mini if r.get('cost') is not None and float(r['cost']) > 0],
                'Total API cost in USD to run all 500 SWE-bench Verified instances (Sol/Opus expected to cost >= Luna/Haiku).'
            )
            add_bench(
                'SWE-bench', 'Latency & Speed', 'SWE-bench Verified Agent Calls per Issue', 'swebench_verified_calls',
                'latency', False, 'Calls/Issue',
                [{'name': r['name'], 'score': float(r['instance_calls'])} for r in mini if r.get('instance_calls') is not None and float(r['instance_calls']) > 0],
                'Average number of agent-environment interaction turns per GitHub issue.'
            )
        if lb_name in ('Verified', 'Lite', 'Test', 'Multimodal'):
            add_bench(
                'SWE-bench', 'Coding & Software Eng', f"SWE-bench {lb_name} (All Submissions)", f"swebench_{lb_name.lower()}_all",
                'quality', True, '% Resolved',
                [{'name': r['name'], 'score': float(r['resolved'])} for r in results if r.get('resolved') is not None],
                f"Full SWE-bench {lb_name} leaderboard (% of real GitHub issues resolved)."
            )

    # =========================================================================
    # 8. AIDER CODING LEADERBOARDS (Polyglot Quality, Latency, Cost, Editing, Refactoring)
    # =========================================================================
    poly_entries = parse_simple_yml_list(os.path.join(CACHE_DIR, 'aider_polyglot.yml'))
    add_bench(
        'Aider Coding', 'Coding & Software Eng', 'Aider Polyglot Coding (Pass@2 %)', 'aider_polyglot_pass2',
        'quality', True, '% Correct',
        [{'name': str(x.get('model')), 'score': float(x['pass_rate_2'])} for x in poly_entries if isinstance(x.get('pass_rate_2'), (int, float))],
        '225 hard Exercism coding problems across C++, Go, Java, JS, Python, and Rust (Pass@2).'
    )
    add_bench(
        'Aider Coding', 'Coding & Software Eng', 'Aider Polyglot Coding (Pass@1 %)', 'aider_polyglot_pass1',
        'quality', True, '% Correct',
        [{'name': str(x.get('model')), 'score': float(x['pass_rate_1'])} for x in poly_entries if isinstance(x.get('pass_rate_1'), (int, float))],
        'First-attempt zero-feedback pass rate on the 225-problem Aider Polyglot suite.'
    )
    add_bench(
        'Aider Coding', 'Latency & Speed', 'Aider Polyglot Latency (Seconds per Case)', 'aider_polyglot_latency',
        'latency', False, 'Seconds/Task',
        [{'name': str(x.get('model')), 'score': float(x['seconds_per_case'])} for x in poly_entries if isinstance(x.get('seconds_per_case'), (int, float)) and float(x['seconds_per_case']) > 0],
        'Average wall-clock seconds per coding task on Aider Polyglot (smaller models expected faster).'
    )
    add_bench(
        'Aider Coding', 'Cost & Pricing', 'Aider Polyglot Total Benchmark Cost ($ USD)', 'aider_polyglot_cost',
        'cost', True, 'USD ($)',
        [{'name': str(x.get('model')), 'score': float(x['total_cost'])} for x in poly_entries if isinstance(x.get('total_cost'), (int, float)) and float(x['total_cost']) > 0],
        'Total dollar cost to complete all 225 Aider Polyglot coding tasks (larger tiers expected to cost >= smaller tiers).'
    )

    edit_entries = parse_simple_yml_list(os.path.join(CACHE_DIR, 'aider_edit.yml'))
    add_bench(
        'Aider Coding', 'Coding & Software Eng', 'Aider Code Editing Leaderboard', 'aider_code_editing',
        'quality', True, '% Correct',
        [{'name': str(x.get('model')), 'score': float(x['pass_rate_2'])} for x in edit_entries if isinstance(x.get('pass_rate_2'), (int, float))],
        '133 Exercism Python code editing benchmark.'
    )

    ref_entries = parse_simple_yml_list(os.path.join(CACHE_DIR, 'aider_refactor.yml'))
    add_bench(
        'Aider Coding', 'Coding & Software Eng', 'Aider Refactoring Leaderboard', 'aider_refactoring',
        'quality', True, '% Correct',
        [{'name': str(x.get('model')), 'score': float(x['pass_rate_1'])} for x in ref_entries if isinstance(x.get('pass_rate_1'), (int, float))],
        '89 large-method Python refactoring tasks.'
    )

    # =========================================================================
    # 9. EVALPLUS CODE GENERATION (HumanEval+, MBPP+, Average)
    # =========================================================================
    with open(os.path.join(CACHE_DIR, 'evalplus_results.json'), 'r', encoding='utf-8') as f:
        evalplus = json.load(f)
    he_items, mb_items, avg_items = [], [], []
    for m_name, obj in evalplus.items():
        p1 = obj.get('pass@1') or {}
        he = p1.get('humaneval+')
        mb = p1.get('mbpp+')
        if he is not None:
            he_items.append({'name': m_name, 'score': float(he)})
        if mb is not None:
            mb_items.append({'name': m_name, 'score': float(mb)})
        if he is not None and mb is not None:
            avg_items.append({'name': m_name, 'score': (float(he) + float(mb)) / 2.0})
    add_bench('EvalPlus', 'Coding & Software Eng', 'EvalPlus HumanEval+ (80x Tests)', 'evalplus_humaneval_plus', 'quality', True, 'Pass@1 %', he_items, 'HumanEval rigorized with 80x additional automated edge-case unit tests.')
    add_bench('EvalPlus', 'Coding & Software Eng', 'EvalPlus MBPP+ (35x Tests)', 'evalplus_mbpp_plus', 'quality', True, 'Pass@1 %', mb_items, 'Mostly Basic Python Problems rigorized with 35x additional edge-case tests.')
    add_bench('EvalPlus', 'Coding & Software Eng', 'EvalPlus Combined Average', 'evalplus_average', 'quality', True, 'Pass@1 %', avg_items, 'Mean of HumanEval+ and MBPP+ Pass@1 scores.')

    print(f"Total benchmark rankings evaluated: {len(benchmarks)}")
    payload = {
        'generatedAt': '2026-11-01',
        'totalBenchmarks': len(benchmarks),
        'popularBenchmarksCount': sum(1 for b in benchmarks if b.get('is_popular')),
        'popularBenchmarkIds': sorted(list(POPULAR_BENCHMARK_IDS)),
        'benchmarks': benchmarks
    }
    out_path = os.path.join(BASE_DIR, 'contradiction_benchmarks_results.json')
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2)

    slim_benchmarks = [
        {
            'id': b['id'],
            'is_popular': b.get('is_popular', False),
            'suite': b['suite'],
            'category': b['category'],
            'name': b['name'],
            'metric_type': b['metric_type'],
            'unit': b['unit'],
            'description': b.get('description', ''),
            'canonical_top25': b['canonical_top25'],
        }
        for b in benchmarks
    ]
    slim_payload = {
        'generatedAt': '2026-11-01',
        'totalBenchmarks': len(slim_benchmarks),
        'popularBenchmarksCount': sum(1 for b in slim_benchmarks if b.get('is_popular')),
        'popularBenchmarkIds': sorted(list(POPULAR_BENCHMARK_IDS)),
        'benchmarks': slim_benchmarks
    }
    data_js_content = 'window.CONTRADICTION_BENCHMARKS_DATA = ' + json.dumps(slim_payload, separators=(',', ':')) + ';\n'
    data_js_path = os.path.join(BASE_DIR, 'data.js')
    with open(data_js_path, 'w', encoding='utf-8') as f:
        f.write(data_js_content)

    # Also build a single self-contained shareable_table.html
    idx_path = os.path.join(BASE_DIR, 'index.html')
    css_path = os.path.join(BASE_DIR, 'styles.css')
    app_path = os.path.join(BASE_DIR, 'app.js')
    if os.path.exists(idx_path) and os.path.exists(css_path) and os.path.exists(app_path):
        with open(idx_path, 'r', encoding='utf-8') as f: html_t = f.read()
        with open(css_path, 'r', encoding='utf-8') as f: css_t = f.read()
        with open(app_path, 'r', encoding='utf-8') as f: app_t = f.read()
        standalone = html_t.replace('<link rel="stylesheet" href="styles.css" />', f'<style>\n{css_t}\n</style>')
        standalone = standalone.replace('<script src="data.js"></script>\n  <script src="app.js"></script>', f'<script>\n{data_js_content}\n{app_t}\n</script>')
        standalone_path = os.path.join(BASE_DIR, 'shareable_table.html')
        with open(standalone_path, 'w', encoding='utf-8') as f:
            f.write(standalone)
        print(f"Saved results to {out_path}, {data_js_path}, and single-file {standalone_path}")

    # Generate clean Markdown tables for README.md and Artifact
    def clean_label(s):
        s = re.sub(r'^.*?\+\s*', '', s)
        s = re.sub(r'^ollama/', '', s)
        s = re.sub(r'\s*\((?:Max,\s*Default Fallback|Adaptive Reasoning|Default Thinking|bf16|FP8|high|32k thinking(?: tokens)?|202\d-\d\d-\d\d)\)', '', s, flags=re.I)
        return s.strip()

    def fmt_score(val, unit, mtype):
        u = (unit or '').lower()
        if mtype == 'cost' or ('$' in u):
            return f"${val:.3f}" if val < 1 else f"${val:.2f}"
        if 'tokens/sec' in u or 'tok/s' in u:
            return f"{val:.1f} tok/s"
        if mtype == 'latency' and 'sec' in u:
            return f"{val:.1f}s"
        return f"{val:.1f}" if val > 10 else f"{val:.3f}".rstrip('0').rstrip('.')

    def fmt_chip(p, b):
        ma, mb = clean_label(p['model_a']), clean_label(p['model_b'])
        mtype = b['metric_type']
        sa = fmt_score(p['score_a'], b['unit'], mtype)
        sb = fmt_score(p['score_b'], b['unit'], mtype)
        if mtype == 'latency':
            return f"**{ma}** (#{p['rank_a']}, {sa}) faster than **{mb}** (#{p['rank_b']}, {sb})"
        if mtype == 'cost':
            return f"**{mb}** ({sb}) cost more than **{ma}** ({sa})"
        return f"**{mb}** (#{p['rank_b']}, {sb}) ahead of **{ma}** (#{p['rank_a']}, {sa})"

    def make_table(benches):
        benches = sorted(
            benches,
            key=lambda b: (
                b['canonical_top25']['contradictions_count'],
                -b['canonical_top25']['comparable_pairs_count'],
                b['name']
            )
        )
        lines = [
            '| Benchmark | Contradictions | Example Contradictions in the Benchmark |',
            '| :--- | :-: | :--- |'
        ]
        for b in benches:
            c = b['canonical_top25']
            if c['contradictions']:
                ex = '; '.join(fmt_chip(p, b) for p in c['contradictions'][:3])
                if len(c['contradictions']) > 3:
                    ex += f" *(+{len(c['contradictions'])-3} more)*"
            else:
                ex = "None"
            lines.append(f"| **{b['name']}** | **{c['contradictions_count']}** | {ex} |")
        return '\n'.join(lines)

    pop = [b for b in benchmarks if b.get('is_popular')]
    all_b = [b for b in benchmarks if b['canonical_top25']['comparable_pairs_count'] > 0]
    readme_md = (
        "# AI Contradictions Benchmark\n\n"
        "- **Live Table (Popular)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks)\n"
        "- **Live Table (ALL)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL)\n"
        "- **Repository**: [https://github.com/sagarvare/ai-benchmark-contradiction-index](https://github.com/sagarvare/ai-benchmark-contradiction-index)\n\n"
        "Measuring the count of contradicted intra-family model pairs within the **Top 100 models** on each benchmark (evaluating $\\binom{100}{2} = 4,950$ candidate pair comparisons per benchmark).\n\n"
        "### Intra-Family Consistency Rules\n\n"
        "1. **Same-generation tier rule:** Larger tiers should rank ahead of smaller tiers within the same version (e.g., GPT-4o > GPT-4o-mini; Claude 3.5 Sonnet > Claude 3.5 Haiku).\n"
        "2. **Cross-generation same-tier rule:** Newer versions should rank ahead of older versions within the same tier (e.g., Claude 3.5 Sonnet > Claude 3 Sonnet; GPT-4o > GPT-4-turbo).\n\n"
        "All popular benchmarks strictly require **>= 100 model submissions** on their public leaderboards.\n\n"
        "---\n\n"
        "## Popular\n\n"
        f"{make_table(pop)}\n\n"
        "---\n\n"
        "## ALL\n\n"
        "<details>\n<summary><strong>Expand ALL benchmarks</strong></summary>\n\n"
        f"{make_table(all_b)}\n\n"
        "</details>\n"
    )
    readme_path = os.path.join(BASE_DIR, 'README.md')
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_md)
    print(f"Saved clean Markdown report to {readme_path}")

if __name__ == '__main__':
    build_all_benchmarks()
