const DATA_URL = "data/dashboard.json";

const groupLabels = {
  top_5: "Top 5",
  picks_6_14: "Picks 6-14",
  picks_15_30: "Picks 15-30",
  second_round: "Second round",
  undrafted: "Undrafted"
};

function formatPct(value) {
  if (value === null || value === undefined || Number.isNaN(value)) return "n/a";
  return `${Math.round(value * 1000) / 10}%`;
}

function formatValue(value) {
  if (value === null || value === undefined || value === "") return "";
  if (typeof value === "number") {
    return Number.isInteger(value) ? String(value) : String(Math.round(value * 1000) / 1000);
  }
  return String(value);
}

function labelize(key) {
  if (groupLabels[key]) return groupLabels[key];
  return String(key).replaceAll("_", " ").replace(/\b\w/g, char => char.toUpperCase());
}

function metricCard(title, value, detail) {
  return `
    <article class="metric-card">
      <h3>${title}</h3>
      <span class="metric-value">${value}</span>
      <small>${detail}</small>
    </article>
  `;
}

function renderMetrics(data) {
  const metrics = document.querySelector("#metrics");
  const agreement = data.mode === "post_draft_evaluation" ? data.model_vs_espn : data.agreement;
  metrics.innerHTML = [
    metricCard("Exact Agreement", formatPct(agreement.accuracy), `${agreement.exact_matches} exact agreements from ${agreement.n} compared players`)
  ].join("");
}

function renderDistribution(data) {
  const root = document.querySelector("#distributionCharts");
  root.innerHTML = "";

  if (data.mode === "post_draft_evaluation") {
    data = {
      ...data,
      distributions: {
        model: data.distributions.model,
        espn: data.distributions.espn
      }
    };
  }

  Object.entries(data.distributions || {}).forEach(([name, rows]) => {
    const max = Math.max(1, ...rows.map(row => row.count));
    const bars = rows.map(row => `
      <div class="bar-row">
        <span>${row.label}</span>
        <div class="bar-track"><div class="bar-fill" style="width: ${(row.count / max) * 100}%"></div></div>
        <strong>${row.count}</strong>
      </div>
    `).join("");
    root.insertAdjacentHTML("beforeend", `<article class="chart-card"><h3>${labelize(name)}</h3>${bars}</article>`);
  });
}

function renderMatrixCard(key, matrixData) {
  const headers = matrixData.groups.map(group => `<th>${group.label}</th>`).join("");
  const rows = matrixData.matrix.map((row, index) => {
    const cells = row.map(value => `<td>${value}</td>`).join("");
    return `<tr><th>${matrixData.groups[index].label}</th>${cells}</tr>`;
  }).join("");
  return `
    <article class="matrix-card">
      <h3>${labelize(key)}</h3>
      <div class="matrix-scroll">
        <table class="matrix-table">
          <thead><tr><th></th>${headers}</tr></thead>
          <tbody>${rows}</tbody>
        </table>
      </div>
    </article>
  `;
}

function renderMatrices(data) {
  const root = document.querySelector("#matrices");
  root.innerHTML = Object.entries(data.confusion_matrices || {})
    .map(([key, matrix]) => renderMatrixCard(key, matrix))
    .join("");
}

function renderTable(selector, rows, columns) {
  const table = document.querySelector(selector);
  if (!rows || rows.length === 0) {
    table.innerHTML = "<tbody><tr><td>No rows available.</td></tr></tbody>";
    return;
  }

  const cols = columns.filter(col => rows.some(row => row[col] !== undefined && row[col] !== null));
  const head = cols.map(col => `<th>${labelize(col)}</th>`).join("");
  const body = rows.map(row => {
    const cells = cols.map(col => {
      const value = row[col];
      const rendered = col.includes("group") && value ? `<span class="group-pill">${labelize(value)}</span>` : formatValue(value);
      return `<td>${rendered}</td>`;
    }).join("");
    return `<tr>${cells}</tr>`;
  }).join("");
  table.innerHTML = `<thead><tr>${head}</tr></thead><tbody>${body}</tbody>`;
}

async function loadDashboard() {
  const response = await fetch(DATA_URL);
  if (!response.ok) throw new Error(`Could not load ${DATA_URL}`);
  const data = await response.json();

  document.querySelector("#summary").textContent = data.summary;
  document.querySelector("#modeLabel").textContent = data.mode_label;
  document.querySelector("#generatedAt").textContent = `Generated ${new Date(data.generated_at).toLocaleString()}`;
  document.querySelector("#modeNote").textContent = data.note;

  renderMetrics(data);
  renderDistribution(data);
  renderMatrices(data);

  renderTable("#disagreementsTable", data.largest_disagreements, ["name", "display_name", "model_group", "espn_group", "gap", "model_espn_gap"]);
  renderTable("#boardTable", data.top_model_board, [
    "model_rank",
    "name",
    "position",
    "organization",
    "model_group",
    "espn_group"
  ]);

  if (data.three_way_comparison) {
    document.querySelector("#threeWaySection").classList.remove("hidden");
    renderTable("#threeWayTable", data.three_way_comparison, ["display_name", "overall_pick", "actual_group", "model_group", "espn_group", "mock_pick"]);
  }

}

loadDashboard().catch(error => {
  document.querySelector("#summary").textContent = error.message;
  document.querySelector("#modeNote").textContent = "Run python scripts/build_dashboard.py to generate docs/data/dashboard.json.";
});
