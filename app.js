(function () {
  const rawData = window.CONTRADICTION_BENCHMARKS_DATA || { benchmarks: [], popularBenchmarkIds: [] };
  const allBenchmarks = rawData.benchmarks || [];

  const POPULAR_IDS = new Set(
    rawData.popularBenchmarkIds && rawData.popularBenchmarkIds.length
      ? rawData.popularBenchmarkIds
      : allBenchmarks.filter(b => b.is_popular).map(b => b.id)
  );

  const urlParams = new URLSearchParams(window.location.search);
  const state = {
    view: urlParams.get('view') === 'ALL' ? 'ALL' : 'popular_benchmarks'
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

  function getSortedBenchmarks() {
    const list = allBenchmarks.filter(b => {
      const c = b.canonical_top25;
      if (!c || c.comparable_pairs_count < 1) return false;
      if (state.view === 'popular_benchmarks' && !POPULAR_IDS.has(b.id)) return false;
      return true;
    });

    // Sort low to high by Inverted Score (contradictions_count ascending),
    // tiebroken by comparable_pairs_count descending, then name ascending
    list.sort((a, b) => {
      const ca = a.canonical_top25;
      const cb = b.canonical_top25;
      if (ca.contradictions_count !== cb.contradictions_count) {
        return ca.contradictions_count - cb.contradictions_count;
      }
      if (cb.comparable_pairs_count !== ca.comparable_pairs_count) {
        return cb.comparable_pairs_count - ca.comparable_pairs_count;
      }
      return a.name.localeCompare(b.name);
    });

    return list;
  }

  function render() {
    const btnPop = document.getElementById('btnPopular');
    const btnAll = document.getElementById('btnAll');
    if (btnPop && btnAll) {
      btnPop.classList.toggle('active', state.view === 'popular_benchmarks');
      btnAll.classList.toggle('active', state.view === 'ALL');
    }

    const list = getSortedBenchmarks();
    const tbody = document.getElementById('tableBody');
    if (!tbody) return;

    const rowsHtml = list.map(b => {
      const c = b.canonical_top25;
      const inv = c.contradictions_count;
      const pairs = c.contradictions || [];

      let examplesHtml = '';
      if (pairs.length === 0) {
        examplesHtml = `<span class="none-label">None</span>`;
      } else {
        const shown = pairs.slice(0, 3);
        const itemsHtml = shown.map(p => formatPairItem(p, b)).join('');
        const extra = pairs.length > 3
          ? `<li class="pair-meta">+${pairs.length - 3} more</li>`
          : '';
        examplesHtml = `<ul class="pair-list">${itemsHtml}${extra}</ul>`;
      }

      return `
        <tr>
          <td class="col-name">${escapeHtml(b.name)}</td>
          <td class="col-score">${inv}</td>
          <td class="col-examples">${examplesHtml}</td>
        </tr>
      `;
    }).join('');

    tbody.innerHTML = rowsHtml;
  }

  function bindEvents() {
    const btnPop = document.getElementById('btnPopular');
    const btnAll = document.getElementById('btnAll');

    if (btnPop) {
      btnPop.addEventListener('click', () => {
        state.view = 'popular_benchmarks';
        const url = new URL(window.location);
        url.searchParams.set('view', 'popular_benchmarks');
        window.history.replaceState({}, '', url);
        render();
      });
    }

    if (btnAll) {
      btnAll.addEventListener('click', () => {
        state.view = 'ALL';
        const url = new URL(window.location);
        url.searchParams.set('view', 'ALL');
        window.history.replaceState({}, '', url);
        render();
      });
    }
  }

  bindEvents();
  render();
})();
