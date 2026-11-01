(function () {
  const rawData = window.CONTRADICTION_BENCHMARKS_DATA || { benchmarks: [], popularBenchmarkIds: [] };
  const allBenchmarks = rawData.benchmarks || [];

  const DEFAULT_POPULAR_IDS = new Set(
    rawData.popularBenchmarkIds && rawData.popularBenchmarkIds.length
      ? rawData.popularBenchmarkIds
      : allBenchmarks.filter(b => b.is_popular).map(b => b.id)
  );

  function loadPopularSet() {
    try {
      const saved = localStorage.getItem('custom_popular_benchmark_ids');
      if (saved) {
        const arr = JSON.parse(saved);
        if (Array.isArray(arr) && arr.length > 0) return new Set(arr);
      }
    } catch (e) {}
    return new Set(DEFAULT_POPULAR_IDS);
  }

  let popularIds = loadPopularSet();

  const urlParams = new URLSearchParams(window.location.search);
  const initialView = urlParams.get('view') === 'ALL' ? 'ALL' : 'popular_benchmarks';
  const savedTheme = localStorage.getItem('contradiction_theme') || 'light';
  document.documentElement.setAttribute('data-theme', savedTheme);

  const state = {
    view: initialView, // 'popular_benchmarks' | 'ALL'
    type: 'all',       // 'all' | 'quality' | 'latency' | 'cost'
    labFilter: null,   // null | 'OpenAI' | 'Anthropic' | 'Google' | 'xAI' | 'DeepSeek' | 'Qwen'
    search: '',
    sortBy: 'score_desc',
    expandedId: null,
    screenshotMode: false
  };

  const LAB_DEFS = [
    { key: 'OpenAI', title: 'OpenAI GPT', match: ['OpenAI'], rule: 'Astra > Sol > Terra > Luna • 6.1 > 6.0', cls: 'lab-openai' },
    { key: 'Anthropic', title: 'Anthropic Claude', match: ['Anthropic'], rule: 'Opus > Sonnet > Haiku • 5.5 > 4.7', cls: 'lab-anthropic' },
    { key: 'Google', title: 'Google Gemini', match: ['Google'], rule: 'Carbon > Argon • Pro > Flash > Lite', cls: 'lab-google' },
    { key: 'xAI', title: 'xAI Grok', match: ['xAI'], rule: 'Grok 4.7 > 4.6 > 4.5 > 4.20', cls: 'lab-xai' },
    { key: 'DeepSeek', title: 'DeepSeek', match: ['DeepSeek'], rule: 'Pro > Flash • V4 > V3 > V2.5', cls: 'lab-deepseek' },
    { key: 'Qwen', title: 'Qwen & Meta', match: ['Alibaba', 'Meta'], rule: 'Max > Plus > Flash • 235B > 32B', cls: 'lab-qwen' }
  ];

  function getLabInfo(familyStr) {
    if (!familyStr) return { label: 'Lab', cls: 'lab-other', key: 'Other' };
    if (familyStr.includes('OpenAI')) return { label: 'OpenAI', cls: 'lab-openai', key: 'OpenAI' };
    if (familyStr.includes('Anthropic')) return { label: 'Anthropic', cls: 'lab-anthropic', key: 'Anthropic' };
    if (familyStr.includes('Google')) return { label: 'Google', cls: 'lab-google', key: 'Google' };
    if (familyStr.includes('xAI')) return { label: 'xAI', cls: 'lab-xai', key: 'xAI' };
    if (familyStr.includes('Meta')) return { label: 'Meta', cls: 'lab-meta', key: 'Qwen' };
    if (familyStr.includes('DeepSeek')) return { label: 'DeepSeek', cls: 'lab-deepseek', key: 'DeepSeek' };
    if (familyStr.includes('Qwen')) return { label: 'Qwen', cls: 'lab-qwen', key: 'Qwen' };
    const firstWord = familyStr.split(' ')[0];
    return { label: firstWord, cls: 'lab-other', key: 'Other' };
  }

  function cleanModelLabel(s) {
    if (!s) return '';
    return s
      .replace(/^.*?\+\s*/, '')
      .replace(/^ollama\//, '')
      .replace(/\s*\((?:Max,\s*Default Fallback|Adaptive Reasoning(?:,\s*Max Effort)?|Default Thinking|bf16|FP8|high|32k thinking(?: tokens)?|202\d-\d\d-\d\d)\)/gi, '')
      .trim();
  }

  function formatScore(val, unit, mtype) {
    if (val === undefined || val === null) return '';
    if (mtype === 'cost' || (unit && unit.includes('$'))) {
      return '$' + Number(val).toFixed(val < 1 ? 3 : 2);
    }
    if (mtype === 'latency' && unit && unit.toLowerCase().includes('sec')) {
      return Number(val).toFixed(1) + 's';
    }
    return Number(val).toFixed(val > 10 ? 1 : 3).replace(/\.?0+$/, '');
  }

  function formatContraChipText(p, bench) {
    const ma = cleanModelLabel(p.model_a);
    const mb = cleanModelLabel(p.model_b);
    const mtype = bench.metric_type;
    const sa = formatScore(p.score_a, bench.unit, mtype);
    const sb = formatScore(p.score_b, bench.unit, mtype);
    if (mtype === 'latency') {
      return `${ma} (#${p.rank_a}, ${sa}) faster than ${mb} (#${p.rank_b}, ${sb})`;
    }
    if (mtype === 'cost') {
      return `${mb} (${sb}) > ${ma} (${sa})`;
    }
    return `${mb} (#${p.rank_b}, ${sb}) > ${ma} (#${p.rank_a}, ${sa})`;
  }

  function heatInfo(score) {
    if (score <= 0.01) return { cls: 'heat-0', grade: 'A+' };
    if (score < 16) return { cls: 'heat-low', grade: 'A' };
    if (score < 32) return { cls: 'heat-med', grade: 'B' };
    return { cls: 'heat-high', grade: 'C' };
  }

  function getBaseViewBenchmarks() {
    return allBenchmarks.filter(b => {
      if (state.view === 'popular_benchmarks' && !popularIds.has(b.id)) return false;
      if (state.type !== 'all' && b.metric_type !== state.type) return false;
      const ev = b.canonical_top25;
      return ev && ev.comparable_pairs_count >= 1;
    });
  }

  function getFiltered() {
    const q = state.search.trim().toLowerCase();
    const base = getBaseViewBenchmarks();
    const list = [];

    for (const b of base) {
      const ev = b.canonical_top25;

      if (state.labFilter) {
        const def = LAB_DEFS.find(d => d.key === state.labFilter);
        if (def) {
          const allP = [...(ev.contradictions || []), ...(ev.valid_pairs || [])];
          const hasLab = allP.some(p => def.match.some(m => (p.family || '').includes(m)));
          if (!hasLab) continue;
        }
      }

      if (q) {
        const matchMeta =
          b.name.toLowerCase().includes(q) ||
          b.suite.toLowerCase().includes(q) ||
          b.category.toLowerCase().includes(q);
        const matchModel =
          (ev.top25 || []).some(m => m.name.toLowerCase().includes(q)) ||
          (ev.contradictions || []).some(p => p.model_a.toLowerCase().includes(q) || p.model_b.toLowerCase().includes(q));
        if (!matchMeta && !matchModel) continue;
      }

      list.push({ bench: b, ev });
    }

    list.sort((a, b) => {
      if (state.sortBy === 'score_desc') {
        if (b.ev.contradiction_score !== a.ev.contradiction_score) return b.ev.contradiction_score - a.ev.contradiction_score;
        if (b.ev.contradictions_count !== a.ev.contradictions_count) return b.ev.contradictions_count - a.ev.contradictions_count;
        return b.ev.comparable_pairs_count - a.ev.comparable_pairs_count;
      }
      if (state.sortBy === 'score_asc') {
        if (a.ev.contradiction_score !== b.ev.contradiction_score) return a.ev.contradiction_score - b.ev.contradiction_score;
        return b.ev.comparable_pairs_count - a.ev.comparable_pairs_count;
      }
      if (state.sortBy === 'pairs') {
        if (b.ev.comparable_pairs_count !== a.ev.comparable_pairs_count) return b.ev.comparable_pairs_count - a.ev.comparable_pairs_count;
        return b.ev.contradiction_score - a.ev.contradiction_score;
      }
      if (state.sortBy === 'name') {
        return a.bench.name.localeCompare(b.bench.name);
      }
      if (state.sortBy === 'type') {
        if (a.bench.metric_type !== b.bench.metric_type) return a.bench.metric_type.localeCompare(b.bench.metric_type);
        return b.ev.contradiction_score - a.ev.contradiction_score;
      }
      return 0;
    });

    return list;
  }

  function renderFamilyStrip() {
    const base = getBaseViewBenchmarks();
    const strip = document.getElementById('familyStrip');

    strip.innerHTML = LAB_DEFS.map(def => {
      let comp = 0;
      let con = 0;
      base.forEach(b => {
        const ev = b.canonical_top25;
        (ev.contradictions || []).forEach(p => {
          if (def.match.some(m => (p.family || '').includes(m))) { comp++; con++; }
        });
        (ev.valid_pairs || []).forEach(p => {
          if (def.match.some(m => (p.family || '').includes(m))) { comp++; }
        });
      });
      const rate = comp > 0 ? ((con / comp) * 100).toFixed(1) : '0.0';
      const isActive = state.labFilter === def.key;
      return `
        <div class="fam-pill-card ${isActive ? 'active-fam' : ''}" data-lab="${def.key}" title="Click to filter benchmarks featuring ${def.title}">
          <div class="fam-top">
            <span><span class="lab-tag ${def.cls}">${def.key}</span> ${def.title.replace(def.key + ' ', '')}</span>
            <span class="fam-rate">${rate}% (${con}/${comp})</span>
          </div>
          <div class="fam-rule">${def.rule}</div>
        </div>
      `;
    }).join('');

    strip.querySelectorAll('.fam-pill-card').forEach(el => {
      el.addEventListener('click', () => {
        const k = el.getAttribute('data-lab');
        state.labFilter = state.labFilter === k ? null : k;
        renderAll();
      });
    });
  }

  function renderTable() {
    document.getElementById('cntPopular').textContent = popularIds.size;
    document.getElementById('cntAll').textContent = allBenchmarks.length;

    const filtered = getFiltered();
    let totComp = 0;
    let totCon = 0;
    let zeroCnt = 0;
    filtered.forEach(({ ev }) => {
      totComp += ev.comparable_pairs_count;
      totCon += ev.contradictions_count;
      if (ev.contradictions_count === 0) zeroCnt++;
    });

    const aggRate = totComp > 0 ? ((totCon / totComp) * 100).toFixed(1) : '0.0';
    document.getElementById('tldrOverallRate').textContent = `${aggRate}%`;
    document.getElementById('tldrOverallSub').textContent = `${totCon} / ${totComp} Top-25 pairs inverted`;
    document.getElementById('tldrZeroCount').textContent = `${zeroCnt} / ${filtered.length}`;

    const tbody = document.getElementById('tableBody');
    tbody.innerHTML = '';

    if (filtered.length === 0) {
      tbody.innerHTML = `<tr><td colspan="6" style="padding:36px;text-align:center;color:var(--text-secondary);">No benchmarks match the active filter.</td></tr>`;
      return;
    }

    filtered.forEach(({ bench, ev }, idx) => {
      const tr = document.createElement('tr');
      tr.className = 'bench-row' + (state.expandedId === bench.id ? ' expanded' : '');

      const h = heatInfo(ev.contradiction_score);
      const tStats = (ev.by_axis && ev.by_axis.tier) || { contradicted: 0, comparable: 0 };
      const vStats = (ev.by_axis && ev.by_axis.version) || { contradicted: 0, comparable: 0 };

      let chipsHtml = '';
      if (ev.contradictions && ev.contradictions.length > 0) {
        const shown = ev.contradictions.slice(0, 2);
        chipsHtml = shown.map(p => {
          const lab = getLabInfo(p.family);
          return `<span class="inv-chip"><span class="lab-tag ${lab.cls}">${lab.label}</span><span>${formatContraChipText(p, bench)}</span></span>`;
        }).join('');
        if (ev.contradictions.length > 2) {
          chipsHtml += `<span class="more-count">+${ev.contradictions.length - 2} more</span>`;
        }
      } else {
        const vShown = (ev.valid_pairs || []).slice(0, 2).map(p => {
          const lab = getLabInfo(p.family);
          return `<span class="lab-tag ${lab.cls}">${lab.label}</span> ${cleanModelLabel(p.model_a)} (#${p.rank_a}) &gt; ${cleanModelLabel(p.model_b)} (#${p.rank_b})`;
        }).join(' &middot; ');
        chipsHtml = `<span class="consistent-chip">&#10003; 100% Monotonic${vShown ? ' &mdash; ' + vShown : ''}</span>`;
      }

      const polHtml =
        bench.metric_type === 'latency'
          ? `<div class="pol-pill"><span class="pol-tag pol-latency">&darr; Latency (Flip)</span><span class="pol-sub">Luna &lt; Terra &lt; Sol</span></div>`
          : bench.metric_type === 'cost'
          ? `<div class="pol-pill"><span class="pol-tag pol-cost">$ Cost</span><span class="pol-sub">Sol &ge; Terra &ge; Luna</span></div>`
          : `<div class="pol-pill"><span class="pol-tag pol-quality">&uarr; Quality</span><span class="pol-sub">Sol &gt; Terra &bull; 6.1 &gt; 6.0</span></div>`;

      tr.innerHTML = `
        <td class="rank-cell">${idx + 1}</td>
        <td>
          <div class="bench-name">
            <span>${bench.name}</span>
          </div>
          <div class="suite-line">
            <span class="suite-pill">${bench.suite}</span>
            <span>${bench.category}</span>
          </div>
        </td>
        <td>${polHtml}</td>
        <td>
          <div class="heat-box ${h.cls}">
            <span class="heat-pct">${ev.contradiction_score.toFixed(1)}%</span>
            <div class="heat-bar-track">
              <div class="heat-bar-fill" style="width:${Math.min(100, ev.contradiction_score)}%"></div>
            </div>
            <span class="grade-tag">${h.grade}</span>
          </div>
        </td>
        <td>
          <div class="pairs-ratio">${ev.contradictions_count} / ${ev.comparable_pairs_count}</div>
          <div class="pairs-axes">Tier ${tStats.contradicted}/${tStats.comparable}${vStats.comparable > 0 ? ` &middot; Gen ${vStats.contradicted}/${vStats.comparable}` : ''}</div>
        </td>
        <td>
          <div class="inversions-wrap">${chipsHtml}</div>
        </td>
      `;

      tr.addEventListener('click', () => {
        state.expandedId = state.expandedId === bench.id ? null : bench.id;
        renderTable();
      });

      tbody.appendChild(tr);

      if (state.expandedId === bench.id) {
        const drawerTr = document.createElement('tr');
        drawerTr.className = 'drawer-row';
        drawerTr.innerHTML = `<td colspan="6">${renderExpandedDrawer(bench, ev)}</td>`;
        tbody.appendChild(drawerTr);
      }
    });
  }

  function renderExpandedDrawer(bench, ev) {
    const allPairs = [
      ...(ev.contradictions || []).map(p => ({ ...p, isContra: true })),
      ...(ev.valid_pairs || []).map(p => ({ ...p, isContra: false }))
    ];

    const pairsHtml = allPairs.map(p => {
      const axName = p.axis === 'tier' ? 'Size Tier' : 'Generation';
      const sa = formatScore(p.score_a, bench.unit, bench.metric_type);
      const sb = formatScore(p.score_b, bench.unit, bench.metric_type);
      const lab = getLabInfo(p.family);
      return `
        <div class="drawer-pair-item ${p.isContra ? '' : 'is-valid'}">
          <div>
            <div class="dp-models">
              <span class="lab-tag ${lab.cls}">${lab.label}</span>
              #${p.rank_b} ${cleanModelLabel(p.model_b)} (${sb}) vs #${p.rank_a} ${cleanModelLabel(p.model_a)} (${sa})
            </div>
            <div class="dp-rule">[${axName} &bull; ${p.family}] Expected: <code>${p.expected}</code></div>
          </div>
          <span class="dp-badge ${p.isContra ? 'bad' : 'good'}">${p.isContra ? 'CONTRADICTED' : 'VALID'}</span>
        </div>
      `;
    }).join('');

    const contraSet = new Set();
    (ev.contradictions || []).forEach(p => {
      contraSet.add(p.model_a);
      contraSet.add(p.model_b);
    });

    const top25Html = (ev.top25 || []).map(m => {
      const isC = contraSet.has(m.name);
      return `
        <div class="t25-item ${isC ? 't25-contra' : ''}" title="${m.name}">
          <div style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">
            <span class="t25-rank">#${m.rank}</span>
            <span class="t25-name">${cleanModelLabel(m.name)}</span>
          </div>
          <span class="t25-score">${formatScore(m.score, bench.unit, bench.metric_type)}</span>
        </div>
      `;
    }).join('');

    return `
      <div class="drawer-grid">
        <div class="drawer-col">
          <h4>All Comparable Intra-Family Pairs in Top 25 (${ev.contradictions_count} Contradicted / ${ev.comparable_pairs_count} Total, Equal Weight)</h4>
          <div class="drawer-pairs-list">${pairsHtml}</div>
        </div>
        <div class="drawer-col">
          <h4>Top 25 Ranked Models (${bench.unit})</h4>
          <div class="top25-mini-grid">${top25Html}</div>
        </div>
      </div>
    `;
  }

  function renderCustomizeGrid() {
    const grid = document.getElementById('customizeGrid');
    const sorted = [...allBenchmarks].sort((a, b) => a.name.localeCompare(b.name));
    grid.innerHTML = sorted.map(b => {
      const checked = popularIds.has(b.id) ? 'checked' : '';
      return `
        <label class="cust-item">
          <input type="checkbox" data-bench-id="${b.id}" ${checked} />
          <span style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;" title="${b.name} (${b.suite})">${b.name}</span>
        </label>
      `;
    }).join('');

    grid.querySelectorAll('input[type="checkbox"]').forEach(cb => {
      cb.addEventListener('change', e => {
        const id = e.target.getAttribute('data-bench-id');
        if (e.target.checked) popularIds.add(id);
        else popularIds.delete(id);
        try {
          localStorage.setItem('custom_popular_benchmark_ids', JSON.stringify(Array.from(popularIds)));
        } catch (err) {}
        renderAll();
      });
    });
  }

  function updateThemeButton() {
    const cur = document.documentElement.getAttribute('data-theme') || 'light';
    document.getElementById('themeIcon').textContent = cur === 'light' ? '☀️' : '🌙';
    document.getElementById('themeLabel').textContent = cur === 'light' ? 'Editorial Light' : 'Dark Mode';
  }

  function copyMarkdownTable() {
    const filtered = getFiltered();
    const lines = [
      `| # | Benchmark | Suite | Polarity | Contradiction Score | Inverted / Pairs | Headline Top-25 Inversions (Actual vs. Expected) |`,
      `| :-: | :--- | :--- | :-: | :-: | :-: | :--- |`
    ];
    filtered.forEach(({ bench, ev }, i) => {
      let ex = '';
      if (ev.contradictions && ev.contradictions.length > 0) {
        ex = ev.contradictions.slice(0, 2).map(p => `\`${formatContraChipText(p, bench)}\``).join(' · ');
        if (ev.contradictions.length > 2) ex += ` *(+${ev.contradictions.length - 2} more)*`;
      } else {
        const vp = (ev.valid_pairs || []).slice(0, 2).map(p => `\`${cleanModelLabel(p.model_a)} (#${p.rank_a}) > ${cleanModelLabel(p.model_b)} (#${p.rank_b})\``).join(', ');
        ex = `✓ 100% Monotonic (${vp})`;
      }
      lines.push(`| ${i + 1} | **${bench.name}** | ${bench.suite} | ${bench.metric_type.toUpperCase()} | **${ev.contradiction_score.toFixed(1)}%** | \`${ev.contradictions_count} / ${ev.comparable_pairs_count}\` | ${ex} |`);
    });

    navigator.clipboard.writeText(lines.join('\n')).then(() => {
      const btn = document.getElementById('copyMdBtn');
      const orig = btn.innerHTML;
      btn.textContent = '✓ Copied Markdown!';
      setTimeout(() => { btn.innerHTML = orig; }, 1800);
    });
  }

  function exportCsv() {
    const filtered = getFiltered();
    const headers = ['Rank', 'Benchmark_ID', 'View', 'Benchmark_Name', 'Suite', 'Polarity', 'Contradiction_Score_Pct', 'Contradicted_Pairs', 'Comparable_Pairs', 'Top_Inversions'];
    const rows = [headers.join(',')];
    filtered.forEach(({ bench, ev }, i) => {
      const inv = (ev.contradictions || []).map(p => formatContraChipText(p, bench)).join(' | ');
      rows.push([
        i + 1,
        `"${bench.id}"`,
        state.view,
        `"${bench.name.replace(/"/g, '""')}"`,
        `"${bench.suite}"`,
        bench.metric_type,
        ev.contradiction_score,
        ev.contradictions_count,
        ev.comparable_pairs_count,
        `"${inv.replace(/"/g, '""')}"`
      ].join(','));
    });
    const blob = new Blob([rows.join('\n')], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `ai_benchmark_contradiction_index_${state.view}.csv`;
    a.click();
    URL.revokeObjectURL(url);
  }

  function renderAll() {
    renderFamilyStrip();
    renderTable();
  }

  function bindEvents() {
    document.querySelectorAll('#viewSwitch .seg-view-btn').forEach(btn => {
      if (btn.getAttribute('data-view') === state.view) btn.classList.add('active');
      else btn.classList.remove('active');

      btn.addEventListener('click', () => {
        document.querySelectorAll('#viewSwitch .seg-view-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.view = btn.getAttribute('data-view');
        const url = new URL(window.location.href);
        url.searchParams.set('view', state.view);
        window.history.replaceState({}, '', url);
        renderAll();
      });
    });

    document.querySelectorAll('#typeFilter .pol-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('#typeFilter .pol-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        state.type = btn.getAttribute('data-type');
        renderAll();
      });
    });

    document.getElementById('searchInput').addEventListener('input', e => {
      state.search = e.target.value;
      renderTable();
    });

    document.querySelectorAll('th.sortable').forEach(th => {
      th.addEventListener('click', () => {
        const target = th.getAttribute('data-sort');
        if (target === 'score_desc') {
          state.sortBy = state.sortBy === 'score_desc' ? 'score_asc' : 'score_desc';
        } else {
          state.sortBy = target;
        }
        document.querySelectorAll('th.sortable').forEach(t => t.classList.remove('active-sort'));
        th.classList.add('active-sort');
        renderTable();
      });
    });

    document.getElementById('themeToggleBtn').addEventListener('click', () => {
      const cur = document.documentElement.getAttribute('data-theme') || 'light';
      const next = cur === 'light' ? 'dark' : 'light';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('contradiction_theme', next); } catch (e) {}
      updateThemeButton();
    });

    document.getElementById('shotModeBtn').addEventListener('click', () => {
      state.screenshotMode = !state.screenshotMode;
      document.getElementById('pageWrap').classList.toggle('screenshot-mode', state.screenshotMode);
    });

    document.getElementById('customizeBtn').addEventListener('click', () => {
      const drawer = document.getElementById('customizeDrawer');
      drawer.classList.toggle('hidden');
      if (!drawer.classList.contains('hidden')) renderCustomizeGrid();
    });

    document.getElementById('closeCustomizeBtn').addEventListener('click', () => {
      document.getElementById('customizeDrawer').classList.add('hidden');
    });

    document.getElementById('resetPopularBtn').addEventListener('click', () => {
      popularIds = new Set(DEFAULT_POPULAR_IDS);
      try { localStorage.removeItem('custom_popular_benchmark_ids'); } catch (e) {}
      renderCustomizeGrid();
      renderAll();
    });

    document.getElementById('copyMdBtn').addEventListener('click', copyMarkdownTable);
    document.getElementById('exportCsvBtn').addEventListener('click', exportCsv);
  }

  updateThemeButton();
  bindEvents();
  renderAll();
})();
