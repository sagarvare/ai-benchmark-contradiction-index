(function () {
  const rawData = window.CONTRADICTION_BENCHMARKS_DATA || { benchmarks: [], popularBenchmarkIds: [] };
  const allBenchmarks = rawData.benchmarks || [];

  const POPULAR_IDS = new Set(
    rawData.popularBenchmarkIds && rawData.popularBenchmarkIds.length
      ? rawData.popularBenchmarkIds
      : allBenchmarks.filter(b => b.is_popular).map(b => b.id)
  );

  const urlParams = new URLSearchParams(window.location.search);
  const initialView = urlParams.get('view') === 'ALL' ? 'ALL' : 'popular_benchmarks';

  const state = {
    view: initialView, // 'popular_benchmarks' | 'ALL'
    metric: 'all',     // 'all' | 'quality' | 'latency' | 'cost'
    search: '',
    sortBy: 'inverted_desc',
    expandedIds: new Set()
  };

  function cleanModelName(raw) {
    if (!raw) return '';
    let s = raw;
    s = s.replace(/^.*?\+\s*/, '');
    s = s.replace(/^ollama\//i, '');
    s = s.replace(/\s*\((?:Max,\s*Default Fallback|Adaptive Reasoning|Default Thinking|bf16|FP8|high|32k thinking(?: tokens)?|202\d-\d\d-\d\d)\)/gi, '');
    return s.trim();
  }

  function escapeHtml(str) {
    return String(str || '')
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatScore(val, unit, metricType) {
    if (val === null || val === undefined || isNaN(val)) return '';
    const num = Number(val);
    const u = (unit || '').toLowerCase();
    if (metricType === 'cost' || u.includes('$') || u.includes('usd')) {
      return num < 1 ? '$' + num.toFixed(3) : '$' + num.toFixed(2);
    }
    if (u.includes('tokens/sec') || u.includes('tok/s')) {
      return num.toFixed(1) + ' tok/s';
    }
    if (metricType === 'latency' && u.includes('sec')) {
      return num < 10 ? num.toFixed(2) + 's' : num.toFixed(1) + 's';
    }
    if (Math.abs(num) >= 100) return num.toFixed(1);
    if (Math.abs(num) >= 10) return num.toFixed(1);
    return Number(num.toFixed(3)).toString();
  }

  function formatPairItem(p, bench) {
    const mA = escapeHtml(cleanModelName(p.model_a));
    const mB = escapeHtml(cleanModelName(p.model_b));
    const sA = formatScore(p.score_a, bench.unit, bench.metric_type);
    const sB = formatScore(p.score_b, bench.unit, bench.metric_type);

    if (bench.metric_type === 'latency') {
      return `<li class="pair-item"><strong>${mA}</strong> <span class="pair-meta">(#${p.rank_a}, ${sA})</span> faster than <strong>${mB}</strong> <span class="pair-meta">(#${p.rank_b}, ${sB})</span></li>`;
    }
    if (bench.metric_type === 'cost') {
      return `<li class="pair-item"><strong>${mB}</strong> <span class="pair-meta">(${sB})</span> cost more than <strong>${mA}</strong> <span class="pair-meta">(${sA})</span></li>`;
    }
    return `<li class="pair-item"><strong>${mB}</strong> <span class="pair-meta">(#${p.rank_b}, ${sB})</span> ahead of <strong>${mA}</strong> <span class="pair-meta">(#${p.rank_a}, ${sA})</span></li>`;
  }

  function formatMetricLabel(metricType) {
    if (metricType === 'latency') return 'Latency';
    if (metricType === 'cost') return 'Cost';
    return 'Quality';
  }

  function getFilteredAndSorted() {
    const q = state.search.trim().toLowerCase();
    let list = allBenchmarks.filter(b => {
      const c = b.canonical_top25;
      if (!c || c.comparable_pairs_count < 1) return false;
      if (state.view === 'popular_benchmarks' && !POPULAR_IDS.has(b.id)) return false;
      if (state.metric !== 'all' && b.metric_type !== state.metric) return false;
      if (q) {
        const matchBench =
          b.name.toLowerCase().includes(q) ||
          b.suite.toLowerCase().includes(q) ||
          (b.category || '').toLowerCase().includes(q);
        const matchModel = (c.contradictions || []).some(
          p =>
            p.model_a.toLowerCase().includes(q) ||
            p.model_b.toLowerCase().includes(q) ||
            (p.family || '').toLowerCase().includes(q)
        );
        if (!matchBench && !matchModel) return false;
      }
      return true;
    });

    list.sort((a, b) => {
      const ca = a.canonical_top25;
      const cb = b.canonical_top25;
      if (state.sortBy === 'inverted_desc') {
        if (cb.contradictions_count !== ca.contradictions_count) return cb.contradictions_count - ca.contradictions_count;
        if (cb.comparable_pairs_count !== ca.comparable_pairs_count) return cb.comparable_pairs_count - ca.comparable_pairs_count;
        return a.name.localeCompare(b.name);
      }
      if (state.sortBy === 'inverted_asc') {
        if (ca.contradictions_count !== cb.contradictions_count) return ca.contradictions_count - cb.contradictions_count;
        if (cb.comparable_pairs_count !== ca.comparable_pairs_count) return cb.comparable_pairs_count - ca.comparable_pairs_count;
        return a.name.localeCompare(b.name);
      }
      if (state.sortBy === 'comparable_desc') {
        if (cb.comparable_pairs_count !== ca.comparable_pairs_count) return cb.comparable_pairs_count - ca.comparable_pairs_count;
        return cb.contradictions_count - ca.contradictions_count;
      }
      if (state.sortBy === 'comparable_asc') {
        if (ca.comparable_pairs_count !== cb.comparable_pairs_count) return ca.comparable_pairs_count - cb.comparable_pairs_count;
        return cb.contradictions_count - ca.contradictions_count;
      }
      if (state.sortBy === 'name') {
        return a.name.localeCompare(b.name);
      }
      return 0;
    });

    return list;
  }

  function updateHeaderCounts() {
    const validAll = allBenchmarks.filter(b => b.canonical_top25 && b.canonical_top25.comparable_pairs_count >= 1);
    const validPop = validAll.filter(b => POPULAR_IDS.has(b.id));
    document.getElementById('countPopular').textContent = `(${validPop.length})`;
    document.getElementById('countAll').textContent = `(${validAll.length})`;
  }

  function renderTable() {
    const rows = getFilteredAndSorted();
    const tbody = document.getElementById('tableBody');

    if (!rows.length) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center; padding: 32px; color:#6b7280;">No matching benchmarks found.</td></tr>`;
      return;
    }

    const html = [];
    rows.forEach((b, idx) => {
      const c = b.canonical_top25;
      const invCount = c.contradictions_count;
      const compCount = c.comparable_pairs_count;
      const contras = c.contradictions || [];
      const isExpanded = state.expandedIds.has(b.id);

      let examplesHtml = '';
      if (contras.length === 0) {
        examplesHtml = `<span class="none-label">None (all ${compCount} pairs follow expected order)</span>`;
      } else {
        const visible = isExpanded ? contras : contras.slice(0, 2);
        const itemsHtml = visible.map(p => formatPairItem(p, b)).join('');
        let moreHtml = '';
        if (contras.length > 2) {
          moreHtml = isExpanded
            ? `<span class="more-toggle">Show fewer</span>`
            : `<span class="more-toggle">Show all ${contras.length} inverted pairs</span>`;
        }
        examplesHtml = `<ul class="pair-list">${itemsHtml}</ul>${moreHtml}`;
      }

      html.push(`
        <tr class="bench-row" data-id="${escapeHtml(b.id)}">
          <td class="col-rank">${idx + 1}</td>
          <td class="col-name">
            <div class="bench-title">${escapeHtml(b.name)}</div>
            <div class="bench-suite">${escapeHtml(b.suite)}</div>
          </td>
          <td class="col-metric">${formatMetricLabel(b.metric_type)}</td>
          <td class="col-num">
            <span class="num-inverted ${invCount === 0 ? 'zero' : ''}">${invCount}</span>
          </td>
          <td class="col-num">
            <span class="num-comparable">${compCount}</span>
          </td>
          <td class="col-examples">${examplesHtml}</td>
        </tr>
      `);
    });

    tbody.innerHTML = html.join('');

    tbody.querySelectorAll('tr.bench-row').forEach(tr => {
      tr.addEventListener('click', () => {
        const id = tr.getAttribute('data-id');
        if (state.expandedIds.has(id)) {
          state.expandedIds.delete(id);
        } else {
          state.expandedIds.add(id);
        }
        renderTable();
      });
    });
  }

  function updateSortHeaders() {
    document.querySelectorAll('#benchmarksTable thead th.sortable').forEach(th => {
      th.classList.remove('active-sort');
      const base = th.getAttribute('data-sort');
      if (base === 'name') {
        th.textContent = state.sortBy === 'name' ? 'Benchmark ↑' : 'Benchmark';
        if (state.sortBy === 'name') th.classList.add('active-sort');
      } else if (base === 'inverted_desc') {
        if (state.sortBy === 'inverted_desc') {
          th.textContent = 'Inverted Pairs ↓';
          th.classList.add('active-sort');
        } else if (state.sortBy === 'inverted_asc') {
          th.textContent = 'Inverted Pairs ↑';
          th.classList.add('active-sort');
        } else {
          th.textContent = 'Inverted Pairs';
        }
      } else if (base === 'comparable_desc') {
        if (state.sortBy === 'comparable_desc') {
          th.textContent = 'Comparable Pairs ↓';
          th.classList.add('active-sort');
        } else if (state.sortBy === 'comparable_asc') {
          th.textContent = 'Comparable Pairs ↑';
          th.classList.add('active-sort');
        } else {
          th.textContent = 'Comparable Pairs';
        }
      }
    });
  }

  function setView(v) {
    state.view = v;
    document.getElementById('btnPopular').classList.toggle('active', v === 'popular_benchmarks');
    document.getElementById('btnAll').classList.toggle('active', v === 'ALL');
    const url = new URL(window.location.href);
    url.searchParams.set('view', v);
    window.history.replaceState({}, '', url.toString());
    renderTable();
  }

  function init() {
    updateHeaderCounts();
    setView(state.view);

    document.getElementById('btnPopular').addEventListener('click', () => setView('popular_benchmarks'));
    document.getElementById('btnAll').addEventListener('click', () => setView('ALL'));

    document.getElementById('metricFilter').addEventListener('change', e => {
      state.metric = e.target.value;
      renderTable();
    });

    document.getElementById('searchInput').addEventListener('input', e => {
      state.search = e.target.value;
      renderTable();
    });

    document.querySelectorAll('#benchmarksTable thead th.sortable').forEach(th => {
      th.addEventListener('click', () => {
        const col = th.getAttribute('data-sort');
        if (col === 'inverted_desc') {
          state.sortBy = state.sortBy === 'inverted_desc' ? 'inverted_asc' : 'inverted_desc';
        } else if (col === 'comparable_desc') {
          state.sortBy = state.sortBy === 'comparable_desc' ? 'comparable_asc' : 'comparable_desc';
        } else if (col === 'name') {
          state.sortBy = 'name';
        }
        updateSortHeaders();
        renderTable();
      });
    });
  }

  init();
})();
