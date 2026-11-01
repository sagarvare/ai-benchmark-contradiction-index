# AI Benchmark Inverted Pairs

- **Live Table (Popular Benchmarks)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks)
- **Live Table (All 144 Benchmarks)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL)
- **Repository**: [https://github.com/sagarvare/ai-benchmark-contradiction-index](https://github.com/sagarvare/ai-benchmark-contradiction-index)

This table measures the **count of inverted model pairs** within the **Top 50 ranked models** on each AI benchmark. A pair of models is counted as inverted when their relative ranking contradicts the expected ordering within the same model family under two rules:

1. **Same-generation tier rule:** Within the same model family and version, a larger tier is expected to rank ahead of a smaller tier (for example, **GPT 6.1 Sol** ahead of **GPT 6.1 Terra** ahead of **GPT 6.1 Luna**, or **Claude Opus 5.5** ahead of **Claude Sonnet 5.5** ahead of **Claude Haiku 5.5**). For latency benchmarks, this order is reversed so smaller models are expected to be faster. For cost benchmarks, larger models are expected to cost more.
2. **Cross-generation same-tier rule:** Within the same model family and size tier, a newer version is expected to rank ahead of an older version (for example, **GPT 6.1 Sol** ahead of **GPT 6.0 Sol**, or **Claude Opus 5.5** ahead of **Claude Opus 4.7**). Crossed pairs such as **GPT 6.1 Sol** and **GPT 6.0 Luna** are not compared.

---

## Popular Benchmarks (44 Benchmarks)

| # | Benchmark | Suite | Metric | Inverted Pairs | Comparable Pairs | Inverted Pairs in Top 50 |
| :-: | :--- | :--- | :--- | :-: | :-: | :--- |
| 1 | **LiveBench v1 — Coding** | LiveBench v1 (2026) | Quality | **14** | 55 | **claude-sonnet-5-5-max-effort** (#1, 91.4) ahead of **claude-opus-5-5-max-effort** (#2, 89.3); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6-sol-max** (#12, 81.8) *(+12 more)* |
| 2 | **SWE-bench Verified (All Submissions)** | SWE-bench | Quality | **11** | 36 | **Claude 4 Sonnet** (#4, 76.8) ahead of **Claude 4 Opus** (#16, 73.2); **Claude 4.5 Opus** (#1, 79.2) ahead of **Claude 4.6 Opus** (#12, 75.6) *(+9 more)* |
| 3 | **Aider Code Editing Leaderboard** | Aider Coding | Quality | **10** | 75 | **gpt-4-0613** (#17, 67.7) ahead of **gpt-4-0125-preview** (#20, 66.2); **Qwen2.5-Coder-14B-Instruct** (#19, 69.2) ahead of **openrouter/qwen/qwen-2.5-coder-32b-instruct** (#32, 65.4) *(+8 more)* |
| 4 | **Arena.ai Text Overall (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **8** | 14 | **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5.5-high** (#4, 1504.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-4-7-high** (#5, 1501.0) *(+6 more)* |
| 5 | **Arena.ai Vision Multimodal (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **8** | 13 | **claude-fable-5-high** (#1, 1309.0) ahead of **claude-fable-5.1-max** (#13, 1288.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-4-7-high** (#4, 1298.0) *(+6 more)* |
| 6 | **Tau2-Bench Tool-Use Agentic** | Artificial Analysis v5 | Quality | **7** | 30 | **Qwen3.5 4B (Reasoning)** (#11, 0.921) ahead of **Qwen3.5 9B (Reasoning)** (#19, 0.868); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 9B (Non-reasoning)** (#24, 0.851) *(+5 more)* |
| 7 | **AA Time to First Answer Token (Seconds)** | Artificial Analysis v5 | Latency | **7** | 27 | **Ministral 3 8B** (#8, 0.8s) faster than **Ministral 3 3B** (#9, 0.9s); **Nemotron 3 Ultra** (#33, 7.5s) faster than **Nemotron 3 Nano Omni 30B A3B** (#36, 9.6s) *(+5 more)* |
| 8 | **LiveBench v1 Global Average** | LiveBench v1 (2026) | Quality | **6** | 57 | **gpt-5.6-sol-max** (#9, 81.1) ahead of **gpt-6-sol-max** (#13, 79.2); **gemini-3.7-flash-high** (#15, 78.8) ahead of **gemini-3.8-flash-high** (#32, 75.8) *(+4 more)* |
| 9 | **Aider Polyglot Latency (Seconds per Case)** | Aider Coding | Latency | **6** | 16 | **gpt-4o-2024-11-20** (#4, 12.1s) faster than **gpt-4o-mini-2024-07-18** (#8, 17.3s); **claude-3-5-sonnet-20241022** (#13, 21.4s) faster than **claude-3-5-haiku-20241022** (#17, 31.8s) *(+4 more)* |
| 10 | **FrontierCode 2.0** | Artificial Analysis v5 | Quality | **5** | 28 | **GPT-6.1 Terra (Max)** (#3, 0.423) ahead of **GPT-6.1 Sol (Max)** (#5, 0.406); **Inkling Small** (#34, 0.048) ahead of **Inkling (Xhigh)** (#35, 0.039) *(+3 more)* |
| 11 | **AA Long-Context Reasoning (LCR)** | Artificial Analysis v5 | Quality | **5** | 20 | **GPT-6 Luna (Max)** (#7, 0.833) ahead of **GPT-6 Astra (Max)** (#25, 0.807); **Muse Glimmer** (#8, 0.833) ahead of **Muse Wonder (Max)** (#26, 0.807) *(+3 more)* |
| 12 | **LiveBench v1 — Mathematics** | LiveBench v1 (2026) | Quality | **4** | 59 | **gemini-3.7-flash-high** (#19, 93.5) ahead of **gemini-3.8-flash-high** (#25, 91.6); **claude-opus-4-5-20251101-thinking-64k-high-effort** (#31, 90.4) ahead of **claude-opus-4-6-thinking-auto-high-effort** (#35, 89.3) *(+2 more)* |
| 13 | **Aider Polyglot Coding (Pass@2 %)** | Aider Coding | Quality | **4** | 35 | **claude-3-7-sonnet-20250219** (#11, 64.9) ahead of **claude-sonnet-4-20250514** (#14, 61.3); **gpt-4.1** (#23, 52.4) ahead of **gpt-4.5-preview** (#27, 44.9) *(+2 more)* |
| 14 | **MLCR-AA Medical Long-Context** | Artificial Analysis v5 | Quality | **4** | 25 | **Claude Sonnet 5.5** (#1, 0.417) ahead of **Claude Opus 5.5** (#9, 0.278); **Claude Haiku 5.5 (Max)** (#5, 0.35) ahead of **Claude Opus 5.5** (#9, 0.278) *(+2 more)* |
| 15 | **HLE-Diamond (Humanity's Last Exam)** | Artificial Analysis v5 | Quality | **3** | 28 | **DeepSeek V4 Flash Vision (Max)** (#22, 0.211) ahead of **DeepSeek V4 Pro 0813 (Max)** (#24, 0.195); **GLM-5.3-Flash** (#25, 0.182) ahead of **GLM-5.3 (Max)** (#26, 0.179) *(+1 more)* |
| 16 | **AutomationBench-AA SaaS Workflows** | Artificial Analysis v5 | Quality | **3** | 23 | **Claude Sonnet 5.5** (#5, 0.718) ahead of **Claude Opus 5.5** (#7, 0.695); **MiMo-V2.6-Flash** (#14, 0.64) ahead of **MiMo-V2.6-Pro** (#21, 0.586) *(+1 more)* |
| 17 | **LiveBench 2.0 — Design** | LiveBench 2.0 (Oct 2026) | Quality | **3** | 8 | **gpt-6-luna** (#6, 82.5) ahead of **gpt-6-astra** (#9, 82.0); **gpt-6.1-terra** (#7, 82.3) ahead of **gpt-6.1-sol** (#8, 82.1) *(+1 more)* |
| 18 | **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **3** | 6 | **GPT-6 Astra (Max)** (#8, 469.8s) faster than **GPT-6 Luna (Max)** (#12, 585.3s); **GPT-6.1 Sol (Max)** (#10, 543.6s) faster than **GPT-6.1 Terra (Max)** (#14, 694.3s) *(+1 more)* |
| 19 | **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **3** | 6 | **GPT-6.1 Sol (Max)** (#9, 24.7s) faster than **GPT-6.1 Terra (Max)** (#23, 86.4s); **GPT-6 Astra (Max)** (#10, 24.7s) faster than **GPT-6 Luna (Max)** (#16, 39.1s) *(+1 more)* |
| 20 | **AA-Briefcase v1.1 Knowledge Work** | Artificial Analysis v5 | Quality | **2** | 26 | **Claude Sonnet 5.5** (#1, 1813.6) ahead of **Claude Opus 5.5** (#2, 1800.5); **DeepSeek V4 Flash Vision (Max)** (#24, 1420.2) ahead of **DeepSeek V4 Pro 0813 (Max)** (#32, 1254.4) |
| 21 | **SciCode Scientific Coding** | Artificial Analysis v5 | Quality | **2** | 24 | **GPT-6.1 Terra (Max)** (#18, 0.551) ahead of **GPT-6.1 Sol (Max)** (#21, 0.542); **Inkling Small** (#32, 0.496) ahead of **Inkling (Xhigh)** (#44, 0.47) |
| 22 | **GDPval-AA Professional Work Elo** | Artificial Analysis v5 | Quality | **2** | 23 | **DeepSeek V4 Flash Vision (Max)** (#24, 1554.0) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 1457.4); **Inkling Small** (#42, 1132.6) ahead of **Inkling (Xhigh)** (#50, 1080.2) |
| 23 | **LiveBench 2.0 — Reasoning** | LiveBench 2.0 (Oct 2026) | Quality | **2** | 8 | **grok-4.6** (#7, 91.2) ahead of **grok-4.7** (#20, 82.7); **gpt-5.6-terra** (#10, 90.6) ahead of **gpt-6.1-terra** (#15, 88.7) |
| 24 | **LiveBench 2.0 — Browser** | LiveBench 2.0 (Oct 2026) | Quality | **2** | 8 | **claude-sonnet-5.5** (#5, 89.3) ahead of **claude-opus-5.5** (#6, 88.4); **grok-4.6** (#18, 49.4) ahead of **grok-4.7** (#20, 49.3) |
| 25 | **OpenAI HealthBench Medical Reasoning** | Artificial Analysis v5 | Quality | **2** | 4 | **Claude Sonnet 5.5** (#1, 0.621) ahead of **Claude Opus 5.5** (#6, 0.57); **Claude Haiku 5.5 (Max)** (#3, 0.585) ahead of **Claude Opus 5.5** (#6, 0.57) |
| 26 | **AA v4 GPQA Diamond (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **1** | 48 | **Grok 4.20 0309 v2 (Reasoning)** (#22, 0.911) ahead of **Grok 4.3** (#30, 0.901) |
| 27 | **SWE-bench Verified (Bash-Only Standardized)** | SWE-bench | Quality | **1** | 33 | **Gemini 3 Flash** (#2, 75.8) ahead of **Gemini 3 Pro Preview** (#5, 74.2) |
| 28 | **AA-Omniscience v1.1 Net Score** | Artificial Analysis v5 | Quality | **1** | 31 | **Muse Spark Open (Xhigh)** (#12, 25.8) ahead of **Muse Wonder (Max)** (#13, 25.1) |
| 29 | **CritPt v2 Agentic Hard** | Artificial Analysis v5 | Quality | **1** | 30 | **Inkling Small** (#30, 0.185) ahead of **Inkling (Xhigh)** (#31, 0.18) |
| 30 | **AA Intelligence Index v5.0** | Artificial Analysis v5 | Quality | **1** | 27 | **Inkling Small** (#33, 12.9) ahead of **Inkling (Xhigh)** (#34, 12.5) |
| 31 | **CritPt Physics Reasoning** | Artificial Analysis v5 | Quality | **1** | 24 | **Inkling Small** (#44, 0.083) ahead of **Inkling (Xhigh)** (#48, 0.054) |
| 32 | **Terminal-Bench 4.0** | Artificial Analysis v5 | Quality | **1** | 24 | **Claude Sonnet 5.5** (#3, 0.636) ahead of **Claude Opus 5.5** (#4, 0.596) |
| 33 | **EvalPlus Combined Average** | EvalPlus | Quality | **1** | 13 | **claude-3-haiku (Mar 2024)** (#23, 68.8) ahead of **claude-3-sonnet (Mar 2024)** (#32, 66.7) |
| 34 | **LiveBench 2.0 — Coding** | LiveBench 2.0 (Oct 2026) | Quality | **1** | 8 | **grok-4.6** (#12, 89.1) ahead of **grok-4.7** (#18, 84.5) |
| 35 | **Arena.ai Coding (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **1** | 7 | **mimo-v2.6-flash** (#13, 1636.0) ahead of **mimo-v2.6-pro** (#16, 1630.0) |
| 36 | **AA Intelligence Index Time per Task (Seconds)** | Artificial Analysis v5 | Latency | **1** | 6 | **Claude Opus 5.5** (#19, 1140.8s) faster than **Claude Sonnet 5.5** (#21, 1298.5s) |
| 37 | **FrontierCode 2.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($1.29) cost more than **GPT-6.1 Sol (Max)** ($1.13) |
| 38 | **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($0.043) cost more than **GPT-6.1 Sol (Max)** ($0.018) |
| 39 | **LiveBench 2.0 Cost — Coding ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **1** | 6 | **gpt-6.1-terra** ($24.97) cost more than **gpt-6.1-sol** ($13.98) |
| 40 | **LMSYS Arena Hard Prompts** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 36 | None (all 36 pairs follow expected order) |
| 41 | **IFBench Instruction Following** | Artificial Analysis v5 | Quality | **0** | 18 | None (all 18 pairs follow expected order) |
| 42 | **AA API Blended Price (3:1 In:Out $/1M)** | Artificial Analysis v5 | Cost | **0** | 13 | None (all 13 pairs follow expected order) |
| 43 | **LiveBench 2.0 Overall Score** | LiveBench 2.0 (Oct 2026) | Quality | **0** | 8 | None (all 8 pairs follow expected order) |
| 44 | **AA Intelligence Index Total Run Cost ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |

---

## All Benchmarks (144 Benchmarks)

<details>
<summary><strong>Expand all 144 benchmarks</strong></summary>

| # | Benchmark | Suite | Metric | Inverted Pairs | Comparable Pairs | Inverted Pairs in Top 50 |
| :-: | :--- | :--- | :--- | :-: | :-: | :--- |
| 1 | **LiveBench v1 — Coding** | LiveBench v1 (2026) | Quality | **14** | 55 | **claude-sonnet-5-5-max-effort** (#1, 91.4) ahead of **claude-opus-5-5-max-effort** (#2, 89.3); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6-sol-max** (#12, 81.8) *(+12 more)* |
| 2 | **LiveBench v1 — IF** | LiveBench v1 (2026) | Quality | **13** | 51 | **qwen3.8-flash-next** (#5, 77.1) ahead of **qwen3.8-max** (#13, 74.1); **claude-fable-5-max-effort** (#6, 75.8) ahead of **claude-fable-5-1-max-effort** (#18, 73.0) *(+11 more)* |
| 3 | **LiveBench v1 — Language** | LiveBench v1 (2026) | Quality | **12** | 55 | **claude-fable-5-max-effort** (#1, 90.7) ahead of **claude-fable-5-1-max-effort** (#3, 89.5); **claude-opus-5-max-effort** (#5, 88.7) ahead of **claude-opus-5-5-max-effort** (#9, 86.3) *(+10 more)* |
| 4 | **LiveBench v1 — Data Analysis** | LiveBench v1 (2026) | Quality | **12** | 49 | **claude-fable-5-max-effort** (#6, 80.5) ahead of **claude-fable-5-1-max-effort** (#8, 80.3); **deepseek-v4-flash-vision-exp** (#12, 79.5) ahead of **deepseek-v4-pro-0813** (#16, 79.2) *(+10 more)* |
| 5 | **AA-Omniscience Non-Hallucination Rate** | Artificial Analysis v5 | Quality | **12** | 23 | **Gemini 4 Argon** (#1, 0.957) ahead of **Gemini 4 Carbon** (#2, 0.886); **Granite 4.2 3B** (#15, 0.697) ahead of **Granite 4.2 8B** (#18, 0.678) *(+10 more)* |
| 6 | **SWE-bench Verified (All Submissions)** | SWE-bench | Quality | **11** | 36 | **Claude 4 Sonnet** (#4, 76.8) ahead of **Claude 4 Opus** (#16, 73.2); **Claude 4.5 Opus** (#1, 79.2) ahead of **Claude 4.6 Opus** (#12, 75.6) *(+9 more)* |
| 7 | **Aider Code Editing Leaderboard** | Aider Coding | Quality | **10** | 75 | **gpt-4-0613** (#17, 67.7) ahead of **gpt-4-0125-preview** (#20, 66.2); **Qwen2.5-Coder-14B-Instruct** (#19, 69.2) ahead of **openrouter/qwen/qwen-2.5-coder-32b-instruct** (#32, 65.4) *(+8 more)* |
| 8 | **Arena.ai Search & Grounding** | LMSYS Arena.ai (2026) | Quality | **10** | 55 | **claude-opus-4-6-search** (#2, 1253.0) ahead of **claude-opus-4-7** (#4, 1233.0); **claude-opus-4-6-search** (#2, 1253.0) ahead of **claude-opus-4-8** (#12, 1204.0) *(+8 more)* |
| 9 | **Arena.ai Text Overall (50-Model Snapshot)** | LMSYS Arena.ai (2026) | Quality | **9** | 43 | **claude-opus-4-6-thinking** (#2, 1504.0) ahead of **claude-opus-4-7-thinking** (#3, 1502.0); **claude-opus-4-6-thinking** (#2, 1504.0) ahead of **claude-opus-4-8-thinking** (#7, 1483.0) *(+7 more)* |
| 10 | **AA End-to-End Response Time (Seconds)** | Artificial Analysis v5 | Latency | **9** | 19 | **Llama 4 Maverick** (#5, 2.9s) faster than **Llama 4 Scout** (#10, 3.9s); **Phi-4** (#16, 5.9s) faster than **Phi-4 Mini** (#33, 11.9s) *(+7 more)* |
| 11 | **SWE-bench Verified Agent Calls per Issue** | SWE-bench | Latency | **9** | 10 | **GPT 5 (medium)** (#1, 13.2) faster than **GPT 5 mini (medium)** (#2, 14.5); **GPT 5 (medium)** (#1, 13.2) faster than **GPT 5 nano (medium)** (#19, 39.8) *(+7 more)* |
| 12 | **LiveBench v1 — Reasoning** | LiveBench v1 (2026) | Quality | **8** | 60 | **gpt-5.6-sol-max** (#5, 91.7) ahead of **gpt-6-sol-max** (#21, 88.7); **muse-spark-1.2-xhigh** (#13, 90.0) ahead of **muse-spark-1.3-xhigh** (#16, 89.7) *(+6 more)* |
| 13 | **LiveBench v1 — Agentic Coding** | LiveBench v1 (2026) | Quality | **8** | 46 | **deepseek-v4-flash-vision-exp** (#5, 65.1) ahead of **deepseek-v4-pro-0813** (#29, 54.9); **claude-sonnet-5-xhigh-effort** (#17, 59.4) ahead of **claude-sonnet-5-5-max-effort** (#27, 56.3) *(+6 more)* |
| 14 | **AA v4 Tau-Bench Banking (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **8** | 45 | **GPT-5.4 (xhigh)** (#9, 0.396) ahead of **GPT-5.5 (xhigh)** (#12, 0.39); **Claude Opus 4.7 (Adaptive Reasoning, Max Effort)** (#17, 0.346) ahead of **Claude Opus 4.8 (Adaptive Reasoning, Max Effort)** (#20, 0.342) *(+6 more)* |
| 15 | **Arena.ai Document Comprehension** | LMSYS Arena.ai (2026) | Quality | **8** | 39 | **claude-opus-4-6-high** (#3, 1507.0) ahead of **claude-opus-4-7-high** (#5, 1495.0); **claude-opus-4-6-high** (#3, 1507.0) ahead of **claude-opus-4-8-high** (#9, 1475.0) *(+6 more)* |
| 16 | **Arena.ai Vision Multimodal (30-Model Table)** | LMSYS Arena.ai (2026) | Quality | **8** | 24 | **claude-opus-4-7-thinking** (#2, 1304.0) ahead of **claude-opus-5-high** (#5, 1299.0); **claude-opus-4-7-thinking** (#2, 1304.0) ahead of **claude-opus-4-8-thinking** (#8, 1286.0) *(+6 more)* |
| 17 | **Arena.ai Text Overall (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **8** | 14 | **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5.5-high** (#4, 1504.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-4-7-high** (#5, 1501.0) *(+6 more)* |
| 18 | **Arena.ai Vision Multimodal (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **8** | 13 | **claude-fable-5-high** (#1, 1309.0) ahead of **claude-fable-5.1-max** (#13, 1288.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-4-7-high** (#4, 1298.0) *(+6 more)* |
| 19 | **AA v4 SciCode (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **7** | 50 | **Muse Spark 1.1 (xhigh)** (#4, 0.582) ahead of **Muse Spark 1.2 (xhigh)** (#7, 0.564); **GPT-5.4 (xhigh)** (#6, 0.566) ahead of **GPT-5.5 (xhigh)** (#9, 0.561) *(+5 more)* |
| 20 | **Tau2-Bench Tool-Use Agentic** | Artificial Analysis v5 | Quality | **7** | 30 | **Qwen3.5 4B (Reasoning)** (#11, 0.921) ahead of **Qwen3.5 9B (Reasoning)** (#19, 0.868); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 9B (Non-reasoning)** (#24, 0.851) *(+5 more)* |
| 21 | **AA Time to First Answer Token (Seconds)** | Artificial Analysis v5 | Latency | **7** | 27 | **Ministral 3 8B** (#8, 0.8s) faster than **Ministral 3 3B** (#9, 0.9s); **Nemotron 3 Ultra** (#33, 7.5s) faster than **Nemotron 3 Nano Omni 30B A3B** (#36, 9.6s) *(+5 more)* |
| 22 | **LiveBench v1 Global Average** | LiveBench v1 (2026) | Quality | **6** | 57 | **gpt-5.6-sol-max** (#9, 81.1) ahead of **gpt-6-sol-max** (#13, 79.2); **gemini-3.7-flash-high** (#15, 78.8) ahead of **gemini-3.8-flash-high** (#32, 75.8) *(+4 more)* |
| 23 | **Arena.ai Coding (108-Model Full Table)** | LMSYS Arena.ai (2026) | Quality | **6** | 56 | **deepseek-v4-flash-high** (#6, 1586.0) ahead of **deepseek-v4-pro-high-preview** (#29, 1465.0); **gpt-5.6-luna-xhigh (codex-harness)** (#15, 1524.0) ahead of **gpt-5.6-terra-xhigh (codex-harness)** (#17, 1521.0) *(+4 more)* |
| 24 | **AA Output Speed (Median Tokens/Sec)** | Artificial Analysis v5 | Latency | **6** | 18 | **Nemotron 3 Ultra** (#9, 351.8 tok/s) faster than **Nemotron 3 Nano** (#14, 293.5 tok/s); **Nemotron 3 Ultra** (#9, 351.8 tok/s) faster than **Nemotron 3 Nano Omni 30B A3B** (#21, 230.5 tok/s) *(+4 more)* |
| 25 | **Aider Polyglot Latency (Seconds per Case)** | Aider Coding | Latency | **6** | 16 | **gpt-4o-2024-11-20** (#4, 12.1s) faster than **gpt-4o-mini-2024-07-18** (#8, 17.3s); **claude-3-5-sonnet-20241022** (#13, 21.4s) faster than **claude-3-5-haiku-20241022** (#17, 31.8s) *(+4 more)* |
| 26 | **AA Median Reasoning Time (Seconds)** | Artificial Analysis v5 | Latency | **6** | 14 | **gpt-oss-120b** (#7, 9.7s) faster than **gpt-oss-20b** (#22, 14.0s); **Muse Wonder (Max)** (#21, 14.0s) faster than **Muse Spark Open (Xhigh)** (#24, 14.4s) *(+4 more)* |
| 27 | **AA v4 Omniscience (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **5** | 54 | **Muse Spark 1.1 (xhigh)** (#6, 28.1) ahead of **Muse Spark 1.2 (xhigh)** (#8, 27.2); **Claude Opus 4.5 (Reasoning)** (#20, 14.0) ahead of **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#21, 13.7) *(+3 more)* |
| 28 | **AA v4 Humanity's Last Exam (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **5** | 41 | **Muse Spark 1.1 (xhigh)** (#8, 0.462) ahead of **Muse Spark 1.2 (xhigh)** (#10, 0.455); **Gemini 3.5 Flash** (#15, 0.427) ahead of **Gemini 3.6 Flash** (#23, 0.408) *(+3 more)* |
| 29 | **SWE-bench Lite (All Submissions)** | SWE-bench | Quality | **5** | 36 | **GPT 4 (0806)** (#22, 39.7) ahead of **GPT 4o** (#25, 38.0); **GPT 4 (0806)** (#28, 39.7) ahead of **GPT 4o** (#38, 34.0) *(+3 more)* |
| 30 | **FrontierCode 2.0** | Artificial Analysis v5 | Quality | **5** | 28 | **GPT-6.1 Terra (Max)** (#3, 0.423) ahead of **GPT-6.1 Sol (Max)** (#5, 0.406); **Inkling Small** (#34, 0.048) ahead of **Inkling (Xhigh)** (#35, 0.039) *(+3 more)* |
| 31 | **AA v4 Latency TTFT (Seconds, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Latency | **5** | 21 | **Phi-4 Multimodal Instruct** (#20, 0.8s) faster than **Phi-4 Mini Instruct** (#24, 0.9s); **GPT-4o (Nov '24)** (#22, 0.9s) faster than **GPT-4o mini** (#29, 0.9s) *(+3 more)* |
| 32 | **AA Long-Context Reasoning (LCR)** | Artificial Analysis v5 | Quality | **5** | 20 | **GPT-6 Luna (Max)** (#7, 0.833) ahead of **GPT-6 Astra (Max)** (#25, 0.807); **Muse Glimmer** (#8, 0.833) ahead of **Muse Wonder (Max)** (#26, 0.807) *(+3 more)* |
| 33 | **AA Time to First Token (TTFT Seconds)** | Artificial Analysis v5 | Latency | **5** | 17 | **Inkling (xhigh)** (#8, 0.5s) faster than **Inkling Small** (#14, 0.6s); **Qwen3.5 9B** (#16, 0.7s) faster than **Qwen3.5 4B** (#31, 0.9s) *(+3 more)* |
| 34 | **LiveBench v1 — Mathematics** | LiveBench v1 (2026) | Quality | **4** | 59 | **gemini-3.7-flash-high** (#19, 93.5) ahead of **gemini-3.8-flash-high** (#25, 91.6); **claude-opus-4-5-20251101-thinking-64k-high-effort** (#31, 90.4) ahead of **claude-opus-4-6-thinking-auto-high-effort** (#35, 89.3) *(+2 more)* |
| 35 | **Aider Polyglot Coding (Pass@1 %)** | Aider Coding | Quality | **4** | 38 | **claude-3-7-sonnet-20250219** (#10, 29.3) ahead of **claude-sonnet-4-20250514** (#15, 25.8); **o3-mini** (#22, 21.0) ahead of **o4-mini** (#27, 19.6) *(+2 more)* |
| 36 | **Aider Polyglot Coding (Pass@2 %)** | Aider Coding | Quality | **4** | 35 | **claude-3-7-sonnet-20250219** (#11, 64.9) ahead of **claude-sonnet-4-20250514** (#14, 61.3); **gpt-4.1** (#23, 52.4) ahead of **gpt-4.5-preview** (#27, 44.9) *(+2 more)* |
| 37 | **MLCR-AA Medical Long-Context** | Artificial Analysis v5 | Quality | **4** | 25 | **Claude Sonnet 5.5** (#1, 0.417) ahead of **Claude Opus 5.5** (#9, 0.278); **Claude Haiku 5.5 (Max)** (#5, 0.35) ahead of **Claude Opus 5.5** (#9, 0.278) *(+2 more)* |
| 38 | **CritPt v2 Hard — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **4** | 6 | **GPT-6 Astra (Max)** (#3, 231.3s) faster than **GPT-6 Luna (Max)** (#10, 408.8s); **GPT-6.1 Sol (Max)** (#4, 257.7s) faster than **GPT-6.1 Terra (Max)** (#9, 391.1s) *(+2 more)* |
| 39 | **AA v4 CritPt Physics (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **3** | 50 | **Gemini 3.5 Flash** (#24, 0.131) ahead of **Gemini 3.6 Flash** (#30, 0.106); **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#25, 0.126) ahead of **Claude Opus 4.7 (Adaptive Reasoning, Max Effort)** (#26, 0.12) *(+1 more)* |
| 40 | **AA v4 Intelligence Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **3** | 47 | **Gemini 3.5 Flash** (#21, 52.0) ahead of **Gemini 3.6 Flash** (#23, 51.6); **Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort)** (#24, 48.4) ahead of **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#32, 44.9) *(+1 more)* |
| 41 | **LMSYS Arena Math** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **3** | 41 | **qwen3-32b** (#6, 1387.3) ahead of **qwen3-235b-a22b** (#9, 1372.4); **gemini-2.0-flash-thinking-exp-01-21** (#13, 1357.3) ahead of **gemini-2.0-pro-exp-02-05** (#18, 1348.7) *(+1 more)* |
| 42 | **AA v4 Coding Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **3** | 37 | **Gemini 3.5 Flash** (#19, 70.1) ahead of **Gemini 3.6 Flash** (#20, 69.2); **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#21, 69.1) ahead of **DeepSeek V4 Pro 0813 (Reasoning, Max Effort)** (#22, 68.8) *(+1 more)* |
| 43 | **AA v4 Terminal-Bench (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **3** | 36 | **Gemini 3.5 Flash** (#19, 0.786) ahead of **Gemini 3.6 Flash** (#23, 0.775); **Qwen3.6 Plus** (#41, 0.614) ahead of **Qwen3.7 Plus** (#42, 0.611) *(+1 more)* |
| 44 | **HLE-Diamond (Humanity's Last Exam)** | Artificial Analysis v5 | Quality | **3** | 28 | **DeepSeek V4 Flash Vision (Max)** (#22, 0.211) ahead of **DeepSeek V4 Pro 0813 (Max)** (#24, 0.195); **GLM-5.3-Flash** (#25, 0.182) ahead of **GLM-5.3 (Max)** (#26, 0.179) *(+1 more)* |
| 45 | **AA-Omniscience Raw Accuracy** | Artificial Analysis v5 | Quality | **3** | 28 | **Muse Spark Open (Xhigh)** (#15, 0.42) ahead of **Muse Wonder Full (Max)** (#16, 0.41); **Muse Spark Open (Xhigh)** (#15, 0.42) ahead of **Muse Wonder (Max)** (#20, 0.38) *(+1 more)* |
| 46 | **FrontierCode 1.0** | Artificial Analysis v5 | Quality | **3** | 25 | **Muse Wonder (Max)** (#6, 0.465) ahead of **Muse Wonder Full (Max)** (#9, 0.449); **GLM-5.3-Flash** (#16, 0.41) ahead of **GLM-5.3 (Max)** (#17, 0.401) *(+1 more)* |
| 47 | **AutomationBench-AA SaaS Workflows** | Artificial Analysis v5 | Quality | **3** | 23 | **Claude Sonnet 5.5** (#5, 0.718) ahead of **Claude Opus 5.5** (#7, 0.695); **MiMo-V2.6-Flash** (#14, 0.64) ahead of **MiMo-V2.6-Pro** (#21, 0.586) *(+1 more)* |
| 48 | **Arena.ai Text-to-Video Generation** | LMSYS Arena.ai (2026) | Quality | **3** | 16 | **dreamina-seedance-2.0-720p** (#5, 1479.0) ahead of **dreamina-seedance-2.5-720p** (#7, 1474.0); **veo-3-fast-audio** (#16, 1348.0) ahead of **veo-3-audio** (#19, 1340.0) *(+1 more)* |
| 49 | **AA v4 Output Speed (Tokens/Sec, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Latency | **3** | 12 | **Qwen3 Next 80B A3B (Reasoning)** (#19, 203.1 tok/s) faster than **Qwen3 30B A3B 2507 (Reasoning)** (#44, 148.6 tok/s); **GPT-5.4 mini (xhigh)** (#24, 189.5 tok/s) faster than **GPT-5.4 nano (xhigh)** (#29, 172.8 tok/s) *(+1 more)* |
| 50 | **LiveBench 2.0 — Design** | LiveBench 2.0 (Oct 2026) | Quality | **3** | 8 | **gpt-6-luna** (#6, 82.5) ahead of **gpt-6-astra** (#9, 82.0); **gpt-6.1-terra** (#7, 82.3) ahead of **gpt-6.1-sol** (#8, 82.1) *(+1 more)* |
| 51 | **AutomationBench-AA — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **3** | 6 | **Muse Wonder (Max)** (#5, 130.1s) faster than **Muse Spark Open (Xhigh)** (#12, 209.9s); **GPT-6 Astra (Max)** (#8, 163.4s) faster than **GPT-6 Luna (Max)** (#18, 285.2s) *(+1 more)* |
| 52 | **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **3** | 6 | **GPT-6 Astra (Max)** (#8, 469.8s) faster than **GPT-6 Luna (Max)** (#12, 585.3s); **GPT-6.1 Sol (Max)** (#10, 543.6s) faster than **GPT-6.1 Terra (Max)** (#14, 694.3s) *(+1 more)* |
| 53 | **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **3** | 6 | **GPT-6.1 Sol (Max)** (#9, 24.7s) faster than **GPT-6.1 Terra (Max)** (#23, 86.4s); **GPT-6 Astra (Max)** (#10, 24.7s) faster than **GPT-6 Luna (Max)** (#16, 39.1s) *(+1 more)* |
| 54 | **LMSYS Arena Math (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **2** | 46 | **qwen3-32b** (#7, 1390.2) ahead of **qwen3-235b-a22b** (#10, 1374.0); **gemini-2.0-flash-thinking-exp-01-21** (#13, 1360.8) ahead of **gemini-2.0-pro-exp-02-05** (#18, 1355.9) |
| 55 | **LMSYS Arena Coding (Classic)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **2** | 38 | **gemini-2.5-flash-preview-05-20** (#2, 1430.9) ahead of **gemini-2.5-pro-exp-03-25** (#4, 1418.5); **o1-mini** (#27, 1341.9) ahead of **o3-mini** (#31, 1338.0) |
| 56 | **LMSYS Arena Longer Query** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **2** | 36 | **gemini-2.0-flash-thinking-exp-01-21** (#10, 1360.3) ahead of **gemini-2.0-pro-exp-02-05** (#11, 1359.8); **o3-mini** (#40, 1306.0) ahead of **o4-mini-2025-04-16** (#42, 1300.2) |
| 57 | **GDP.pdf Document Deliverable** | Artificial Analysis v5 | Quality | **2** | 27 | **GLM-5.3-Flash** (#27, 0.154) ahead of **GLM-5.3 (Max)** (#42, 0.112); **DeepSeek V4 Flash Vision (Max)** (#35, 0.12) ahead of **DeepSeek V4 Pro 0813 (Max)** (#37, 0.114) |
| 58 | **AA-Briefcase v1.1 Knowledge Work** | Artificial Analysis v5 | Quality | **2** | 26 | **Claude Sonnet 5.5** (#1, 1813.6) ahead of **Claude Opus 5.5** (#2, 1800.5); **DeepSeek V4 Flash Vision (Max)** (#24, 1420.2) ahead of **DeepSeek V4 Pro 0813 (Max)** (#32, 1254.4) |
| 59 | **SciCode Scientific Coding** | Artificial Analysis v5 | Quality | **2** | 24 | **GPT-6.1 Terra (Max)** (#18, 0.551) ahead of **GPT-6.1 Sol (Max)** (#21, 0.542); **Inkling Small** (#32, 0.496) ahead of **Inkling (Xhigh)** (#44, 0.47) |
| 60 | **GDPval-AA Professional Work Elo** | Artificial Analysis v5 | Quality | **2** | 23 | **DeepSeek V4 Flash Vision (Max)** (#24, 1554.0) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 1457.4); **Inkling Small** (#42, 1132.6) ahead of **Inkling (Xhigh)** (#50, 1080.2) |
| 61 | **Tau3-Banking Agentic Benchmark** | Artificial Analysis v5 | Quality | **2** | 12 | **DeepSeek V4 Flash Vision (Max)** (#10, 0.41) ahead of **DeepSeek V4 Pro 0813 (Max)** (#11, 0.396); **Qwen3.5 122B A10B (Reasoning)** (#38, 0.153) ahead of **Qwen3.5 397B A17B (Reasoning)** (#44, 0.134) |
| 62 | **EvalPlus MBPP+ (35x Tests)** | EvalPlus | Quality | **2** | 11 | **DeepSeek-V2.5 (Nov 2024)** (#6, 74.1) ahead of **DeepSeek-V3 (Nov 2024)** (#9, 73.0); **GPT-4-Turbo (Nov 2023)** (#7, 73.3) ahead of **GPT 4o (Aug 2024)** (#10, 72.2) |
| 63 | **SWE-bench Verified Total Run Cost ($ USD)** | SWE-bench | Cost | **2** | 10 | **GPT 4.1 mini** ($217.58) cost more than **GPT 4.1** ($73.16); **GPT 5 nano (medium)** ($19.04) cost more than **GPT 5 mini (medium)** ($17.74) |
| 64 | **LiveBench 2.0 — Reasoning** | LiveBench 2.0 (Oct 2026) | Quality | **2** | 8 | **grok-4.6** (#7, 91.2) ahead of **grok-4.7** (#20, 82.7); **gpt-5.6-terra** (#10, 90.6) ahead of **gpt-6.1-terra** (#15, 88.7) |
| 65 | **LiveBench 2.0 — Browser** | LiveBench 2.0 (Oct 2026) | Quality | **2** | 8 | **claude-sonnet-5.5** (#5, 89.3) ahead of **claude-opus-5.5** (#6, 88.4); **grok-4.6** (#18, 49.4) ahead of **grok-4.7** (#20, 49.3) |
| 66 | **AA-AnalystAgent Data Analyst** | Artificial Analysis v5 | Quality | **2** | 6 | **Claude Sonnet 5.5** (#2, 0.575) ahead of **Claude Opus 5.5** (#3, 0.562); **Inkling Small** (#17, 0.275) ahead of **Inkling (Xhigh)** (#19, 0.237) |
| 67 | **AA-Briefcase v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **2** | 6 | **GPT-6 Astra (Max)** (#11, 870.2s) faster than **GPT-6 Luna (Max)** (#12, 922.0s); **Claude Opus 5.5** (#21, 2225.4s) faster than **Claude Sonnet 5.5** (#23, 2844.5s) |
| 68 | **Terminal-Bench 4.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **2** | 6 | **GPT-6 Astra (Max)** (#8, 958.5s) faster than **GPT-6 Luna (Max)** (#10, 1181.4s); **Claude Opus 5.5** (#16, 1665.0s) faster than **Claude Sonnet 5.5** (#17, 1740.0s) |
| 69 | **GDP.pdf Document — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **2** | 6 | **GPT-6 Astra (Max)** (#11, 117.1s) faster than **GPT-6 Luna (Max)** (#20, 208.1s); **GPT-6.1 Sol (Max)** (#12, 132.9s) faster than **GPT-6.1 Terra (Max)** (#14, 150.5s) |
| 70 | **HLE-Diamond — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **2** | 6 | **GPT-6 Astra (Max)** (#3, 138.0s) faster than **GPT-6 Luna (Max)** (#14, 248.6s); **GPT-6.1 Sol (Max)** (#5, 147.5s) faster than **GPT-6.1 Terra (Max)** (#15, 297.2s) |
| 71 | **AA-3D Interactive WebGL Elo** | Artificial Analysis v5 | Quality | **2** | 5 | **Claude Sonnet 5.5** (#1, 1198.8) ahead of **Claude Opus 5.5** (#2, 1196.4); **GLM-5.3-Flash** (#14, 936.6) ahead of **GLM-5.3 (Max)** (#16, 783.0) |
| 72 | **OpenAI HealthBench Medical Reasoning** | Artificial Analysis v5 | Quality | **2** | 4 | **Claude Sonnet 5.5** (#1, 0.621) ahead of **Claude Opus 5.5** (#6, 0.57); **Claude Haiku 5.5 (Max)** (#3, 0.585) ahead of **Claude Opus 5.5** (#6, 0.57) |
| 73 | **AA v4 GPQA Diamond (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **1** | 48 | **Grok 4.20 0309 v2 (Reasoning)** (#22, 0.911) ahead of **Grok 4.3** (#30, 0.901) |
| 74 | **LMSYS Arena Overall (243 Models)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **1** | 43 | **gemini-2.0-flash-thinking-exp-01-21** (#8, 1376.7) ahead of **gemini-2.0-pro-exp-02-05** (#9, 1376.3) |
| 75 | **LMSYS Arena Creative Writing** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **1** | 42 | **gemini-2.0-flash-thinking-exp-1219** (#10, 1368.8) ahead of **gemini-2.0-pro-exp-02-05** (#11, 1367.1) |
| 76 | **LMSYS Arena Coding (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **1** | 40 | **gemini-2.5-flash-preview-05-20** (#4, 1429.7) ahead of **gemini-2.5-pro-exp-03-25** (#6, 1425.3) |
| 77 | **AA v4 Agentic Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **1** | 39 | **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#19, 48.4) ahead of **DeepSeek V4 Pro (Reasoning, Max Effort)** (#43, 37.8) |
| 78 | **LMSYS Arena Multi-Turn Dialogue** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **1** | 34 | **o1-preview** (#21, 1323.9) ahead of **o1-2024-12-17** (#25, 1314.5) |
| 79 | **SWE-bench Verified (Bash-Only Standardized)** | SWE-bench | Quality | **1** | 33 | **Gemini 3 Flash** (#2, 75.8) ahead of **Gemini 3 Pro Preview** (#5, 74.2) |
| 80 | **AA-Omniscience v1.1 Net Score** | Artificial Analysis v5 | Quality | **1** | 31 | **Muse Spark Open (Xhigh)** (#12, 25.8) ahead of **Muse Wonder (Max)** (#13, 25.1) |
| 81 | **CritPt v2 Agentic Hard** | Artificial Analysis v5 | Quality | **1** | 30 | **Inkling Small** (#30, 0.185) ahead of **Inkling (Xhigh)** (#31, 0.18) |
| 82 | **AA Intelligence Index v5.0** | Artificial Analysis v5 | Quality | **1** | 27 | **Inkling Small** (#33, 12.9) ahead of **Inkling (Xhigh)** (#34, 12.5) |
| 83 | **CritPt Physics Reasoning** | Artificial Analysis v5 | Quality | **1** | 24 | **Inkling Small** (#44, 0.083) ahead of **Inkling (Xhigh)** (#48, 0.054) |
| 84 | **Terminal-Bench 4.0** | Artificial Analysis v5 | Quality | **1** | 24 | **Claude Sonnet 5.5** (#3, 0.636) ahead of **Claude Opus 5.5** (#4, 0.596) |
| 85 | **Humanity's Last Exam (Full HLE)** | Artificial Analysis v5 | Quality | **1** | 21 | **Inkling Small** (#44, 0.333) ahead of **Inkling (Xhigh)** (#46, 0.319) |
| 86 | **MMMU-Pro Multimodal Understanding** | Artificial Analysis v5 | Quality | **1** | 21 | **Inkling Small** (#29, 0.741) ahead of **Inkling (Xhigh)** (#30, 0.735) |
| 87 | **EvalPlus HumanEval+ (80x Tests)** | EvalPlus | Quality | **1** | 21 | **claude-3-haiku (Mar 2024)** (#35, 68.9) ahead of **claude-3-sonnet (Mar 2024)** (#43, 64.0) |
| 88 | **Arena.ai Image-to-Video Generation** | LMSYS Arena.ai (2026) | Quality | **1** | 15 | **veo-3-fast-audio** (#21, 1326.0) ahead of **veo-3** (#30, 1258.0) |
| 89 | **EvalPlus Combined Average** | EvalPlus | Quality | **1** | 13 | **claude-3-haiku (Mar 2024)** (#23, 68.8) ahead of **claude-3-sonnet (Mar 2024)** (#32, 66.7) |
| 90 | **LiveBench v1 Cost per Successful Task ($ USD)** | LiveBench v1 (2026) | Cost | **1** | 12 | **claude-sonnet-5-5-max-effort** ($0.868) cost more than **claude-opus-5-5-max-effort** ($0.799) |
| 91 | **AIME 2025 Competition Math** | Artificial Analysis v5 | Quality | **1** | 11 | **Ministral 3 8B** (#35, 0.317) ahead of **Ministral 3 14B** (#36, 0.3) |
| 92 | **SWE-bench Test (All Submissions)** | SWE-bench | Quality | **1** | 11 | **GPT 4 (1106)** (#16, 12.5) ahead of **GPT 4o** (#17, 12.0) |
| 93 | **GPQA Diamond** | Artificial Analysis v5 | Quality | **1** | 9 | **Inkling Small** (#19, 0.895) ahead of **Inkling (Xhigh)** (#25, 0.872) |
| 94 | **Terminal-Bench 2.1** | Artificial Analysis v5 | Quality | **1** | 9 | **GLM-5.3-Flash** (#6, 0.843) ahead of **GLM-5.3 (Max)** (#7, 0.839) |
| 95 | **LiveBench 2.0 — Coding** | LiveBench 2.0 (Oct 2026) | Quality | **1** | 8 | **grok-4.6** (#12, 89.1) ahead of **grok-4.7** (#18, 84.5) |
| 96 | **Aider Refactoring Leaderboard** | Aider Coding | Quality | **1** | 8 | **gpt-4-1106-preview** (#6, 50.6) ahead of **gpt-4o-2024-08-06** (#8, 49.4) |
| 97 | **Harvey LAB-AA v1.1 Legal Agent** | Artificial Analysis v5 | Quality | **1** | 7 | **GLM-5.3-Flash** (#11, 0.008) ahead of **GLM-5.3 (Max)** (#13, 0.003) |
| 98 | **Arena.ai Coding (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **1** | 7 | **mimo-v2.6-flash** (#13, 1636.0) ahead of **mimo-v2.6-pro** (#16, 1630.0) |
| 99 | **Code2Video-AA Elo** | Artificial Analysis v5 | Quality | **1** | 6 | **MiMo-V2.6-Flash** (#9, 1051.6) ahead of **MiMo-V2.6-Pro** (#10, 1051.5) |
| 100 | **AA Intelligence Index Time per Task (Seconds)** | Artificial Analysis v5 | Latency | **1** | 6 | **Claude Opus 5.5** (#19, 1140.8s) faster than **Claude Sonnet 5.5** (#21, 1298.5s) |
| 101 | **FrontierCode 2.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($1.29) cost more than **GPT-6.1 Sol (Max)** ($1.13) |
| 102 | **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($0.043) cost more than **GPT-6.1 Sol (Max)** ($0.018) |
| 103 | **HLE-Diamond — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($0.146) cost more than **GPT-6.1 Sol (Max)** ($0.109) |
| 104 | **CritPt v2 Hard — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **GPT-6.1 Terra (Max)** ($0.251) cost more than **GPT-6.1 Sol (Max)** ($0.230) |
| 105 | **Terminal-Bench Science — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **1** | 6 | **Claude Sonnet 5.5** ($23.76) cost more than **Claude Opus 5.5** ($19.97) |
| 106 | **Terminal-Bench Science — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency | **1** | 6 | **Claude Opus 5.5** (#15, 2020.7s) faster than **Claude Sonnet 5.5** (#19, 2315.2s) |
| 107 | **LiveBench 2.0 Cost — Coding ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **1** | 6 | **gpt-6.1-terra** ($24.97) cost more than **gpt-6.1-sol** ($13.98) |
| 108 | **HealthBench Professional Clinical** | Artificial Analysis v5 | Quality | **1** | 4 | **Claude Sonnet 5.5** (#3, 0.63) ahead of **Claude Opus 5.5** (#5, 0.599) |
| 109 | **EnterpriseOps-Gym-AA** | Artificial Analysis v5 | Quality | **1** | 3 | **Inkling Small** (#7, 0.427) ahead of **Inkling (Xhigh)** (#12, 0.38) |
| 110 | **ITBench-AA SRE & Root Cause** | Artificial Analysis v5 | Quality | **1** | 1 | **GLM-5.3-Flash** (#3, 0.512) ahead of **GLM-5.3 (Max)** (#6, 0.461) |
| 111 | **LMSYS Arena Instruction Following (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 44 | None (all 44 pairs follow expected order) |
| 112 | **LMSYS Arena Overall (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 42 | None (all 42 pairs follow expected order) |
| 113 | **LMSYS Arena Hard Prompts (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 39 | None (all 39 pairs follow expected order) |
| 114 | **LMSYS Arena Instruction Following** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 38 | None (all 38 pairs follow expected order) |
| 115 | **LMSYS Arena Hard Prompts** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0** | 36 | None (all 36 pairs follow expected order) |
| 116 | **Terminal-Bench Science 0.1** | Artificial Analysis v5 | Quality | **0** | 31 | None (all 31 pairs follow expected order) |
| 117 | **SWE-bench Multimodal (All Submissions)** | SWE-bench | Quality | **0** | 19 | None (all 19 pairs follow expected order) |
| 118 | **Terminal-Bench Hard** | Artificial Analysis v5 | Quality | **0** | 18 | None (all 18 pairs follow expected order) |
| 119 | **IFBench Instruction Following** | Artificial Analysis v5 | Quality | **0** | 18 | None (all 18 pairs follow expected order) |
| 120 | **AA API Output Price ($/1M Tokens)** | Artificial Analysis v5 | Cost | **0** | 16 | None (all 16 pairs follow expected order) |
| 121 | **AA API Blended Price (3:1 In:Out $/1M)** | Artificial Analysis v5 | Cost | **0** | 13 | None (all 13 pairs follow expected order) |
| 122 | **Aider Polyglot Total Benchmark Cost ($ USD)** | Aider Coding | Cost | **0** | 13 | None (all 13 pairs follow expected order) |
| 123 | **AA API Input Price ($/1M Tokens)** | Artificial Analysis v5 | Cost | **0** | 12 | None (all 12 pairs follow expected order) |
| 124 | **LiveBench v1 Cost per Question ($ USD)** | LiveBench v1 (2026) | Cost | **0** | 12 | None (all 12 pairs follow expected order) |
| 125 | **AA v4 Blended API Price ($/1M, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Cost | **0** | 11 | None (all 11 pairs follow expected order) |
| 126 | **LiveCodeBench** | Artificial Analysis v5 | Quality | **0** | 10 | None (all 10 pairs follow expected order) |
| 127 | **Arena.ai Text-to-Image Generation** | LMSYS Arena.ai (2026) | Quality | **0** | 10 | None (all 10 pairs follow expected order) |
| 128 | **LiveBench 2.0 Overall Score** | LiveBench 2.0 (Oct 2026) | Quality | **0** | 8 | None (all 8 pairs follow expected order) |
| 129 | **LiveBench 2.0 — Long Agentic** | LiveBench 2.0 (Oct 2026) | Quality | **0** | 8 | None (all 8 pairs follow expected order) |
| 130 | **LiveBench 2.0 — Data Analysis** | LiveBench 2.0 (Oct 2026) | Quality | **0** | 8 | None (all 8 pairs follow expected order) |
| 131 | **LiveBench 2.0 — Research** | LiveBench 2.0 (Oct 2026) | Quality | **0** | 8 | None (all 8 pairs follow expected order) |
| 132 | **AA Intelligence Index Total Run Cost ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 133 | **AA-Briefcase Total Suite Cost ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 134 | **AA-Briefcase v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 135 | **AutomationBench-AA — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 136 | **Terminal-Bench 4.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 137 | **GDP.pdf Document — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 138 | **LiveBench 2.0 Cost — Overall Mean ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 139 | **LiveBench 2.0 Cost — Long Agentic ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 140 | **LiveBench 2.0 Cost — Browser ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 141 | **LiveBench 2.0 Cost — Data Analysis ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 142 | **LiveBench 2.0 Cost — Research ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 143 | **LiveBench 2.0 Cost — Design ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0** | 6 | None (all 6 pairs follow expected order) |
| 144 | **Arena.ai Image Editing** | LMSYS Arena.ai (2026) | Quality | **0** | 6 | None (all 6 pairs follow expected order) |

</details>
