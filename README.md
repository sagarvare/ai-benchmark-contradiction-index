# AI Benchmark Contradiction Index

A single, equal-weighted meta-benchmark measuring how frequently the **Top 25 ranked models** on AI leaderboards violate intra-family scaling laws.

> [!IMPORTANT]
> **Single Shareable Table & App (`popular_benchmarks` vs `ALL`)**:
> - **Interactive Web Table**: [index.html](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/index.html) ([app.js](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/app.js), [styles.css](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/styles.css), [data.js](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/data.js))
> - **Single-File Zero-Dependency Bundle (Drop Anywhere to Host/Share)**: [shareable_table.html](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/shareable_table.html)
> - **Generator & Taxonomy**: [generate_all_benchmarks_data.py](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/generate_all_benchmarks_data.py), [compute_contradictions.py](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/compute_contradictions.py), [model_taxonomy.py](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/model_taxonomy.py)

---

## 1. Equal-Weighted Contradiction Score Rule

Every model in a benchmark's **Top 25** is parsed into $(\text{Family}, \text{Version}, \text{Size Tier})$. Two models in the Top 25 are **comparable** if and only if they belong to the same model family and differ along **strictly one axis** (all comparable pairs are **weighted equally**):

- **Intra-Version Size Tier** (same version, different size class): e.g., `GPT-6.1 Sol > GPT-6.1 Terra > GPT-6.1 Luna`, `Claude Opus 5.5 > Sonnet 5.5 > Haiku 5.5`, `Gemini 4 Carbon > Argon`.
- **Inter-Version Same-Tier** (same size class, different version): e.g., `GPT-6.1 Sol > GPT-6.0 Sol > GPT-5.6 Sol`, `Claude Opus 5.5 > Opus 4.7 > Opus 4.6`.
- **Cross-Axis Exclusion**: Crossed pairs (`GPT-6.1 Sol` vs `GPT-6.0 Luna`) are **never** compared.
- **Expected Polarity**:
  - **Quality**: Larger tier / newer generation scores higher (`Sol >= Terra >= Luna`, `6.1 Sol >= 6.0 Sol`).
  - **Latency / Speed**: **100% flipped** (`Luna` faster / lower latency than `Terra` faster than `Sol`).
  - **Cost (Unit & Total Benchmark Run Cost)**: Larger tier costs at least as much as smaller tier (`Cost(Sol) >= Cost(Terra) >= Cost(Luna)`).

$$\text{Contradiction Score} = \frac{\text{Contradicted Top-25 Pairs}}{\text{Comparable Top-25 Pairs}} \times 100\%$$

---

## 2. View 1: `popular_benchmarks` (44 Flagship Benchmarks — 18.9% Mean Contradiction, `64 / 339` Pairs)

