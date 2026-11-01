# AI Benchmark Inverted Pairs

- **Live Table (Popular)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=popular_benchmarks)
- **Live Table (ALL)**: [https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL](https://sagarvare.github.io/ai-benchmark-contradiction-index/?view=ALL)
- **Repository**: [https://github.com/sagarvare/ai-benchmark-contradiction-index](https://github.com/sagarvare/ai-benchmark-contradiction-index)

This table measures the **count of inverted model pairs** within the **Top 50 ranked models** on each AI benchmark. A pair of models is counted as inverted when their relative ranking contradicts the expected ordering within the same model family under two rules:

1. **Same-generation tier rule:** Within the same model family and version, a larger tier is expected to rank ahead of a smaller tier (for example, **GPT 6.1 Sol** ahead of **GPT 6.1 Terra** ahead of **GPT 6.1 Luna**, or **Claude Opus 5.5** ahead of **Claude Sonnet 5.5** ahead of **Claude Haiku 5.5**). For latency benchmarks, this order is reversed so smaller models are expected to be faster. For cost benchmarks, larger models are expected to cost more.
2. **Cross-generation same-tier rule:** Within the same model family and size tier, a newer version is expected to rank ahead of an older version (for example, **GPT 6.1 Sol** ahead of **GPT 6.0 Sol**, or **Claude Opus 5.5** ahead of **Claude Opus 4.7**). Crossed pairs such as **GPT 6.1 Sol** and **GPT 6.0 Luna** are not compared.

---

## Popular

| Benchmark | Inverted Score | Example Inversions in the Benchmark |
| :--- | :-: | :--- |
| **LMSYS Arena Hard Prompts** | **0** | None |
| **IFBench Instruction Following** | **0** | None |
| **AA API Blended Price (3:1 In:Out $/1M)** | **0** | None |
| **LiveBench 2.0 Overall Score** | **0** | None |
| **AA Intelligence Index Total Run Cost ($ USD)** | **0** | None |
| **AA v4 GPQA Diamond (Aug 2026)** | **1** | **Grok 4.20 0309 v2 (Reasoning)** (#22, 0.911) ahead of **Grok 4.3** (#30, 0.901) |
| **SWE-bench Verified (Bash-Only Standardized)** | **1** | **Gemini 3 Flash** (#2, 75.8) ahead of **Gemini 3 Pro Preview** (#5, 74.2) |
| **AA-Omniscience v1.1 Net Score** | **1** | **Muse Spark Open (Xhigh)** (#12, 25.8) ahead of **Muse Wonder (Max)** (#13, 25.1) |
| **CritPt v2 Agentic Hard** | **1** | **Inkling Small** (#30, 0.185) ahead of **Inkling (Xhigh)** (#31, 0.18) |
| **AA Intelligence Index v5.0** | **1** | **Inkling Small** (#33, 12.9) ahead of **Inkling (Xhigh)** (#34, 12.5) |
| **CritPt Physics Reasoning** | **1** | **Inkling Small** (#44, 0.083) ahead of **Inkling (Xhigh)** (#48, 0.054) |
| **Terminal-Bench 4.0** | **1** | **Claude Sonnet 5.5** (#3, 0.636) ahead of **Claude Opus 5.5** (#4, 0.596) |
| **EvalPlus Combined Average** | **1** | **claude-3-haiku (Mar 2024)** (#23, 68.8) ahead of **claude-3-sonnet (Mar 2024)** (#32, 66.7) |
| **LiveBench 2.0 — Coding** | **1** | **grok-4.6** (#12, 89.1) ahead of **grok-4.7** (#18, 84.5) |
| **Arena.ai Coding (Oct 2026)** | **1** | **mimo-v2.6-flash** (#13, 1636.0) ahead of **mimo-v2.6-pro** (#16, 1630.0) |
| **AA Intelligence Index Time per Task (Seconds)** | **1** | **Claude Opus 5.5** (#19, 1140.8s) faster than **Claude Sonnet 5.5** (#21, 1298.5s) |
| **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($0.043) cost more than **GPT-6.1 Sol (Max)** ($0.018) |
| **FrontierCode 2.0 — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($1.29) cost more than **GPT-6.1 Sol (Max)** ($1.13) |
| **LiveBench 2.0 Cost — Coding ($/Task)** | **1** | **gpt-6.1-terra** ($24.97) cost more than **gpt-6.1-sol** ($13.98) |
| **AA-Briefcase v1.1 Knowledge Work** | **2** | **Claude Sonnet 5.5** (#1, 1813.6) ahead of **Claude Opus 5.5** (#2, 1800.5); **DeepSeek V4 Flash Vision (Max)** (#24, 1420.2) ahead of **DeepSeek V4 Pro 0813 (Max)** (#32, 1254.4) |
| **SciCode Scientific Coding** | **2** | **GPT-6.1 Terra (Max)** (#18, 0.551) ahead of **GPT-6.1 Sol (Max)** (#21, 0.542); **Inkling Small** (#32, 0.496) ahead of **Inkling (Xhigh)** (#44, 0.47) |
| **GDPval-AA Professional Work Elo** | **2** | **DeepSeek V4 Flash Vision (Max)** (#24, 1554.0) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 1457.4); **Inkling Small** (#42, 1132.6) ahead of **Inkling (Xhigh)** (#50, 1080.2) |
| **LiveBench 2.0 — Browser** | **2** | **claude-sonnet-5.5** (#5, 89.3) ahead of **claude-opus-5.5** (#6, 88.4); **grok-4.6** (#18, 49.4) ahead of **grok-4.7** (#20, 49.3) |
| **LiveBench 2.0 — Reasoning** | **2** | **grok-4.6** (#7, 91.2) ahead of **grok-4.7** (#20, 82.7); **gpt-5.6-terra** (#10, 90.6) ahead of **gpt-6.1-terra** (#15, 88.7) |
| **OpenAI HealthBench Medical Reasoning** | **2** | **Claude Sonnet 5.5** (#1, 0.621) ahead of **Claude Opus 5.5** (#6, 0.57); **Claude Haiku 5.5 (Max)** (#3, 0.585) ahead of **Claude Opus 5.5** (#6, 0.57) |
| **HLE-Diamond (Humanity's Last Exam)** | **3** | **DeepSeek V4 Flash Vision (Max)** (#22, 0.211) ahead of **DeepSeek V4 Pro 0813 (Max)** (#24, 0.195); **GLM-5.3-Flash** (#25, 0.182) ahead of **GLM-5.3 (Max)** (#26, 0.179); **Inkling Small** (#40, 0.121) ahead of **Inkling (Xhigh)** (#44, 0.106) |
| **AutomationBench-AA SaaS Workflows** | **3** | **Claude Sonnet 5.5** (#5, 0.718) ahead of **Claude Opus 5.5** (#7, 0.695); **MiMo-V2.6-Flash** (#14, 0.64) ahead of **MiMo-V2.6-Pro** (#21, 0.586); **Claude Sonnet 5.5 (Xhigh, Default Fallback)** (#16, 0.655) ahead of **Claude Opus 5.5 (Xhigh, Default Fallback)** (#17, 0.649) |
| **LiveBench 2.0 — Design** | **3** | **gpt-6-luna** (#6, 82.5) ahead of **gpt-6-astra** (#9, 82.0); **gpt-6.1-terra** (#7, 82.3) ahead of **gpt-6.1-sol** (#8, 82.1); **grok-4.6** (#10, 79.8) ahead of **grok-4.7** (#13, 78.0) |
| **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | **3** | **GPT-6.1 Sol (Max)** (#9, 24.7s) faster than **GPT-6.1 Terra (Max)** (#23, 86.4s); **GPT-6 Astra (Max)** (#10, 24.7s) faster than **GPT-6 Luna (Max)** (#16, 39.1s); **Claude Opus 5.5** (#20, 61.4s) faster than **Claude Sonnet 5.5** (#22, 68.9s) |
| **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | **3** | **GPT-6 Astra (Max)** (#8, 469.8s) faster than **GPT-6 Luna (Max)** (#12, 585.3s); **GPT-6.1 Sol (Max)** (#10, 543.6s) faster than **GPT-6.1 Terra (Max)** (#14, 694.3s); **Claude Opus 5.5** (#20, 1316.4s) faster than **Claude Sonnet 5.5** (#22, 1437.7s) |
| **LiveBench v1 — Mathematics** | **4** | **gemini-3.7-flash-high** (#19, 93.5) ahead of **gemini-3.8-flash-high** (#25, 91.6); **claude-opus-4-5-20251101-thinking-64k-high-effort** (#31, 90.4) ahead of **claude-opus-4-6-thinking-auto-high-effort** (#35, 89.3); **glm-5.2** (#33, 89.8) ahead of **glm-5.3** (#41, 87.9) *(+1 more)* |
| **Aider Polyglot Coding (Pass@2 %)** | **4** | **claude-3-7-sonnet-20250219** (#11, 64.9) ahead of **claude-sonnet-4-20250514** (#14, 61.3); **gpt-4.1** (#23, 52.4) ahead of **gpt-4.5-preview** (#27, 44.9); **claude-3-7-sonnet-20250219** (#19, 64.9) ahead of **claude-sonnet-4-20250514 (no thinking)** (#28, 56.4) *(+1 more)* |
| **MLCR-AA Medical Long-Context** | **4** | **Claude Sonnet 5.5** (#1, 0.417) ahead of **Claude Opus 5.5** (#9, 0.278); **Claude Haiku 5.5 (Max)** (#5, 0.35) ahead of **Claude Opus 5.5** (#9, 0.278); **Qwen3.8-Flash-Next** (#15, 0.206) ahead of **Qwen3.8 Max (0902)** (#17, 0.2) *(+1 more)* |
| **FrontierCode 2.0** | **5** | **GPT-6.1 Terra (Max)** (#3, 0.423) ahead of **GPT-6.1 Sol (Max)** (#5, 0.406); **Inkling Small** (#34, 0.048) ahead of **Inkling (Xhigh)** (#35, 0.039); **GPT-6.1 Terra** (#12, 0.375) ahead of **GPT-6.1 Sol** (#14, 0.367) *(+2 more)* |
| **AA Long-Context Reasoning (LCR)** | **5** | **GPT-6 Luna (Max)** (#7, 0.833) ahead of **GPT-6 Astra (Max)** (#25, 0.807); **Muse Glimmer** (#8, 0.833) ahead of **Muse Wonder (Max)** (#26, 0.807); **DeepSeek V4 Flash Vision (Max)** (#24, 0.813) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 0.803) *(+2 more)* |
| **LiveBench v1 Global Average** | **6** | **gpt-5.6-sol-max** (#9, 81.1) ahead of **gpt-6-sol-max** (#13, 79.2); **gemini-3.7-flash-high** (#15, 78.8) ahead of **gemini-3.8-flash-high** (#32, 75.8); **claude-opus-4-7-xhigh-effort** (#27, 76.5) ahead of **claude-opus-4-8-max-effort** (#28, 76.2) *(+3 more)* |
| **Aider Polyglot Latency (Seconds per Case)** | **6** | **gpt-4o-2024-11-20** (#4, 12.1s) faster than **gpt-4o-mini-2024-07-18** (#8, 17.3s); **claude-3-5-sonnet-20241022** (#13, 21.4s) faster than **claude-3-5-haiku-20241022** (#17, 31.8s); **Qwen3 235B A22B diff, no think, Alibaba API** (#25, 45.4s) faster than **Qwen3 32B** (#48, 372.2s) *(+3 more)* |
| **Tau2-Bench Tool-Use Agentic** | **7** | **Qwen3.5 4B (Reasoning)** (#11, 0.921) ahead of **Qwen3.5 9B (Reasoning)** (#19, 0.868); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 9B (Non-reasoning)** (#24, 0.851); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 122B A10B (Non-reasoning)** (#26, 0.845) *(+4 more)* |
| **AA Time to First Answer Token (Seconds)** | **7** | **Ministral 3 8B** (#8, 0.8s) faster than **Ministral 3 3B** (#9, 0.9s); **Nemotron 3 Ultra** (#33, 7.5s) faster than **Nemotron 3 Nano Omni 30B A3B** (#36, 9.6s); **MiMo-V2.6-Pro** (#34, 8.1s) faster than **MiMo-V2.6-Flash** (#41, 12.9s) *(+4 more)* |
| **Arena.ai Text Overall (Oct 2026)** | **8** | **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5.5-high** (#4, 1504.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-4-7-high** (#5, 1501.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5-max** (#11, 1489.0) *(+5 more)* |
| **Arena.ai Vision Multimodal (Oct 2026)** | **8** | **claude-fable-5-high** (#1, 1309.0) ahead of **claude-fable-5.1-max** (#13, 1288.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-4-7-high** (#4, 1298.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-5-high** (#12, 1289.0) *(+5 more)* |
| **Aider Code Editing Leaderboard** | **10** | **gpt-4-0613** (#17, 67.7) ahead of **gpt-4-0125-preview** (#20, 66.2); **Qwen2.5-Coder-14B-Instruct** (#19, 69.2) ahead of **openrouter/qwen/qwen-2.5-coder-32b-instruct** (#32, 65.4); **gpt-4-0613** (#22, 67.7) ahead of **gpt-4-1106-preview** (#28, 65.4) *(+7 more)* |
| **SWE-bench Verified (All Submissions)** | **11** | **Claude 4 Sonnet** (#4, 76.8) ahead of **Claude 4 Opus** (#16, 73.2); **Claude 4.5 Opus** (#1, 79.2) ahead of **Claude 4.6 Opus** (#12, 75.6); **Claude 4 Sonnet** (#5, 76.8) ahead of **Claude 4.5 Sonnet** (#15, 74.8) *(+8 more)* |
| **LiveBench v1 — Coding** | **14** | **claude-sonnet-5-5-max-effort** (#1, 91.4) ahead of **claude-opus-5-5-max-effort** (#2, 89.3); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6-sol-max** (#12, 81.8); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6.1-sol-max** (#19, 80.4) *(+11 more)* |

---

## ALL

<details>
<summary><strong>Expand ALL benchmarks</strong></summary>

| Benchmark | Inverted Score | Example Inversions in the Benchmark |
| :--- | :-: | :--- |
| **LMSYS Arena Instruction Following (Style-Controlled)** | **0** | None |
| **LMSYS Arena Overall (Style-Controlled)** | **0** | None |
| **LMSYS Arena Hard Prompts (Style-Controlled)** | **0** | None |
| **LMSYS Arena Instruction Following** | **0** | None |
| **LMSYS Arena Hard Prompts** | **0** | None |
| **Terminal-Bench Science 0.1** | **0** | None |
| **SWE-bench Multimodal (All Submissions)** | **0** | None |
| **IFBench Instruction Following** | **0** | None |
| **Terminal-Bench Hard** | **0** | None |
| **AA API Output Price ($/1M Tokens)** | **0** | None |
| **AA API Blended Price (3:1 In:Out $/1M)** | **0** | None |
| **Aider Polyglot Total Benchmark Cost ($ USD)** | **0** | None |
| **AA API Input Price ($/1M Tokens)** | **0** | None |
| **LiveBench v1 Cost per Question ($ USD)** | **0** | None |
| **AA v4 Blended API Price ($/1M, Aug 2026)** | **0** | None |
| **Arena.ai Text-to-Image Generation** | **0** | None |
| **LiveCodeBench** | **0** | None |
| **LiveBench 2.0 Overall Score** | **0** | None |
| **LiveBench 2.0 — Data Analysis** | **0** | None |
| **LiveBench 2.0 — Long Agentic** | **0** | None |
| **LiveBench 2.0 — Research** | **0** | None |
| **AA Intelligence Index Total Run Cost ($ USD)** | **0** | None |
| **AA-Briefcase Total Suite Cost ($ USD)** | **0** | None |
| **AA-Briefcase v1.1 — Total Cost per Task ($ USD)** | **0** | None |
| **Arena.ai Image Editing** | **0** | None |
| **AutomationBench-AA — Total Cost per Task ($ USD)** | **0** | None |
| **GDP.pdf Document — Total Cost per Task ($ USD)** | **0** | None |
| **LiveBench 2.0 Cost — Browser ($/Task)** | **0** | None |
| **LiveBench 2.0 Cost — Data Analysis ($/Task)** | **0** | None |
| **LiveBench 2.0 Cost — Design ($/Task)** | **0** | None |
| **LiveBench 2.0 Cost — Long Agentic ($/Task)** | **0** | None |
| **LiveBench 2.0 Cost — Overall Mean ($/Task)** | **0** | None |
| **LiveBench 2.0 Cost — Research ($/Task)** | **0** | None |
| **Terminal-Bench 4.0 — Total Cost per Task ($ USD)** | **0** | None |
| **AA v4 GPQA Diamond (Aug 2026)** | **1** | **Grok 4.20 0309 v2 (Reasoning)** (#22, 0.911) ahead of **Grok 4.3** (#30, 0.901) |
| **LMSYS Arena Overall (243 Models)** | **1** | **gemini-2.0-flash-thinking-exp-01-21** (#8, 1376.7) ahead of **gemini-2.0-pro-exp-02-05** (#9, 1376.3) |
| **LMSYS Arena Creative Writing** | **1** | **gemini-2.0-flash-thinking-exp-1219** (#10, 1368.8) ahead of **gemini-2.0-pro-exp-02-05** (#11, 1367.1) |
| **LMSYS Arena Coding (Style-Controlled)** | **1** | **gemini-2.5-flash-preview-05-20** (#4, 1429.7) ahead of **gemini-2.5-pro-exp-03-25** (#6, 1425.3) |
| **AA v4 Agentic Index (Aug 2026)** | **1** | **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#19, 48.4) ahead of **DeepSeek V4 Pro (Reasoning, Max Effort)** (#43, 37.8) |
| **LMSYS Arena Multi-Turn Dialogue** | **1** | **o1-preview** (#21, 1323.9) ahead of **o1-2024-12-17** (#25, 1314.5) |
| **SWE-bench Verified (Bash-Only Standardized)** | **1** | **Gemini 3 Flash** (#2, 75.8) ahead of **Gemini 3 Pro Preview** (#5, 74.2) |
| **AA-Omniscience v1.1 Net Score** | **1** | **Muse Spark Open (Xhigh)** (#12, 25.8) ahead of **Muse Wonder (Max)** (#13, 25.1) |
| **CritPt v2 Agentic Hard** | **1** | **Inkling Small** (#30, 0.185) ahead of **Inkling (Xhigh)** (#31, 0.18) |
| **AA Intelligence Index v5.0** | **1** | **Inkling Small** (#33, 12.9) ahead of **Inkling (Xhigh)** (#34, 12.5) |
| **CritPt Physics Reasoning** | **1** | **Inkling Small** (#44, 0.083) ahead of **Inkling (Xhigh)** (#48, 0.054) |
| **Terminal-Bench 4.0** | **1** | **Claude Sonnet 5.5** (#3, 0.636) ahead of **Claude Opus 5.5** (#4, 0.596) |
| **EvalPlus HumanEval+ (80x Tests)** | **1** | **claude-3-haiku (Mar 2024)** (#35, 68.9) ahead of **claude-3-sonnet (Mar 2024)** (#43, 64.0) |
| **Humanity's Last Exam (Full HLE)** | **1** | **Inkling Small** (#44, 0.333) ahead of **Inkling (Xhigh)** (#46, 0.319) |
| **MMMU-Pro Multimodal Understanding** | **1** | **Inkling Small** (#29, 0.741) ahead of **Inkling (Xhigh)** (#30, 0.735) |
| **Arena.ai Image-to-Video Generation** | **1** | **veo-3-fast-audio** (#21, 1326.0) ahead of **veo-3** (#30, 1258.0) |
| **EvalPlus Combined Average** | **1** | **claude-3-haiku (Mar 2024)** (#23, 68.8) ahead of **claude-3-sonnet (Mar 2024)** (#32, 66.7) |
| **LiveBench v1 Cost per Successful Task ($ USD)** | **1** | **claude-sonnet-5-5-max-effort** ($0.868) cost more than **claude-opus-5-5-max-effort** ($0.799) |
| **AIME 2025 Competition Math** | **1** | **Ministral 3 8B** (#35, 0.317) ahead of **Ministral 3 14B** (#36, 0.3) |
| **SWE-bench Test (All Submissions)** | **1** | **GPT 4 (1106)** (#16, 12.5) ahead of **GPT 4o** (#17, 12.0) |
| **GPQA Diamond** | **1** | **Inkling Small** (#19, 0.895) ahead of **Inkling (Xhigh)** (#25, 0.872) |
| **Terminal-Bench 2.1** | **1** | **GLM-5.3-Flash** (#6, 0.843) ahead of **GLM-5.3 (Max)** (#7, 0.839) |
| **Aider Refactoring Leaderboard** | **1** | **gpt-4-1106-preview** (#6, 50.6) ahead of **gpt-4o-2024-08-06** (#8, 49.4) |
| **LiveBench 2.0 — Coding** | **1** | **grok-4.6** (#12, 89.1) ahead of **grok-4.7** (#18, 84.5) |
| **Arena.ai Coding (Oct 2026)** | **1** | **mimo-v2.6-flash** (#13, 1636.0) ahead of **mimo-v2.6-pro** (#16, 1630.0) |
| **Harvey LAB-AA v1.1 Legal Agent** | **1** | **GLM-5.3-Flash** (#11, 0.008) ahead of **GLM-5.3 (Max)** (#13, 0.003) |
| **AA Intelligence Index Time per Task (Seconds)** | **1** | **Claude Opus 5.5** (#19, 1140.8s) faster than **Claude Sonnet 5.5** (#21, 1298.5s) |
| **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($0.043) cost more than **GPT-6.1 Sol (Max)** ($0.018) |
| **Code2Video-AA Elo** | **1** | **MiMo-V2.6-Flash** (#9, 1051.6) ahead of **MiMo-V2.6-Pro** (#10, 1051.5) |
| **CritPt v2 Hard — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($0.251) cost more than **GPT-6.1 Sol (Max)** ($0.230) |
| **FrontierCode 2.0 — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($1.29) cost more than **GPT-6.1 Sol (Max)** ($1.13) |
| **HLE-Diamond — Total Cost per Task ($ USD)** | **1** | **GPT-6.1 Terra (Max)** ($0.146) cost more than **GPT-6.1 Sol (Max)** ($0.109) |
| **LiveBench 2.0 Cost — Coding ($/Task)** | **1** | **gpt-6.1-terra** ($24.97) cost more than **gpt-6.1-sol** ($13.98) |
| **Terminal-Bench Science — Total Cost per Task ($ USD)** | **1** | **Claude Sonnet 5.5** ($23.76) cost more than **Claude Opus 5.5** ($19.97) |
| **Terminal-Bench Science — Wall-Clock Time per Task (Sec)** | **1** | **Claude Opus 5.5** (#15, 2020.7s) faster than **Claude Sonnet 5.5** (#19, 2315.2s) |
| **HealthBench Professional Clinical** | **1** | **Claude Sonnet 5.5** (#3, 0.63) ahead of **Claude Opus 5.5** (#5, 0.599) |
| **EnterpriseOps-Gym-AA** | **1** | **Inkling Small** (#7, 0.427) ahead of **Inkling (Xhigh)** (#12, 0.38) |
| **ITBench-AA SRE & Root Cause** | **1** | **GLM-5.3-Flash** (#3, 0.512) ahead of **GLM-5.3 (Max)** (#6, 0.461) |
| **LMSYS Arena Math (Style-Controlled)** | **2** | **qwen3-32b** (#7, 1390.2) ahead of **qwen3-235b-a22b** (#10, 1374.0); **gemini-2.0-flash-thinking-exp-01-21** (#13, 1360.8) ahead of **gemini-2.0-pro-exp-02-05** (#18, 1355.9) |
| **LMSYS Arena Coding (Classic)** | **2** | **gemini-2.5-flash-preview-05-20** (#2, 1430.9) ahead of **gemini-2.5-pro-exp-03-25** (#4, 1418.5); **o1-mini** (#27, 1341.9) ahead of **o3-mini** (#31, 1338.0) |
| **LMSYS Arena Longer Query** | **2** | **gemini-2.0-flash-thinking-exp-01-21** (#10, 1360.3) ahead of **gemini-2.0-pro-exp-02-05** (#11, 1359.8); **o3-mini** (#40, 1306.0) ahead of **o4-mini-2025-04-16** (#42, 1300.2) |
| **GDP.pdf Document Deliverable** | **2** | **GLM-5.3-Flash** (#27, 0.154) ahead of **GLM-5.3 (Max)** (#42, 0.112); **DeepSeek V4 Flash Vision (Max)** (#35, 0.12) ahead of **DeepSeek V4 Pro 0813 (Max)** (#37, 0.114) |
| **AA-Briefcase v1.1 Knowledge Work** | **2** | **Claude Sonnet 5.5** (#1, 1813.6) ahead of **Claude Opus 5.5** (#2, 1800.5); **DeepSeek V4 Flash Vision (Max)** (#24, 1420.2) ahead of **DeepSeek V4 Pro 0813 (Max)** (#32, 1254.4) |
| **SciCode Scientific Coding** | **2** | **GPT-6.1 Terra (Max)** (#18, 0.551) ahead of **GPT-6.1 Sol (Max)** (#21, 0.542); **Inkling Small** (#32, 0.496) ahead of **Inkling (Xhigh)** (#44, 0.47) |
| **GDPval-AA Professional Work Elo** | **2** | **DeepSeek V4 Flash Vision (Max)** (#24, 1554.0) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 1457.4); **Inkling Small** (#42, 1132.6) ahead of **Inkling (Xhigh)** (#50, 1080.2) |
| **Tau3-Banking Agentic Benchmark** | **2** | **DeepSeek V4 Flash Vision (Max)** (#10, 0.41) ahead of **DeepSeek V4 Pro 0813 (Max)** (#11, 0.396); **Qwen3.5 122B A10B (Reasoning)** (#38, 0.153) ahead of **Qwen3.5 397B A17B (Reasoning)** (#44, 0.134) |
| **EvalPlus MBPP+ (35x Tests)** | **2** | **DeepSeek-V2.5 (Nov 2024)** (#6, 74.1) ahead of **DeepSeek-V3 (Nov 2024)** (#9, 73.0); **GPT-4-Turbo (Nov 2023)** (#7, 73.3) ahead of **GPT 4o (Aug 2024)** (#10, 72.2) |
| **SWE-bench Verified Total Run Cost ($ USD)** | **2** | **GPT 4.1 mini** ($217.58) cost more than **GPT 4.1** ($73.16); **GPT 5 nano (medium)** ($19.04) cost more than **GPT 5 mini (medium)** ($17.74) |
| **LiveBench 2.0 — Browser** | **2** | **claude-sonnet-5.5** (#5, 89.3) ahead of **claude-opus-5.5** (#6, 88.4); **grok-4.6** (#18, 49.4) ahead of **grok-4.7** (#20, 49.3) |
| **LiveBench 2.0 — Reasoning** | **2** | **grok-4.6** (#7, 91.2) ahead of **grok-4.7** (#20, 82.7); **gpt-5.6-terra** (#10, 90.6) ahead of **gpt-6.1-terra** (#15, 88.7) |
| **AA-AnalystAgent Data Analyst** | **2** | **Claude Sonnet 5.5** (#2, 0.575) ahead of **Claude Opus 5.5** (#3, 0.562); **Inkling Small** (#17, 0.275) ahead of **Inkling (Xhigh)** (#19, 0.237) |
| **AA-Briefcase v1.1 — Wall-Clock Time per Task (Sec)** | **2** | **GPT-6 Astra (Max)** (#11, 870.2s) faster than **GPT-6 Luna (Max)** (#12, 922.0s); **Claude Opus 5.5** (#21, 2225.4s) faster than **Claude Sonnet 5.5** (#23, 2844.5s) |
| **GDP.pdf Document — Wall-Clock Time per Task (Sec)** | **2** | **GPT-6 Astra (Max)** (#11, 117.1s) faster than **GPT-6 Luna (Max)** (#20, 208.1s); **GPT-6.1 Sol (Max)** (#12, 132.9s) faster than **GPT-6.1 Terra (Max)** (#14, 150.5s) |
| **HLE-Diamond — Wall-Clock Time per Task (Sec)** | **2** | **GPT-6 Astra (Max)** (#3, 138.0s) faster than **GPT-6 Luna (Max)** (#14, 248.6s); **GPT-6.1 Sol (Max)** (#5, 147.5s) faster than **GPT-6.1 Terra (Max)** (#15, 297.2s) |
| **Terminal-Bench 4.0 — Wall-Clock Time per Task (Sec)** | **2** | **GPT-6 Astra (Max)** (#8, 958.5s) faster than **GPT-6 Luna (Max)** (#10, 1181.4s); **Claude Opus 5.5** (#16, 1665.0s) faster than **Claude Sonnet 5.5** (#17, 1740.0s) |
| **AA-3D Interactive WebGL Elo** | **2** | **Claude Sonnet 5.5** (#1, 1198.8) ahead of **Claude Opus 5.5** (#2, 1196.4); **GLM-5.3-Flash** (#14, 936.6) ahead of **GLM-5.3 (Max)** (#16, 783.0) |
| **OpenAI HealthBench Medical Reasoning** | **2** | **Claude Sonnet 5.5** (#1, 0.621) ahead of **Claude Opus 5.5** (#6, 0.57); **Claude Haiku 5.5 (Max)** (#3, 0.585) ahead of **Claude Opus 5.5** (#6, 0.57) |
| **AA v4 CritPt Physics (Aug 2026)** | **3** | **Gemini 3.5 Flash** (#24, 0.131) ahead of **Gemini 3.6 Flash** (#30, 0.106); **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#25, 0.126) ahead of **Claude Opus 4.7 (Adaptive Reasoning, Max Effort)** (#26, 0.12); **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#33, 0.166) ahead of **DeepSeek V4 Pro (Reasoning, Max Effort)** (#40, 0.129) |
| **AA v4 Intelligence Index (Aug 2026)** | **3** | **Gemini 3.5 Flash** (#21, 52.0) ahead of **Gemini 3.6 Flash** (#23, 51.6); **Claude Sonnet 4.6 (Adaptive Reasoning, Max Effort)** (#24, 48.4) ahead of **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#32, 44.9); **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#32, 51.8) ahead of **DeepSeek V4 Pro (Reasoning, Max Effort)** (#50, 45.3) |
| **LMSYS Arena Math** | **3** | **qwen3-32b** (#6, 1387.3) ahead of **qwen3-235b-a22b** (#9, 1372.4); **gemini-2.0-flash-thinking-exp-01-21** (#13, 1357.3) ahead of **gemini-2.0-pro-exp-02-05** (#18, 1348.7); **gemini-2.5-flash-preview-05-20** (#2, 1435.2) ahead of **gemini-2.5-pro-exp-03-25** (#3, 1434.6) |
| **AA v4 Coding Index (Aug 2026)** | **3** | **Gemini 3.5 Flash** (#19, 70.1) ahead of **Gemini 3.6 Flash** (#20, 69.2); **DeepSeek V4 Flash 0731 (Reasoning, Max Effort)** (#21, 69.1) ahead of **DeepSeek V4 Pro 0813 (Reasoning, Max Effort)** (#22, 68.8); **Inkling Small** (#45, 52.9) ahead of **Inkling (xhigh)** (#50, 52.1) |
| **AA v4 Terminal-Bench (Aug 2026)** | **3** | **Gemini 3.5 Flash** (#19, 0.786) ahead of **Gemini 3.6 Flash** (#23, 0.775); **Qwen3.6 Plus** (#41, 0.614) ahead of **Qwen3.7 Plus** (#42, 0.611); **GPT-5.4 nano (xhigh)** (#43, 0.607) ahead of **GPT-5.4 mini (xhigh)** (#46, 0.592) |
| **AA-Omniscience Raw Accuracy** | **3** | **Muse Spark Open (Xhigh)** (#15, 0.42) ahead of **Muse Wonder Full (Max)** (#16, 0.41); **Muse Spark Open (Xhigh)** (#15, 0.42) ahead of **Muse Wonder (Max)** (#20, 0.38); **Granite 4.2 8B** (#47, 0.118) ahead of **Granite 4.2 30B** (#48, 0.112) |
| **HLE-Diamond (Humanity's Last Exam)** | **3** | **DeepSeek V4 Flash Vision (Max)** (#22, 0.211) ahead of **DeepSeek V4 Pro 0813 (Max)** (#24, 0.195); **GLM-5.3-Flash** (#25, 0.182) ahead of **GLM-5.3 (Max)** (#26, 0.179); **Inkling Small** (#40, 0.121) ahead of **Inkling (Xhigh)** (#44, 0.106) |
| **FrontierCode 1.0** | **3** | **Muse Wonder (Max)** (#6, 0.465) ahead of **Muse Wonder Full (Max)** (#9, 0.449); **GLM-5.3-Flash** (#16, 0.41) ahead of **GLM-5.3 (Max)** (#17, 0.401); **GPT-6.1 Terra (Medium)** (#18, 0.437) ahead of **GPT-6.1 Sol (Medium)** (#22, 0.433) |
| **AutomationBench-AA SaaS Workflows** | **3** | **Claude Sonnet 5.5** (#5, 0.718) ahead of **Claude Opus 5.5** (#7, 0.695); **MiMo-V2.6-Flash** (#14, 0.64) ahead of **MiMo-V2.6-Pro** (#21, 0.586); **Claude Sonnet 5.5 (Xhigh, Default Fallback)** (#16, 0.655) ahead of **Claude Opus 5.5 (Xhigh, Default Fallback)** (#17, 0.649) |
| **Arena.ai Text-to-Video Generation** | **3** | **dreamina-seedance-2.0-720p** (#5, 1479.0) ahead of **dreamina-seedance-2.5-720p** (#7, 1474.0); **veo-3-fast-audio** (#16, 1348.0) ahead of **veo-3-audio** (#19, 1340.0); **veo-3-fast-audio** (#16, 1348.0) ahead of **veo-3** (#23, 1254.0) |
| **AA v4 Output Speed (Tokens/Sec, Aug 2026)** | **3** | **Qwen3 Next 80B A3B (Reasoning)** (#19, 203.1 tok/s) faster than **Qwen3 30B A3B 2507 (Reasoning)** (#44, 148.6 tok/s); **GPT-5.4 mini (xhigh)** (#24, 189.5 tok/s) faster than **GPT-5.4 nano (xhigh)** (#29, 172.8 tok/s); **GPT-5.4 mini (Non-Reasoning)** (#36, 186.4 tok/s) faster than **GPT-5.4 nano (Non-Reasoning)** (#44, 177.6 tok/s) |
| **LiveBench 2.0 — Design** | **3** | **gpt-6-luna** (#6, 82.5) ahead of **gpt-6-astra** (#9, 82.0); **gpt-6.1-terra** (#7, 82.3) ahead of **gpt-6.1-sol** (#8, 82.1); **grok-4.6** (#10, 79.8) ahead of **grok-4.7** (#13, 78.0) |
| **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | **3** | **GPT-6.1 Sol (Max)** (#9, 24.7s) faster than **GPT-6.1 Terra (Max)** (#23, 86.4s); **GPT-6 Astra (Max)** (#10, 24.7s) faster than **GPT-6 Luna (Max)** (#16, 39.1s); **Claude Opus 5.5** (#20, 61.4s) faster than **Claude Sonnet 5.5** (#22, 68.9s) |
| **AutomationBench-AA — Wall-Clock Time per Task (Sec)** | **3** | **Muse Wonder (Max)** (#5, 130.1s) faster than **Muse Spark Open (Xhigh)** (#12, 209.9s); **GPT-6 Astra (Max)** (#8, 163.4s) faster than **GPT-6 Luna (Max)** (#18, 285.2s); **Claude Opus 5.5** (#14, 270.6s) faster than **Claude Sonnet 5.5** (#15, 277.1s) |
| **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | **3** | **GPT-6 Astra (Max)** (#8, 469.8s) faster than **GPT-6 Luna (Max)** (#12, 585.3s); **GPT-6.1 Sol (Max)** (#10, 543.6s) faster than **GPT-6.1 Terra (Max)** (#14, 694.3s); **Claude Opus 5.5** (#20, 1316.4s) faster than **Claude Sonnet 5.5** (#22, 1437.7s) |
| **LiveBench v1 — Mathematics** | **4** | **gemini-3.7-flash-high** (#19, 93.5) ahead of **gemini-3.8-flash-high** (#25, 91.6); **claude-opus-4-5-20251101-thinking-64k-high-effort** (#31, 90.4) ahead of **claude-opus-4-6-thinking-auto-high-effort** (#35, 89.3); **glm-5.2** (#33, 89.8) ahead of **glm-5.3** (#41, 87.9) *(+1 more)* |
| **Aider Polyglot Coding (Pass@1 %)** | **4** | **claude-3-7-sonnet-20250219** (#10, 29.3) ahead of **claude-sonnet-4-20250514** (#15, 25.8); **o3-mini** (#22, 21.0) ahead of **o4-mini** (#27, 19.6); **claude-3-7-sonnet-20250219** (#18, 29.3) ahead of **claude-sonnet-4-20250514 (no thinking)** (#37, 20.4) *(+1 more)* |
| **Aider Polyglot Coding (Pass@2 %)** | **4** | **claude-3-7-sonnet-20250219** (#11, 64.9) ahead of **claude-sonnet-4-20250514** (#14, 61.3); **gpt-4.1** (#23, 52.4) ahead of **gpt-4.5-preview** (#27, 44.9); **claude-3-7-sonnet-20250219** (#19, 64.9) ahead of **claude-sonnet-4-20250514 (no thinking)** (#28, 56.4) *(+1 more)* |
| **MLCR-AA Medical Long-Context** | **4** | **Claude Sonnet 5.5** (#1, 0.417) ahead of **Claude Opus 5.5** (#9, 0.278); **Claude Haiku 5.5 (Max)** (#5, 0.35) ahead of **Claude Opus 5.5** (#9, 0.278); **Qwen3.8-Flash-Next** (#15, 0.206) ahead of **Qwen3.8 Max (0902)** (#17, 0.2) *(+1 more)* |
| **CritPt v2 Hard — Wall-Clock Time per Task (Sec)** | **4** | **GPT-6 Astra (Max)** (#3, 231.3s) faster than **GPT-6 Luna (Max)** (#10, 408.8s); **GPT-6.1 Sol (Max)** (#4, 257.7s) faster than **GPT-6.1 Terra (Max)** (#9, 391.1s); **Muse Wonder (Max)** (#11, 471.4s) faster than **Muse Spark Open (Xhigh)** (#12, 482.5s) *(+1 more)* |
| **AA v4 Omniscience (Aug 2026)** | **5** | **Muse Spark 1.1 (xhigh)** (#6, 28.1) ahead of **Muse Spark 1.2 (xhigh)** (#8, 27.2); **Claude Opus 4.5 (Reasoning)** (#20, 14.0) ahead of **Claude Opus 4.6 (Adaptive Reasoning, Max Effort)** (#21, 13.7); **Qwen3.7 Max** (#22, 13.5) ahead of **Qwen3.8 Max** (#39, 3.4) *(+2 more)* |
| **AA v4 Humanity's Last Exam (Aug 2026)** | **5** | **Muse Spark 1.1 (xhigh)** (#8, 0.462) ahead of **Muse Spark 1.2 (xhigh)** (#10, 0.455); **Gemini 3.5 Flash** (#15, 0.427) ahead of **Gemini 3.6 Flash** (#23, 0.408); **Inkling Small** (#49, 0.333) ahead of **Inkling (xhigh)** (#50, 0.319) *(+2 more)* |
| **SWE-bench Lite (All Submissions)** | **5** | **GPT 4 (0806)** (#22, 39.7) ahead of **GPT 4o** (#25, 38.0); **GPT 4 (0806)** (#28, 39.7) ahead of **GPT 4o** (#38, 34.0); **GPT 4 (0806)** (#28, 39.7) ahead of **GPT 4o** (#42, 32.0) *(+2 more)* |
| **FrontierCode 2.0** | **5** | **GPT-6.1 Terra (Max)** (#3, 0.423) ahead of **GPT-6.1 Sol (Max)** (#5, 0.406); **Inkling Small** (#34, 0.048) ahead of **Inkling (Xhigh)** (#35, 0.039); **GPT-6.1 Terra** (#12, 0.375) ahead of **GPT-6.1 Sol** (#14, 0.367) *(+2 more)* |
| **AA v4 Latency TTFT (Seconds, Aug 2026)** | **5** | **Phi-4 Multimodal Instruct** (#20, 0.8s) faster than **Phi-4 Mini Instruct** (#24, 0.9s); **GPT-4o (Nov '24)** (#22, 0.9s) faster than **GPT-4o mini** (#29, 0.9s); **gpt-oss-120b** (#23, 0.9s) faster than **gpt-oss-20b** (#32, 1.0s) *(+2 more)* |
| **AA Long-Context Reasoning (LCR)** | **5** | **GPT-6 Luna (Max)** (#7, 0.833) ahead of **GPT-6 Astra (Max)** (#25, 0.807); **Muse Glimmer** (#8, 0.833) ahead of **Muse Wonder (Max)** (#26, 0.807); **DeepSeek V4 Flash Vision (Max)** (#24, 0.813) ahead of **DeepSeek V4 Pro 0813 (Max)** (#27, 0.803) *(+2 more)* |
| **AA Time to First Token (TTFT Seconds)** | **5** | **Inkling (xhigh)** (#8, 0.5s) faster than **Inkling Small** (#14, 0.6s); **Qwen3.5 9B** (#16, 0.7s) faster than **Qwen3.5 4B** (#31, 0.9s); **MiMo-V2.6-Pro** (#17, 0.7s) faster than **MiMo-V2.6-Flash** (#35, 0.9s) *(+2 more)* |
| **LiveBench v1 Global Average** | **6** | **gpt-5.6-sol-max** (#9, 81.1) ahead of **gpt-6-sol-max** (#13, 79.2); **gemini-3.7-flash-high** (#15, 78.8) ahead of **gemini-3.8-flash-high** (#32, 75.8); **claude-opus-4-7-xhigh-effort** (#27, 76.5) ahead of **claude-opus-4-8-max-effort** (#28, 76.2) *(+3 more)* |
| **Arena.ai Coding (108-Model Full Table)** | **6** | **deepseek-v4-flash-high** (#6, 1586.0) ahead of **deepseek-v4-pro-high-preview** (#29, 1465.0); **gpt-5.6-luna-xhigh (codex-harness)** (#15, 1524.0) ahead of **gpt-5.6-terra-xhigh (codex-harness)** (#17, 1521.0); **gpt-5.2** (#40, 1419.0) ahead of **gpt-5.3-codex (codex-harness)** (#43, 1409.0) *(+3 more)* |
| **AA Output Speed (Median Tokens/Sec)** | **6** | **Nemotron 3 Ultra** (#9, 351.8 tok/s) faster than **Nemotron 3 Nano** (#14, 293.5 tok/s); **Nemotron 3 Ultra** (#9, 351.8 tok/s) faster than **Nemotron 3 Nano Omni 30B A3B** (#21, 230.5 tok/s); **Llama 4 Maverick** (#12, 311.7 tok/s) faster than **Llama 4 Scout** (#37, 154.2 tok/s) *(+3 more)* |
| **Aider Polyglot Latency (Seconds per Case)** | **6** | **gpt-4o-2024-11-20** (#4, 12.1s) faster than **gpt-4o-mini-2024-07-18** (#8, 17.3s); **claude-3-5-sonnet-20241022** (#13, 21.4s) faster than **claude-3-5-haiku-20241022** (#17, 31.8s); **Qwen3 235B A22B diff, no think, Alibaba API** (#25, 45.4s) faster than **Qwen3 32B** (#48, 372.2s) *(+3 more)* |
| **AA Median Reasoning Time (Seconds)** | **6** | **gpt-oss-120b** (#7, 9.7s) faster than **gpt-oss-20b** (#22, 14.0s); **Muse Wonder (Max)** (#21, 14.0s) faster than **Muse Spark Open (Xhigh)** (#24, 14.4s); **Muse Wonder (Max)** (#21, 14.0s) faster than **Muse Glimmer** (#33, 18.8s) *(+3 more)* |
| **AA v4 SciCode (Aug 2026)** | **7** | **Muse Spark 1.1 (xhigh)** (#4, 0.582) ahead of **Muse Spark 1.2 (xhigh)** (#7, 0.564); **GPT-5.4 (xhigh)** (#6, 0.566) ahead of **GPT-5.5 (xhigh)** (#9, 0.561); **GPT-5.2 Codex (xhigh)** (#12, 0.546) ahead of **GPT-5.3 Codex (xhigh)** (#20, 0.532) *(+4 more)* |
| **Tau2-Bench Tool-Use Agentic** | **7** | **Qwen3.5 4B (Reasoning)** (#11, 0.921) ahead of **Qwen3.5 9B (Reasoning)** (#19, 0.868); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 9B (Non-reasoning)** (#24, 0.851); **Qwen3.5 4B (Non-reasoning)** (#18, 0.877) ahead of **Qwen3.5 122B A10B (Non-reasoning)** (#26, 0.845) *(+4 more)* |
| **AA Time to First Answer Token (Seconds)** | **7** | **Ministral 3 8B** (#8, 0.8s) faster than **Ministral 3 3B** (#9, 0.9s); **Nemotron 3 Ultra** (#33, 7.5s) faster than **Nemotron 3 Nano Omni 30B A3B** (#36, 9.6s); **MiMo-V2.6-Pro** (#34, 8.1s) faster than **MiMo-V2.6-Flash** (#41, 12.9s) *(+4 more)* |
| **LiveBench v1 — Reasoning** | **8** | **gpt-5.6-sol-max** (#5, 91.7) ahead of **gpt-6-sol-max** (#21, 88.7); **muse-spark-1.2-xhigh** (#13, 90.0) ahead of **muse-spark-1.3-xhigh** (#16, 89.7); **claude-opus-4-6-thinking-auto-high-effort** (#20, 88.7) ahead of **claude-opus-4-7-xhigh-effort** (#27, 87.2) *(+5 more)* |
| **LiveBench v1 — Agentic Coding** | **8** | **deepseek-v4-flash-vision-exp** (#5, 65.1) ahead of **deepseek-v4-pro-0813** (#29, 54.9); **claude-sonnet-5-xhigh-effort** (#17, 59.4) ahead of **claude-sonnet-5-5-max-effort** (#27, 56.3); **muse-spark-1.1-xhigh** (#18, 58.5) ahead of **muse-spark-1.2-xhigh** (#20, 57.6) *(+5 more)* |
| **AA v4 Tau-Bench Banking (Aug 2026)** | **8** | **GPT-5.4 (xhigh)** (#9, 0.396) ahead of **GPT-5.5 (xhigh)** (#12, 0.39); **Claude Opus 4.7 (Adaptive Reasoning, Max Effort)** (#17, 0.346) ahead of **Claude Opus 4.8 (Adaptive Reasoning, Max Effort)** (#20, 0.342); **Gemini 3.5 Flash** (#22, 0.322) ahead of **Gemini 3.6 Flash** (#25, 0.299) *(+5 more)* |
| **Arena.ai Document Comprehension** | **8** | **claude-opus-4-6-high** (#3, 1507.0) ahead of **claude-opus-4-7-high** (#5, 1495.0); **claude-opus-4-6-high** (#3, 1507.0) ahead of **claude-opus-4-8-high** (#9, 1475.0); **claude-opus-4-7-high** (#5, 1495.0) ahead of **claude-opus-4-8-high** (#9, 1475.0) *(+5 more)* |
| **Arena.ai Vision Multimodal (30-Model Table)** | **8** | **claude-opus-4-7-thinking** (#2, 1304.0) ahead of **claude-opus-5-high** (#5, 1299.0); **claude-opus-4-7-thinking** (#2, 1304.0) ahead of **claude-opus-4-8-thinking** (#8, 1286.0); **claude-opus-4-6-thinking** (#4, 1300.0) ahead of **claude-opus-5-high** (#5, 1299.0) *(+5 more)* |
| **Arena.ai Text Overall (Oct 2026)** | **8** | **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5.5-high** (#4, 1504.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-4-7-high** (#5, 1501.0); **claude-opus-4-6-high** (#2, 1505.0) ahead of **claude-opus-5-max** (#11, 1489.0) *(+5 more)* |
| **Arena.ai Vision Multimodal (Oct 2026)** | **8** | **claude-fable-5-high** (#1, 1309.0) ahead of **claude-fable-5.1-max** (#13, 1288.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-4-7-high** (#4, 1298.0); **claude-opus-4-6-high** (#3, 1299.0) ahead of **claude-opus-5-high** (#12, 1289.0) *(+5 more)* |
| **Arena.ai Text Overall (50-Model Snapshot)** | **9** | **claude-opus-4-6-thinking** (#2, 1504.0) ahead of **claude-opus-4-7-thinking** (#3, 1502.0); **claude-opus-4-6-thinking** (#2, 1504.0) ahead of **claude-opus-4-8-thinking** (#7, 1483.0); **claude-opus-4-7-thinking** (#3, 1502.0) ahead of **claude-opus-4-8-thinking** (#7, 1483.0) *(+6 more)* |
| **AA End-to-End Response Time (Seconds)** | **9** | **Llama 4 Maverick** (#5, 2.9s) faster than **Llama 4 Scout** (#10, 3.9s); **Phi-4** (#16, 5.9s) faster than **Phi-4 Mini** (#33, 11.9s); **Nemotron 3 Ultra** (#27, 8.9s) faster than **Nemotron 3 Nano Omni 30B A3B** (#32, 11.8s) *(+6 more)* |
| **SWE-bench Verified Agent Calls per Issue** | **9** | **GPT 5 (medium)** (#1, 13.2) faster than **GPT 5 mini (medium)** (#2, 14.5); **GPT 5 (medium)** (#1, 13.2) faster than **GPT 5 nano (medium)** (#19, 39.8); **GPT 5 mini (medium)** (#2, 14.5) faster than **GPT 5 nano (medium)** (#19, 39.8) *(+6 more)* |
| **Aider Code Editing Leaderboard** | **10** | **gpt-4-0613** (#17, 67.7) ahead of **gpt-4-0125-preview** (#20, 66.2); **Qwen2.5-Coder-14B-Instruct** (#19, 69.2) ahead of **openrouter/qwen/qwen-2.5-coder-32b-instruct** (#32, 65.4); **gpt-4-0613** (#22, 67.7) ahead of **gpt-4-1106-preview** (#28, 65.4) *(+7 more)* |
| **Arena.ai Search & Grounding** | **10** | **claude-opus-4-6-search** (#2, 1253.0) ahead of **claude-opus-4-7** (#4, 1233.0); **claude-opus-4-6-search** (#2, 1253.0) ahead of **claude-opus-4-8** (#12, 1204.0); **claude-opus-4-7** (#4, 1233.0) ahead of **claude-opus-4-8** (#12, 1204.0) *(+7 more)* |
| **SWE-bench Verified (All Submissions)** | **11** | **Claude 4 Sonnet** (#4, 76.8) ahead of **Claude 4 Opus** (#16, 73.2); **Claude 4.5 Opus** (#1, 79.2) ahead of **Claude 4.6 Opus** (#12, 75.6); **Claude 4 Sonnet** (#5, 76.8) ahead of **Claude 4.5 Sonnet** (#15, 74.8) *(+8 more)* |
| **LiveBench v1 — Language** | **12** | **claude-fable-5-max-effort** (#1, 90.7) ahead of **claude-fable-5-1-max-effort** (#3, 89.5); **claude-opus-5-max-effort** (#5, 88.7) ahead of **claude-opus-5-5-max-effort** (#9, 86.3); **gpt-5.6-sol-max** (#7, 87.7) ahead of **gpt-6-sol-max** (#13, 85.3) *(+9 more)* |
| **LiveBench v1 — Data Analysis** | **12** | **claude-fable-5-max-effort** (#6, 80.5) ahead of **claude-fable-5-1-max-effort** (#8, 80.3); **deepseek-v4-flash-vision-exp** (#12, 79.5) ahead of **deepseek-v4-pro-0813** (#16, 79.2); **claude-opus-4-7-xhigh-effort** (#22, 78.3) ahead of **claude-opus-5-max-effort** (#34, 74.6) *(+9 more)* |
| **AA-Omniscience Non-Hallucination Rate** | **12** | **Gemini 4 Argon** (#1, 0.957) ahead of **Gemini 4 Carbon** (#2, 0.886); **Granite 4.2 3B** (#15, 0.697) ahead of **Granite 4.2 8B** (#18, 0.678); **Claude Haiku 5.5 (Max)** (#19, 0.658) ahead of **Claude Sonnet 5.5** (#29, 0.567) *(+9 more)* |
| **LiveBench v1 — IF** | **13** | **qwen3.8-flash-next** (#5, 77.1) ahead of **qwen3.8-max** (#13, 74.1); **claude-fable-5-max-effort** (#6, 75.8) ahead of **claude-fable-5-1-max-effort** (#18, 73.0); **gemini-3.5-flash-high** (#7, 75.6) ahead of **gemini-3.6-flash-high** (#9, 75.4) *(+10 more)* |
| **LiveBench v1 — Coding** | **14** | **claude-sonnet-5-5-max-effort** (#1, 91.4) ahead of **claude-opus-5-5-max-effort** (#2, 89.3); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6-sol-max** (#12, 81.8); **gpt-5.6-sol-max** (#5, 83.9) ahead of **gpt-6.1-sol-max** (#19, 80.4) *(+11 more)* |

</details>