| # | Benchmark | Suite | Polarity | Contradiction Score | Inverted / Pairs | Top-25 Inversions (Actual vs. Expected) |
| :-: | :--- | :--- | :-: | :-: | :-: | :--- |
| 1 | **Arena.ai Vision Multimodal (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **66.7%** | `8 / 12` | `claude-fable-5-high (#1, 1309.0) > claude-fable-5.1-max (#13, 1288.0)` · `claude-opus-4-6-high (#3, 1299.0) > claude-opus-4-7-high (#4, 1298.0)` *(+6 more)* |
| 2 | **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **60.0%** | `3 / 5` | `GPT-6 Astra (Max) (#8, 469.8s) faster than GPT-6 Luna (Max) (#12, 585.3s)` · `GPT-6.1 Sol (Max) (#10, 543.6s) faster than GPT-6.1 Terra (Max) (#14, 694.3s)` *(+1 more)* |
| 3 | **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **60.0%** | `3 / 5` | `GPT-6.1 Sol (Max) (#9, 24.7s) faster than GPT-6.1 Terra (Max) (#23, 86.4s)` · `GPT-6 Astra (Max) (#10, 24.7s) faster than GPT-6 Luna (Max) (#16, 39.1s)` *(+1 more)* |
| 4 | **Arena.ai Text Overall (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **50.0%** | `5 / 10` | `claude-opus-4-6-high (#2, 1505.0) > claude-opus-5.5-high (#4, 1504.0)` · `claude-opus-4-6-high (#2, 1505.0) > claude-opus-4-7-high (#5, 1501.0)` *(+3 more)* |
| 5 | **OpenAI HealthBench Medical Reasoning** | Artificial Analysis v5 | Quality | **50.0%** | `2 / 4` | `Claude Sonnet 5.5 (#1, 0.621) > Claude Opus 5.5 (#6, 0.57)` · `Claude Haiku 5.5 (Max) (#3, 0.585) > Claude Opus 5.5 (#6, 0.57)` |
| 6 | **MLCR-AA Medical Long-Context** | Artificial Analysis v5 | Quality | **42.9%** | `3 / 7` | `Claude Sonnet 5.5 (#1, 0.417) > Claude Opus 5.5 (#9, 0.278)` · `Claude Haiku 5.5 (Max) (#5, 0.35) > Claude Opus 5.5 (#9, 0.278)` *(+1 more)* |
| 7 | **LiveBench 2.0 — Design** | LiveBench 2.0 (Oct 2026) | Quality | **42.9%** | `3 / 7` | `gpt-6-luna (#6, 82.5) > gpt-6-astra (#9, 82.0)` · `gpt-6.1-terra (#7, 82.3) > gpt-6.1-sol (#8, 82.1)` *(+1 more)* |
| 8 | **LiveBench v1 — Coding** | LiveBench v1 (2026) | Quality | **40.9%** | `9 / 22` | `claude-sonnet-5-5-max-effort (#1, 91.4) > claude-opus-5-5-max-effort (#2, 89.3)` · `gpt-5.6-sol-max (#5, 83.9) > gpt-6-sol-max (#12, 81.8)` *(+7 more)* |
| 9 | **AutomationBench-AA SaaS Workflows** | Artificial Analysis v5 | Quality | **40.0%** | `2 / 5` | `Claude Sonnet 5.5 (#5, 0.718) > Claude Opus 5.5 (#7, 0.695)` · `MiMo-V2.6-Flash (#14, 0.64) > MiMo-V2.6-Pro (#21, 0.586)` |
| 10 | **Aider Polyglot Latency (Seconds per Case)** | Aider Coding | Latency (Flip) | **33.3%** | `2 / 6` | `gpt-4o-2024-11-20 (#4, 12.1s) faster than gpt-4o-mini-2024-07-18 (#8, 17.3s)` · `claude-3-5-sonnet-20241022 (#13, 21.4s) faster than claude-3-5-haiku-20241022 (#17, 31.8s)` |
| 11 | **LiveBench 2.0 — Reasoning** | LiveBench 2.0 (Oct 2026) | Quality | **28.6%** | `2 / 7` | `grok-4.6 (#7, 91.2) > grok-4.7 (#20, 82.7)` · `gpt-5.6-terra (#10, 90.6) > gpt-6.1-terra (#15, 88.7)` |
| 12 | **LiveBench 2.0 — Browser** | LiveBench 2.0 (Oct 2026) | Quality | **28.6%** | `2 / 7` | `claude-sonnet-5.5 (#5, 89.3) > claude-opus-5.5 (#6, 88.4)` · `grok-4.6 (#18, 49.4) > grok-4.7 (#20, 49.3)` |
| 13 | **FrontierCode 2.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **25.0%** | `1 / 4` | `GPT-6.1 Terra (Max) ($1.29) > GPT-6.1 Sol (Max) ($1.13)` |
| 14 | **LiveBench 2.0 Cost — Coding ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **25.0%** | `1 / 4` | `gpt-6.1-terra ($24.97) > gpt-6.1-sol ($13.98)` |
| 15 | **SWE-bench Verified (All Submissions)** | SWE-bench | Quality | **25.0%** | `1 / 4` | `Claude 4 Sonnet (#4, 76.8) > Claude 4 Opus (#16, 73.2)` |
| 16 | **AA Intelligence Index Time per Task (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **20.0%** | `1 / 5` | `Claude Opus 5.5 (#19, 1140.8s) faster than Claude Sonnet 5.5 (#21, 1298.5s)` |
| 17 | **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **20.0%** | `1 / 5` | `GPT-6.1 Terra (Max) ($0.043) > GPT-6.1 Sol (Max) ($0.018)` |
| 18 | **Arena.ai Coding (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **20.0%** | `1 / 5` | `mimo-v2.6-flash (#13, 1636.0) > mimo-v2.6-pro (#16, 1630.0)` |
| 19 | **SciCode Scientific Coding** | Artificial Analysis v5 | Quality | **16.7%** | `1 / 6` | `GPT-6.1 Terra (Max) (#18, 0.551) > GPT-6.1 Sol (Max) (#21, 0.542)` |
| 20 | **AA Long-Context Reasoning (LCR)** | Artificial Analysis v5 | Quality | **16.7%** | `1 / 6` | `GPT-6 Luna (Max) (#7, 0.833) > GPT-6 Astra (Max) (#25, 0.807)` |
| 21 | **AA Time to First Answer Token (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **16.7%** | `1 / 6` | `Ministral 3 8B (#8, 0.8s) faster than Ministral 3 3B (#9, 0.9s)` |
| 22 | **Tau2-Bench Tool-Use Agentic** | Artificial Analysis v5 | Quality | **14.3%** | `1 / 7` | `Qwen3.5 4B (Reasoning) (#11, 0.921) > Qwen3.5 9B (Reasoning) (#19, 0.868)` |
| 23 | **LiveBench 2.0 — Coding** | LiveBench 2.0 (Oct 2026) | Quality | **14.3%** | `1 / 7` | `grok-4.6 (#12, 89.1) > grok-4.7 (#18, 84.5)` |
| 24 | **FrontierCode 2.0** | Artificial Analysis v5 | Quality | **12.5%** | `1 / 8` | `GPT-6.1 Terra (Max) (#3, 0.423) > GPT-6.1 Sol (Max) (#5, 0.406)` |
| 25 | **Terminal-Bench 4.0** | Artificial Analysis v5 | Quality | **12.5%** | `1 / 8` | `Claude Sonnet 5.5 (#3, 0.636) > Claude Opus 5.5 (#4, 0.596)` |
| 26 | **Aider Polyglot Coding (Pass@2 %)** | Aider Coding | Quality | **12.5%** | `1 / 8` | `claude-3-7-sonnet-20250219 (#11, 64.9) > claude-sonnet-4-20250514 (#14, 61.3)` |
| 27 | **Aider Code Editing Leaderboard** | Aider Coding | Quality | **12.5%** | `1 / 8` | `gpt-4-0613 (#17, 67.7) > gpt-4-0125-preview (#20, 66.2)` |
| 28 | **HLE-Diamond (Humanity's Last Exam)** | Artificial Analysis v5 | Quality | **11.1%** | `1 / 9` | `DeepSeek V4 Flash Vision (Max) (#22, 0.211) > DeepSeek V4 Pro 0813 (Max) (#24, 0.195)` |
| 29 | **AA-Briefcase v1.1 Knowledge Work** | Artificial Analysis v5 | Quality | **11.1%** | `1 / 9` | `Claude Sonnet 5.5 (#1, 1813.6) > Claude Opus 5.5 (#2, 1800.5)` |
| 30 | **LiveBench v1 Global Average** | LiveBench v1 (2026) | Quality | **8.3%** | `1 / 12` | `gpt-5.6-sol-max (#9, 81.1) > gpt-6-sol-max (#13, 79.2)` |
| 31 | **SWE-bench Verified (Bash-Only Standardized)** | SWE-bench | Quality | **7.7%** | `1 / 13` | `Gemini 3 Flash (#2, 75.8) > Gemini 3 Pro Preview (#5, 74.2)` |
| 32 | **LiveBench v1 — Mathematics** | LiveBench v1 (2026) | Quality | **5.6%** | `1 / 18` | `gemini-3.7-flash-high (#19, 93.5) > gemini-3.8-flash-high (#25, 91.6)` |
| 33 | **AA v4 GPQA Diamond (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **0.0%** | `0 / 16` | ✓ **100% Consistent** (`Grok 4.6 (#1) > Grok 4.5 (#9)`, `Grok 4.6 (#1) > Grok 4.20 0309 v2 (Reasoning) (#22)`) |
| 34 | **GDPval-AA Professional Work Elo** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`Claude Opus 5.5 (#1) > Claude Sonnet 5.5 (#4)`, `Claude Opus 5.5 (#1) > Claude Haiku 5.5 (Max) (#16)`) |
| 35 | **LMSYS Arena Hard Prompts** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#2)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#8)`) |
| 36 | **AA Intelligence Index v5.0** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`Gemini 4 Carbon (#1) > Gemini 4 Argon (#7)`, `Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#5)`) |
| 37 | **CritPt v2 Agentic Hard** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#1) > GPT-6 Luna (Max) (#13)`, `GPT-6.1 Sol (Max) (#2) > GPT-6.1 Terra (Max) (#3)`) |
| 38 | **LiveBench 2.0 Overall Score** | LiveBench 2.0 (Oct 2026) | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`gpt-6-astra (#2) > gpt-6-luna (#17)`, `claude-opus-5.5 (#3) > claude-sonnet-5.5 (#5)`) |
| 39 | **EvalPlus Combined Average** | EvalPlus | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`DeepSeek-V3 (Nov 2024) (#3) > DeepSeek-V2.5 (Nov 2024) (#5)`, `GPT 4o (Aug 2024) (#4) > GPT 4o Mini (July 2024) (#8)`) |
| 40 | **AA-Omniscience v1.1 Net Score** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Gemini 4 Carbon (#1) > Gemini 4 Argon (#4)`, `Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#9)`) |
| 41 | **CritPt Physics Reasoning** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Muse Wonder Full (Max) (#1) > Muse Wonder (Max) (#8)`, `GPT-6.1 Sol (Max) (#2) > GPT-6.1 Terra (Max) (#9)`) |
| 42 | **IFBench Instruction Following** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Nemotron 3 Ultra 550B A55B (Reasoning) (#2) > Nemotron Cascade 2 30B A3B (#3)`, `Qwen3.5 397B A17B (Reasoning) (#5) > Qwen3.5 122B A10B (Reasoning) (#8)`) |
| 43 | **AA API Blended Price (3:1 In:Out $/1M)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Sol (Daybreak Blue, max) (#14)`, `Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#11)`) |
| 44 | **AA Intelligence Index Total Run Cost ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#4)`, `Claude Opus 5.5 (#2) > Claude Haiku 5.5 (Max) (#23)`) |

---

## 3. View 2: `ALL` (143 Evaluated Benchmarks Across 9 Suites — 15.8% Mean Contradiction, `167 / 1,055` Pairs)

<details>
<summary><strong>Click to expand full 143-row table (ALL view)</strong></summary>

| # | Benchmark | Suite | Polarity | Contradiction Score | Inverted / Pairs | Top-25 Inversions (Actual vs. Expected) |
| :-: | :--- | :--- | :-: | :-: | :-: | :--- |
| 1 | **SWE-bench Verified Agent Calls per Issue** | SWE-bench | Latency (Flip) | **85.7%** | `6 / 7` | `GPT 5 (medium) (#1, 13.2) faster than GPT 5 mini (medium) (#2, 14.5)` · `GPT 5 (medium) (#1, 13.2) faster than GPT 5 nano (medium) (#19, 39.8)` *(+4 more)* |
| 2 | **Arena.ai Vision Multimodal (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **66.7%** | `8 / 12` | `claude-fable-5-high (#1, 1309.0) > claude-fable-5.1-max (#13, 1288.0)` · `claude-opus-4-6-high (#3, 1299.0) > claude-opus-4-7-high (#4, 1298.0)` *(+6 more)* |
| 3 | **AA Output Speed (Median Tokens/Sec)** | Artificial Analysis v5 | Latency (Flip) | **66.7%** | `2 / 3` | `Nemotron 3 Ultra (#9, 351.8s) faster than Nemotron 3 Nano (#14, 293.5s)` · `Nemotron 3 Ultra (#9, 351.8s) faster than Nemotron 3 Nano Omni 30B A3B (#21, 230.5s)` |
| 4 | **FrontierCode 2.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **60.0%** | `3 / 5` | `GPT-6 Astra (Max) (#8, 469.8s) faster than GPT-6 Luna (Max) (#12, 585.3s)` · `GPT-6.1 Sol (Max) (#10, 543.6s) faster than GPT-6.1 Terra (Max) (#14, 694.3s)` *(+1 more)* |
| 5 | **AA-Omniscience v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **60.0%** | `3 / 5` | `GPT-6.1 Sol (Max) (#9, 24.7s) faster than GPT-6.1 Terra (Max) (#23, 86.4s)` · `GPT-6 Astra (Max) (#10, 24.7s) faster than GPT-6 Luna (Max) (#16, 39.1s)` *(+1 more)* |
| 6 | **CritPt v2 Hard — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **60.0%** | `3 / 5` | `GPT-6 Astra (Max) (#3, 231.3s) faster than GPT-6 Luna (Max) (#10, 408.8s)` · `GPT-6.1 Sol (Max) (#4, 257.7s) faster than GPT-6.1 Terra (Max) (#9, 391.1s)` *(+1 more)* |
| 7 | **Arena.ai Text Overall (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **50.0%** | `5 / 10` | `claude-opus-4-6-high (#2, 1505.0) > claude-opus-5.5-high (#4, 1504.0)` · `claude-opus-4-6-high (#2, 1505.0) > claude-opus-4-7-high (#5, 1501.0)` *(+3 more)* |
| 8 | **OpenAI HealthBench Medical Reasoning** | Artificial Analysis v5 | Quality | **50.0%** | `2 / 4` | `Claude Sonnet 5.5 (#1, 0.621) > Claude Opus 5.5 (#6, 0.57)` · `Claude Haiku 5.5 (Max) (#3, 0.585) > Claude Opus 5.5 (#6, 0.57)` |
| 9 | **AA Median Reasoning Time (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **50.0%** | `1 / 2` | `gpt-oss-120b (#7, 9.7s) faster than gpt-oss-20b (#22, 14.0s)` |
| 10 | **MLCR-AA Medical Long-Context** | Artificial Analysis v5 | Quality | **42.9%** | `3 / 7` | `Claude Sonnet 5.5 (#1, 0.417) > Claude Opus 5.5 (#9, 0.278)` · `Claude Haiku 5.5 (Max) (#5, 0.35) > Claude Opus 5.5 (#9, 0.278)` *(+1 more)* |
| 11 | **LiveBench 2.0 — Design** | LiveBench 2.0 (Oct 2026) | Quality | **42.9%** | `3 / 7` | `gpt-6-luna (#6, 82.5) > gpt-6-astra (#9, 82.0)` · `gpt-6.1-terra (#7, 82.3) > gpt-6.1-sol (#8, 82.1)` *(+1 more)* |
| 12 | **LiveBench v1 — Coding** | LiveBench v1 (2026) | Quality | **40.9%** | `9 / 22` | `claude-sonnet-5-5-max-effort (#1, 91.4) > claude-opus-5-5-max-effort (#2, 89.3)` · `gpt-5.6-sol-max (#5, 83.9) > gpt-6-sol-max (#12, 81.8)` *(+7 more)* |
| 13 | **AutomationBench-AA SaaS Workflows** | Artificial Analysis v5 | Quality | **40.0%** | `2 / 5` | `Claude Sonnet 5.5 (#5, 0.718) > Claude Opus 5.5 (#7, 0.695)` · `MiMo-V2.6-Flash (#14, 0.64) > MiMo-V2.6-Pro (#21, 0.586)` |
| 14 | **AA-Omniscience Non-Hallucination Rate** | Artificial Analysis v5 | Quality | **40.0%** | `2 / 5` | `Gemini 4 Argon (#1, 0.957) > Gemini 4 Carbon (#2, 0.886)` · `Granite 4.2 3B (#15, 0.697) > Granite 4.2 8B (#18, 0.678)` |
| 15 | **AA-Briefcase v1.1 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **40.0%** | `2 / 5` | `GPT-6 Astra (Max) (#11, 870.2s) faster than GPT-6 Luna (Max) (#12, 922.0s)` · `Claude Opus 5.5 (#21, 2225.4s) faster than Claude Sonnet 5.5 (#23, 2844.5s)` |
| 16 | **AutomationBench-AA — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **40.0%** | `2 / 5` | `GPT-6 Astra (Max) (#8, 163.4s) faster than GPT-6 Luna (Max) (#18, 285.2s)` · `Claude Opus 5.5 (#14, 270.6s) faster than Claude Sonnet 5.5 (#15, 277.1s)` |
| 17 | **Terminal-Bench 4.0 — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **40.0%** | `2 / 5` | `GPT-6 Astra (Max) (#8, 958.5s) faster than GPT-6 Luna (Max) (#10, 1181.4s)` · `Claude Opus 5.5 (#16, 1665.0s) faster than Claude Sonnet 5.5 (#17, 1740.0s)` |
| 18 | **GDP.pdf Document — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **40.0%** | `2 / 5` | `GPT-6 Astra (Max) (#11, 117.1s) faster than GPT-6 Luna (Max) (#20, 208.1s)` · `GPT-6.1 Sol (Max) (#12, 132.9s) faster than GPT-6.1 Terra (Max) (#14, 150.5s)` |
| 19 | **HLE-Diamond — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **40.0%** | `2 / 5` | `GPT-6 Astra (Max) (#3, 138.0s) faster than GPT-6 Luna (Max) (#14, 248.6s)` · `GPT-6.1 Sol (Max) (#5, 147.5s) faster than GPT-6.1 Terra (Max) (#15, 297.2s)` |
| 20 | **Arena.ai Vision Multimodal (30-Model Table)** | LMSYS Arena.ai (2026) | Quality | **37.5%** | `6 / 16` | `claude-opus-4-7-thinking (#2, 1304.0) > claude-opus-5-high (#5, 1299.0)` · `claude-opus-4-7-thinking (#2, 1304.0) > claude-opus-4-8-thinking (#8, 1286.0)` *(+4 more)* |
| 21 | **AA v4 SciCode (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **35.3%** | `6 / 17` | `Muse Spark 1.1 (xhigh) (#4, 0.582) > Muse Spark 1.2 (xhigh) (#7, 0.564)` · `GPT-5.4 (xhigh) (#6, 0.566) > GPT-5.5 (xhigh) (#9, 0.561)` *(+4 more)* |
| 22 | **Aider Polyglot Latency (Seconds per Case)** | Aider Coding | Latency (Flip) | **33.3%** | `2 / 6` | `gpt-4o-2024-11-20 (#4, 12.1s) faster than gpt-4o-mini-2024-07-18 (#8, 17.3s)` · `claude-3-5-sonnet-20241022 (#13, 21.4s) faster than claude-3-5-haiku-20241022 (#17, 31.8s)` |
| 23 | **AA End-to-End Response Time (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **33.3%** | `1 / 3` | `Llama 4 Maverick (#5, 2.9s) faster than Llama 4 Scout (#10, 3.9s)` |
| 24 | **LiveBench v1 Cost per Successful Task ($ USD)** | LiveBench v1 (2026) | Cost | **33.3%** | `1 / 3` | `claude-sonnet-5-5-max-effort ($0.868) > claude-opus-5-5-max-effort ($0.799)` |
| 25 | **LiveBench v1 — IF** | LiveBench v1 (2026) | Quality | **30.8%** | `4 / 13` | `qwen3.8-flash-next (#5, 77.1) > qwen3.8-max (#13, 74.1)` · `claude-fable-5-max-effort (#6, 75.8) > claude-fable-5-1-max-effort (#18, 73.0)` *(+2 more)* |
| 26 | **Arena.ai Text Overall (50-Model Snapshot)** | LMSYS Arena.ai (2026) | Quality | **30.8%** | `4 / 13` | `claude-opus-4-6-thinking (#2, 1504.0) > claude-opus-4-7-thinking (#3, 1502.0)` · `claude-opus-4-6-thinking (#2, 1504.0) > claude-opus-4-8-thinking (#7, 1483.0)` *(+2 more)* |
| 27 | **LiveBench 2.0 — Reasoning** | LiveBench 2.0 (Oct 2026) | Quality | **28.6%** | `2 / 7` | `grok-4.6 (#7, 91.2) > grok-4.7 (#20, 82.7)` · `gpt-5.6-terra (#10, 90.6) > gpt-6.1-terra (#15, 88.7)` |
| 28 | **LiveBench 2.0 — Browser** | LiveBench 2.0 (Oct 2026) | Quality | **28.6%** | `2 / 7` | `claude-sonnet-5.5 (#5, 89.3) > claude-opus-5.5 (#6, 88.4)` · `grok-4.6 (#18, 49.4) > grok-4.7 (#20, 49.3)` |
| 29 | **Arena.ai Document Comprehension** | LMSYS Arena.ai (2026) | Quality | **25.0%** | `4 / 16` | `claude-opus-4-6-high (#3, 1507.0) > claude-opus-4-7-high (#5, 1495.0)` · `claude-opus-4-6-high (#3, 1507.0) > claude-opus-4-8-high (#9, 1475.0)` *(+2 more)* |
| 30 | **Arena.ai Text-to-Video Generation** | LMSYS Arena.ai (2026) | Quality | **25.0%** | `2 / 8` | `dreamina-seedance-2.0-720p (#5, 1479.0) > dreamina-seedance-2.5-720p (#7, 1474.0)` · `veo-3-fast-audio (#16, 1348.0) > veo-3-audio (#19, 1340.0)` |
| 31 | **AA-3D Interactive WebGL Elo** | Artificial Analysis v5 | Quality | **25.0%** | `1 / 4` | `Claude Sonnet 5.5 (#1, 1198.8) > Claude Opus 5.5 (#2, 1196.4)` |
| 32 | **AA-AnalystAgent Data Analyst** | Artificial Analysis v5 | Quality | **25.0%** | `1 / 4` | `Claude Sonnet 5.5 (#2, 0.575) > Claude Opus 5.5 (#3, 0.562)` |
| 33 | **HealthBench Professional Clinical** | Artificial Analysis v5 | Quality | **25.0%** | `1 / 4` | `Claude Sonnet 5.5 (#3, 0.63) > Claude Opus 5.5 (#5, 0.599)` |
| 34 | **FrontierCode 2.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **25.0%** | `1 / 4` | `GPT-6.1 Terra (Max) ($1.29) > GPT-6.1 Sol (Max) ($1.13)` |
| 35 | **HLE-Diamond — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **25.0%** | `1 / 4` | `GPT-6.1 Terra (Max) ($0.146) > GPT-6.1 Sol (Max) ($0.109)` |
| 36 | **CritPt v2 Hard — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **25.0%** | `1 / 4` | `GPT-6.1 Terra (Max) ($0.251) > GPT-6.1 Sol (Max) ($0.230)` |
| 37 | **Terminal-Bench Science — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **25.0%** | `1 / 4` | `Claude Sonnet 5.5 ($23.76) > Claude Opus 5.5 ($19.97)` |
| 38 | **LiveBench 2.0 Cost — Coding ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **25.0%** | `1 / 4` | `gpt-6.1-terra ($24.97) > gpt-6.1-sol ($13.98)` |
| 39 | **SWE-bench Verified (All Submissions)** | SWE-bench | Quality | **25.0%** | `1 / 4` | `Claude 4 Sonnet (#4, 76.8) > Claude 4 Opus (#16, 73.2)` |
| 40 | **SWE-bench Lite (All Submissions)** | SWE-bench | Quality | **25.0%** | `1 / 4` | `GPT 4 (0806) (#22, 39.7) > GPT 4o (#25, 38.0)` |
| 41 | **Arena.ai Search & Grounding** | LMSYS Arena.ai (2026) | Quality | **24.1%** | `7 / 29` | `claude-opus-4-6-search (#2, 1253.0) > claude-opus-4-7 (#4, 1233.0)` · `claude-opus-4-6-search (#2, 1253.0) > claude-opus-4-8 (#12, 1204.0)` *(+5 more)* |
| 42 | **LiveBench v1 — Language** | LiveBench v1 (2026) | Quality | **20.0%** | `4 / 20` | `claude-fable-5-max-effort (#1, 90.7) > claude-fable-5-1-max-effort (#3, 89.5)` · `claude-opus-5-max-effort (#5, 88.7) > claude-opus-5-5-max-effort (#9, 86.3)` *(+2 more)* |
| 43 | **AA v4 Tau-Bench Banking (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **20.0%** | `3 / 15` | `GPT-5.4 (xhigh) (#9, 0.396) > GPT-5.5 (xhigh) (#12, 0.39)` · `Claude Opus 4.7 (Adaptive Reasoning, Max Effort) (#17, 0.346) > Claude Opus 4.8 (Adaptive Reasoning, Max Effort) (#20, 0.342)` *(+1 more)* |
| 44 | **EvalPlus MBPP+ (35x Tests)** | EvalPlus | Quality | **20.0%** | `2 / 10` | `DeepSeek-V2.5 (Nov 2024) (#6, 74.1) > DeepSeek-V3 (Nov 2024) (#9, 73.0)` · `GPT-4-Turbo (Nov 2023) (#7, 73.3) > GPT 4o (Aug 2024) (#10, 72.2)` |
| 45 | **Code2Video-AA Elo** | Artificial Analysis v5 | Quality | **20.0%** | `1 / 5` | `MiMo-V2.6-Flash (#9, 1051.6) > MiMo-V2.6-Pro (#10, 1051.5)` |
| 46 | **Tau3-Banking Agentic Benchmark** | Artificial Analysis v5 | Quality | **20.0%** | `1 / 5` | `DeepSeek V4 Flash Vision (Max) (#10, 0.41) > DeepSeek V4 Pro 0813 (Max) (#11, 0.396)` |
| 47 | **AA Intelligence Index Time per Task (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **20.0%** | `1 / 5` | `Claude Opus 5.5 (#19, 1140.8s) faster than Claude Sonnet 5.5 (#21, 1298.5s)` |
| 48 | **AA-Omniscience v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **20.0%** | `1 / 5` | `GPT-6.1 Terra (Max) ($0.043) > GPT-6.1 Sol (Max) ($0.018)` |
| 49 | **Terminal-Bench Science — Wall-Clock Time per Task (Sec)** | Artificial Analysis v5 | Latency (Flip) | **20.0%** | `1 / 5` | `Claude Opus 5.5 (#15, 2020.7s) faster than Claude Sonnet 5.5 (#19, 2315.2s)` |
| 50 | **AA v4 Latency TTFT (Seconds, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Latency (Flip) | **20.0%** | `1 / 5` | `Phi-4 Multimodal Instruct (#20, 0.8s) faster than Phi-4 Mini Instruct (#24, 0.9s)` |
| 51 | **Arena.ai Coding (Oct 2026)** | LMSYS Arena.ai (2026) | Quality | **20.0%** | `1 / 5` | `mimo-v2.6-flash (#13, 1636.0) > mimo-v2.6-pro (#16, 1630.0)` |
| 52 | **LMSYS Arena Overall (243 Models)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **20.0%** | `1 / 5` | `gemini-2.0-flash-thinking-exp-01-21 (#8, 1376.7) > gemini-2.0-pro-exp-02-05 (#9, 1376.3)` |
| 53 | **LMSYS Arena Math** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **16.7%** | `2 / 12` | `qwen3-32b (#6, 1387.3) > qwen3-235b-a22b (#9, 1372.4)` · `gemini-2.0-flash-thinking-exp-01-21 (#13, 1357.3) > gemini-2.0-pro-exp-02-05 (#18, 1348.7)` |
| 54 | **LMSYS Arena Math (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **16.7%** | `2 / 12` | `qwen3-32b (#7, 1390.2) > qwen3-235b-a22b (#10, 1374.0)` · `gemini-2.0-flash-thinking-exp-01-21 (#13, 1360.8) > gemini-2.0-pro-exp-02-05 (#18, 1355.9)` |
| 55 | **SciCode Scientific Coding** | Artificial Analysis v5 | Quality | **16.7%** | `1 / 6` | `GPT-6.1 Terra (Max) (#18, 0.551) > GPT-6.1 Sol (Max) (#21, 0.542)` |
| 56 | **AA Long-Context Reasoning (LCR)** | Artificial Analysis v5 | Quality | **16.7%** | `1 / 6` | `GPT-6 Luna (Max) (#7, 0.833) > GPT-6 Astra (Max) (#25, 0.807)` |
| 57 | **AA Time to First Answer Token (Seconds)** | Artificial Analysis v5 | Latency (Flip) | **16.7%** | `1 / 6` | `Ministral 3 8B (#8, 0.8s) faster than Ministral 3 3B (#9, 0.9s)` |
| 58 | **AA v4 Humanity's Last Exam (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **14.3%** | `2 / 14` | `Muse Spark 1.1 (xhigh) (#8, 0.462) > Muse Spark 1.2 (xhigh) (#10, 0.455)` · `Gemini 3.5 Flash (#15, 0.427) > Gemini 3.6 Flash (#23, 0.408)` |
| 59 | **FrontierCode 1.0** | Artificial Analysis v5 | Quality | **14.3%** | `1 / 7` | `Muse Wonder (Max) (#6, 0.465) > Muse Wonder Full (Max) (#9, 0.449)` |
| 60 | **Tau2-Bench Tool-Use Agentic** | Artificial Analysis v5 | Quality | **14.3%** | `1 / 7` | `Qwen3.5 4B (Reasoning) (#11, 0.921) > Qwen3.5 9B (Reasoning) (#19, 0.868)` |
| 61 | **LiveBench 2.0 — Coding** | LiveBench 2.0 (Oct 2026) | Quality | **14.3%** | `1 / 7` | `grok-4.6 (#12, 89.1) > grok-4.7 (#18, 84.5)` |
| 62 | **Aider Polyglot Coding (Pass@1 %)** | Aider Coding | Quality | **14.3%** | `1 / 7` | `claude-3-7-sonnet-20250219 (#10, 29.3) > claude-sonnet-4-20250514 (#15, 25.8)` |
| 63 | **AA v4 Coding Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **13.3%** | `2 / 15` | `Gemini 3.5 Flash (#19, 70.1) > Gemini 3.6 Flash (#20, 69.2)` · `DeepSeek V4 Flash 0731 (Reasoning, Max Effort) (#21, 69.1) > DeepSeek V4 Pro 0813 (Reasoning, Max Effort) (#22, 68.8)` |
| 64 | **LiveBench v1 — Data Analysis** | LiveBench v1 (2026) | Quality | **12.5%** | `2 / 16` | `claude-fable-5-max-effort (#6, 80.5) > claude-fable-5-1-max-effort (#8, 80.3)` · `deepseek-v4-flash-vision-exp (#12, 79.5) > deepseek-v4-pro-0813 (#16, 79.2)` |
| 65 | **FrontierCode 2.0** | Artificial Analysis v5 | Quality | **12.5%** | `1 / 8` | `GPT-6.1 Terra (Max) (#3, 0.423) > GPT-6.1 Sol (Max) (#5, 0.406)` |
| 66 | **Terminal-Bench 4.0** | Artificial Analysis v5 | Quality | **12.5%** | `1 / 8` | `Claude Sonnet 5.5 (#3, 0.636) > Claude Opus 5.5 (#4, 0.596)` |
| 67 | **LMSYS Arena Creative Writing** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **12.5%** | `1 / 8` | `gemini-2.0-flash-thinking-exp-1219 (#10, 1368.8) > gemini-2.0-pro-exp-02-05 (#11, 1367.1)` |
| 68 | **LMSYS Arena Multi-Turn Dialogue** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **12.5%** | `1 / 8` | `o1-preview (#21, 1323.9) > o1-2024-12-17 (#25, 1314.5)` |
| 69 | **Aider Polyglot Coding (Pass@2 %)** | Aider Coding | Quality | **12.5%** | `1 / 8` | `claude-3-7-sonnet-20250219 (#11, 64.9) > claude-sonnet-4-20250514 (#14, 61.3)` |
| 70 | **Aider Code Editing Leaderboard** | Aider Coding | Quality | **12.5%** | `1 / 8` | `gpt-4-0613 (#17, 67.7) > gpt-4-0125-preview (#20, 66.2)` |
| 71 | **HLE-Diamond (Humanity's Last Exam)** | Artificial Analysis v5 | Quality | **11.1%** | `1 / 9` | `DeepSeek V4 Flash Vision (Max) (#22, 0.211) > DeepSeek V4 Pro 0813 (Max) (#24, 0.195)` |
| 72 | **AA-Briefcase v1.1 Knowledge Work** | Artificial Analysis v5 | Quality | **11.1%** | `1 / 9` | `Claude Sonnet 5.5 (#1, 1813.6) > Claude Opus 5.5 (#2, 1800.5)` |
| 73 | **LMSYS Arena Longer Query** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **11.1%** | `1 / 9` | `gemini-2.0-flash-thinking-exp-01-21 (#10, 1360.3) > gemini-2.0-pro-exp-02-05 (#11, 1359.8)` |
| 74 | **LiveBench v1 — Reasoning** | LiveBench v1 (2026) | Quality | **10.5%** | `2 / 19` | `gpt-5.6-sol-max (#5, 91.7) > gpt-6-sol-max (#21, 88.7)` · `muse-spark-1.2-xhigh (#13, 90.0) > muse-spark-1.3-xhigh (#16, 89.7)` |
| 75 | **LiveBench v1 — Agentic Coding** | LiveBench v1 (2026) | Quality | **9.1%** | `1 / 11` | `muse-spark-1.1-xhigh (#18, 58.5) > muse-spark-1.2-xhigh (#20, 57.6)` |
| 76 | **AA v4 Omniscience (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **8.7%** | `2 / 23` | `Muse Spark 1.1 (xhigh) (#6, 28.1) > Muse Spark 1.2 (xhigh) (#8, 27.2)` · `Claude Opus 4.5 (Reasoning) (#20, 14.0) > Claude Opus 4.6 (Adaptive Reasoning, Max Effort) (#21, 13.7)` |
| 77 | **LiveBench v1 Global Average** | LiveBench v1 (2026) | Quality | **8.3%** | `1 / 12` | `gpt-5.6-sol-max (#9, 81.1) > gpt-6-sol-max (#13, 79.2)` |
| 78 | **Arena.ai Coding (108-Model Full Table)** | LMSYS Arena.ai (2026) | Quality | **8.3%** | `1 / 12` | `gpt-5.6-luna-xhigh (codex-harness) (#15, 1524.0) > gpt-5.6-terra-xhigh (codex-harness) (#17, 1521.0)` |
| 79 | **SWE-bench Verified (Bash-Only Standardized)** | SWE-bench | Quality | **7.7%** | `1 / 13` | `Gemini 3 Flash (#2, 75.8) > Gemini 3 Pro Preview (#5, 74.2)` |
| 80 | **AA v4 Intelligence Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **6.7%** | `1 / 15` | `Gemini 3.5 Flash (#21, 52.0) > Gemini 3.6 Flash (#23, 51.6)` |
| 81 | **AA v4 Terminal-Bench (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **6.7%** | `1 / 15` | `Gemini 3.5 Flash (#19, 0.786) > Gemini 3.6 Flash (#23, 0.775)` |
| 82 | **LiveBench v1 — Mathematics** | LiveBench v1 (2026) | Quality | **5.6%** | `1 / 18` | `gemini-3.7-flash-high (#19, 93.5) > gemini-3.8-flash-high (#25, 91.6)` |
| 83 | **AA v4 GPQA Diamond (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **0.0%** | `0 / 16` | ✓ **100% Consistent** (`Grok 4.6 (#1) > Grok 4.5 (#9)`, `Grok 4.6 (#1) > Grok 4.20 0309 v2 (Reasoning) (#22)`) |
| 84 | **AA v4 Agentic Index (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **0.0%** | `0 / 15` | ✓ **100% Consistent** (`Claude Opus 5 (Adaptive Reasoning, Max Effort) (#1) > Claude Sonnet 5 (Adaptive Reasoning, Max Effort) (#9)`, `Claude Opus 5 (Adaptive Reasoning, Max Effort) (#1) > Claude Opus 4.8 (Adaptive Reasoning, Max Effort) (#11)`) |
| 85 | **AA v4 CritPt Physics (Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Quality | **0.0%** | `0 / 13` | ✓ **100% Consistent** (`GPT-5.6 Sol (max) (#1) > GPT-5.6 Terra (max) (#2)`, `GPT-5.6 Sol (max) (#1) > GPT-5.6 Luna (max) (#10)`) |
| 86 | **LMSYS Arena Coding (Classic)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 12` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#2)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#9)`) |
| 87 | **GDPval-AA Professional Work Elo** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`Claude Opus 5.5 (#1) > Claude Sonnet 5.5 (#4)`, `Claude Opus 5.5 (#1) > Claude Haiku 5.5 (Max) (#16)`) |
| 88 | **LMSYS Arena Hard Prompts** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#2)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#8)`) |
| 89 | **LMSYS Arena Hard Prompts (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#3)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#14)`) |
| 90 | **LMSYS Arena Coding (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`o3-2025-04-16 (#1) > o1-2024-12-17 (#15)`, `o3-2025-04-16 (#1) > o3-mini-high (#16)`) |
| 91 | **LMSYS Arena Instruction Following** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#2)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#8)`) |
| 92 | **LMSYS Arena Instruction Following (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 9` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#2)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#13)`) |
| 93 | **AA Intelligence Index v5.0** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`Gemini 4 Carbon (#1) > Gemini 4 Argon (#7)`, `Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#5)`) |
| 94 | **CritPt v2 Agentic Hard** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#1) > GPT-6 Luna (Max) (#13)`, `GPT-6.1 Sol (Max) (#2) > GPT-6.1 Terra (Max) (#3)`) |
| 95 | **Terminal-Bench Science 0.1** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`Gemini 4 Carbon (#1) > Gemini 4 Argon (#7)`, `GPT-6 Astra (Max) (#2) > GPT-6 Luna (Max) (#17)`) |
| 96 | **LMSYS Arena Overall (Style-Controlled)** | LMSYS Chatbot Arena (Sub-Tasks) | Quality | **0.0%** | `0 / 8` | ✓ **100% Consistent** (`gemini-2.5-pro-preview-05-06 (#1) > gemini-2.5-flash-preview-05-20 (#5)`, `gemini-2.5-pro-preview-05-06 (#1) > gemini-2.0-pro-exp-02-05 (#10)`) |
| 97 | **GDP.pdf Document Deliverable** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`Muse Wonder Full (Max) (#1) > Muse Wonder (Max) (#5)`, `GPT-6.1 Sol (Max) (#3) > GPT-6.1 Terra (Max) (#6)`) |
| 98 | **AA-Omniscience Raw Accuracy** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#6)`, `Claude Opus 5.5 (#2) > Claude Haiku 5.5 (Max) (#24)`) |
| 99 | **LiveBench 2.0 Overall Score** | LiveBench 2.0 (Oct 2026) | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`gpt-6-astra (#2) > gpt-6-luna (#17)`, `claude-opus-5.5 (#3) > claude-sonnet-5.5 (#5)`) |
| 100 | **LiveBench 2.0 — Long Agentic** | LiveBench 2.0 (Oct 2026) | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`gpt-6-astra (#2) > gpt-6-luna (#15)`, `claude-opus-5.5 (#3) > claude-sonnet-5.5 (#5)`) |
| 101 | **Arena.ai Image-to-Video Generation** | LMSYS Arena.ai (2026) | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`gemini-omni-1.1-flash (#2) > gemini-omni-flash (#6)`, `dreamina-seedance-2.5-720p (#4) > dreamina-seedance-2.0-720p (#5)`) |
| 102 | **EvalPlus Combined Average** | EvalPlus | Quality | **0.0%** | `0 / 7` | ✓ **100% Consistent** (`DeepSeek-V3 (Nov 2024) (#3) > DeepSeek-V2.5 (Nov 2024) (#5)`, `GPT 4o (Aug 2024) (#4) > GPT 4o Mini (July 2024) (#8)`) |
| 103 | **AA-Omniscience v1.1 Net Score** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Gemini 4 Carbon (#1) > Gemini 4 Argon (#4)`, `Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#9)`) |
| 104 | **CritPt Physics Reasoning** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Muse Wonder Full (Max) (#1) > Muse Wonder (Max) (#8)`, `GPT-6.1 Sol (Max) (#2) > GPT-6.1 Terra (Max) (#9)`) |
| 105 | **IFBench Instruction Following** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`Nemotron 3 Ultra 550B A55B (Reasoning) (#2) > Nemotron Cascade 2 30B A3B (#3)`, `Qwen3.5 397B A17B (Reasoning) (#5) > Qwen3.5 122B A10B (Reasoning) (#8)`) |
| 106 | **Aider Polyglot Total Benchmark Cost ($ USD)** | Aider Coding | Cost | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`o3-pro (#3) > o3 (#10)`, `o3-pro (#3) > o3-mini (#14)`) |
| 107 | **EvalPlus HumanEval+ (80x Tests)** | EvalPlus | Quality | **0.0%** | `0 / 6` | ✓ **100% Consistent** (`GPT 4o (Aug 2024) (#3) > GPT-4-Turbo (April 2024) (#5)`, `GPT 4o (Aug 2024) (#3) > GPT 4o Mini (July 2024) (#7)`) |
| 108 | **Humanity's Last Exam (Full HLE)** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`Claude Opus 5.5 (#1) > Claude Sonnet 5.5 (#4)`, `Claude Opus 5.5 (#1) > Claude Haiku 5.5 (Max) (#16)`) |
| 109 | **Harvey LAB-AA v1.1 Legal Agent** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`Muse Wonder Full (Max) (#1) > Muse Wonder (Max) (#2)`, `GPT-6 Astra (Max) (#4) > GPT-6 Luna (Max) (#9)`) |
| 110 | **GDP.pdf Document — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Luna (Max) (#23)`, `Claude Opus 5.5 (#3) > Claude Sonnet 5.5 (#5)`) |
| 111 | **LiveBench 2.0 — Research** | LiveBench 2.0 (Oct 2026) | Quality | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`grok-4.7 (#2) > grok-4.6 (#5)`, `claude-opus-5.5 (#4) > claude-sonnet-5.5 (#6)`) |
| 112 | **LiveBench 2.0 Cost — Research ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`gpt-6-astra (#2) > gpt-6-luna (#24)`, `claude-opus-5.5 (#3) > claude-sonnet-5.5 (#4)`) |
| 113 | **Arena.ai Text-to-Image Generation** | LMSYS Arena.ai (2026) | Quality | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`gpt-image-2 (medium) (#1) > gpt-image-1.5-high-fidelity (#9)`, `reve-2.1 (#2) > reve-2.0 (#4)`) |
| 114 | **Arena.ai Image Editing** | LMSYS Arena.ai (2026) | Quality | **0.0%** | `0 / 5` | ✓ **100% Consistent** (`gpt-image-2.5-sunburst (#1) > gpt-image-2.5-flare (#2)`, `gpt-image-2 (medium) (#3) > gpt-image-1.5-high-fidelity (#15)`) |
| 115 | **AA API Input Price ($/1M Tokens)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Sol (Daybreak Blue, max) (#15)`, `Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#9)`) |
| 116 | **AA API Output Price ($/1M Tokens)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Sol (Daybreak Blue, max) (#15)`, `Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#10)`) |
| 117 | **AA API Blended Price (3:1 In:Out $/1M)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Sol (Daybreak Blue, max) (#14)`, `Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#11)`) |
| 118 | **AA Intelligence Index Total Run Cost ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#4)`, `Claude Opus 5.5 (#2) > Claude Haiku 5.5 (Max) (#23)`) |
| 119 | **AA-Briefcase Total Suite Cost ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#3)`, `Claude Opus 5.5 (#2) > Claude Haiku 5.5 (Max) (#21)`) |
| 120 | **AA-Briefcase v1.1 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#2) > Claude Sonnet 5.5 (#3)`, `Claude Opus 5.5 (#2) > Claude Haiku 5.5 (Max) (#21)`) |
| 121 | **AutomationBench-AA — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#5)`, `Claude Opus 5.5 (#4) > Claude Haiku 5.5 (Max) (#24)`) |
| 122 | **Terminal-Bench 4.0 — Total Cost per Task ($ USD)** | Artificial Analysis v5 | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude Opus 5.5 (#4) > Claude Sonnet 5.5 (#5)`, `Claude Opus 5.5 (#4) > Claude Haiku 5.5 (Max) (#23)`) |
| 123 | **LiveBench 2.0 — Data Analysis** | LiveBench 2.0 (Oct 2026) | Quality | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`gpt-6-astra (#2) > gpt-6-luna (#19)`, `gpt-6.1-sol (#3) > gpt-6.1-terra (#4)`) |
| 124 | **LiveBench 2.0 Cost — Overall Mean ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`claude-opus-5.5 (#2) > claude-sonnet-5.5 (#4)`, `claude-opus-5.5 (#2) > claude-haiku-5.5 (#19)`) |
| 125 | **LiveBench 2.0 Cost — Long Agentic ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`claude-opus-5.5 (#2) > claude-sonnet-5.5 (#4)`, `claude-opus-5.5 (#2) > claude-haiku-5.5 (#12)`) |
| 126 | **LiveBench 2.0 Cost — Browser ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`claude-opus-5.5 (#3) > claude-sonnet-5.5 (#4)`, `claude-opus-5.5 (#3) > claude-haiku-5.5 (#22)`) |
| 127 | **LiveBench 2.0 Cost — Data Analysis ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`claude-opus-5.5 (#2) > claude-sonnet-5.5 (#4)`, `claude-opus-5.5 (#2) > claude-haiku-5.5 (#24)`) |
| 128 | **LiveBench 2.0 Cost — Design ($/Task)** | LiveBench 2.0 (Oct 2026) | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`claude-opus-5.5 (#2) > claude-sonnet-5.5 (#3)`, `claude-opus-5.5 (#2) > claude-haiku-5.5 (#13)`) |
| 129 | **SWE-bench Verified Total Run Cost ($ USD)** | SWE-bench | Cost | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`Claude 4 Opus (20250514) (#2) > Claude 4 Sonnet (20250514) (#15)`, `Claude 4.5 Opus (#4) > Claude 4.5 Sonnet (#5)`) |
| 130 | **SWE-bench Multimodal (All Submissions)** | SWE-bench | Quality | **0.0%** | `0 / 4` | ✓ **100% Consistent** (`OpenHands-Versa (Claude-Sonnet 4) (#4) > OpenHands-Versa (Claude-3.7 Sonnet) (#6)`, `OpenHands-Versa (Claude-Sonnet 4) (#4) > Claude-3.5 Sonnet (#12)`) |
| 131 | **Terminal-Bench Hard** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 3` | ✓ **100% Consistent** (`Qwen3.5 397B A17B (Reasoning) (#7) > Qwen3.5 122B A10B (Reasoning) (#13)`, `Qwen3.5 397B A17B (Reasoning) (#7) > Qwen3.5 9B (Reasoning) (#21)`) |
| 132 | **MMMU-Pro Multimodal Understanding** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 3` | ✓ **100% Consistent** (`GPT-6 Astra (Max) (#2) > GPT-6 Luna (Max) (#13)`, `GPT-6.1 Sol (Max) (#3) > GPT-6.1 Terra (Max) (#5)`) |
| 133 | **AA Time to First Token (TTFT Seconds)** | Artificial Analysis v5 | Latency (Flip) | **0.0%** | `0 / 3` | ✓ **100% Consistent** (`Nemotron 3 Ultra (#20) > Nemotron 3 Nano (#3)`, `gpt-oss-120b (#21) > gpt-oss-20b (#9)`) |
| 134 | **SWE-bench Test (All Submissions)** | SWE-bench | Quality | **0.0%** | `0 / 3` | ✓ **100% Consistent** (`Claude 4.5 Opus (#1) > Claude 3 Opus (#14)`, `SWE-agent 1.0 (Claude 3.7 Sonnet) (#5) > CodeAct v2.1 (claude-3-5-sonnet-20241022) (#7)`) |
| 135 | **GPQA Diamond** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`DeepSeek V4 Pro 0813 (Max) (#7) > DeepSeek V4 Flash Vision (Max) (#12)`, `Qwen3.8 Max (0902) (#8) > Qwen3.8-Flash-Next (#9)`) |
| 136 | **AIME 2025 Competition Math** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`gpt-oss-120b (#2) > gpt-oss-20b (#5)`, `Magistral Medium 1.2 (#13) > Magistral Small 1.2 (#15)`) |
| 137 | **Terminal-Bench 2.1** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`Qwen3.8 Max (0902) (#2) > Qwen3.8-Flash-Next (#5)`, `DeepSeek V4 Pro 0813 (Max) (#10) > DeepSeek V4 Flash Vision (Max) (#13)`) |
| 138 | **LiveCodeBench** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`gpt-oss-120b (#1) > gpt-oss-20b (#6)`, `Magistral Medium 1.2 (#9) > Magistral Small 1.2 (#15)`) |
| 139 | **AA v4 Blended API Price ($/1M, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Cost | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`o1-pro (#1) > o1 (#8)`, `Claude 4 Opus (Reasoning) (#5) > Claude 4 Sonnet (Reasoning) (#25)`) |
| 140 | **LiveBench v1 Cost per Question ($ USD)** | LiveBench v1 (2026) | Cost | **0.0%** | `0 / 2` | ✓ **100% Consistent** (`claude-opus-5-5-max-effort (#4) > claude-sonnet-5-5-max-effort (#5)`, `gpt-5.6-sol-max (#11) > gpt-5.6-terra-max (#20)`) |
| 141 | **EnterpriseOps-Gym-AA** | Artificial Analysis v5 | Quality | **0.0%** | `0 / 1` | ✓ **100% Consistent** (`DeepSeek V4 Pro 0813 (Max) (#1) > DeepSeek V4 Flash Vision (Max) (#5)`) |
| 142 | **AA v4 Output Speed (Tokens/Sec, Aug 2026)** | Artificial Analysis v4 (Aug 2026) | Latency (Flip) | **0.0%** | `0 / 1` | ✓ **100% Consistent** (`Gemini 2.5 Flash (Reasoning) (#13) > Gemini 2.5 Flash-Lite (Reasoning) (#6)`) |
| 143 | **Aider Refactoring Leaderboard** | Aider Coding | Quality | **0.0%** | `0 / 1` | ✓ **100% Consistent** (`gpt-4o (#4) > gpt-4-1106-preview (#5)`) |

</details>

---

## 4. Single Best Way to Host, Share & Customize

1. **One-Command Static Hosting (Cloudflare Pages / Vercel / GitHub Pages)**:
   Because [index.html](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/index.html) and the single-file bundle [shareable_table.html](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/shareable_table.html) are 100% static with zero build step, deploy globally in one command:
   ```bash
   npx wrangler pages deploy /Users/sagar-sayali/ai-benchmark-contradiction-index --project-name ai-benchmark-contradiction-index
   # OR
   npx vercel --prod /Users/sagar-sayali/ai-benchmark-contradiction-index
   ```
2. **Two-View URL Sharing (`popular_benchmarks` vs `ALL`)**:
   - Default view (`popular_benchmarks`): `?view=popular_benchmarks`
   - Full catalog (`ALL`): `?view=ALL`
3. **Customizing `popular_benchmarks`**:
   - **In the UI**: Click **Customize Popular** in the top bar of [index.html](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/index.html) to check/uncheck any benchmark, or click **Copy Markdown** to copy the current table as GitHub Markdown.
   - **In Code**: Edit [`POPULAR_BENCHMARK_IDS`](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/generate_all_benchmarks_data.py#L10-L60) in [generate_all_benchmarks_data.py](file:///Users/sagar-sayali/ai-benchmark-contradiction-index/generate_all_benchmarks_data.py) and run `python3 generate_all_benchmarks_data.py`.
