async function loadTime() {
  const res = await fetch("/api/time");
  const data = await res.json();
  document.getElementById("server-time").textContent = data.time;
}

async function loadUsers() {
  const res = await fetch("/api/users?page=1&limit=5");
  const data = await res.json();
  let html = "<tr><th>ID</th><th>Name</th></tr>";
  data.users.forEach(u => html += `<tr><td>${u.id}</td><td>${u.name}</td></tr>`);
  document.getElementById("user-table").innerHTML = html;
  document.getElementById("user-count").textContent = data.users.length;
}

async function loadProducts() {
  const res = await fetch("/api/products");
  const data = await res.json();
  const grid = document.getElementById("product-grid");
  data.products.forEach(p => {
    const div = document.createElement("div");
    div.className = "col-md-4 mb-2";
    div.innerHTML = `<div class="card"><div class="card-body">${p.name} - ₹${p.price}</div></div>`;
    grid.appendChild(div);
  });
}

async function loadChart() {
  const res = await fetch("/api/status");
  const data = await res.json();
  new Chart(document.getElementById("statusChart"), {
    type: "bar",
    data: {
      labels: ["App Version", "Uptime"],
      datasets: [{
        label: "Status",
        data: [parseFloat(data.app_version.replace(/\D/g,'')), parseFloat(data.uptime)],
        backgroundColor: ["#0d6efd", "#198754"]
      }]
    }
  });
}

document.getElementById("live-search").addEventListener("input", async e => {
  const q = e.target.value;
  const res = await fetch(`/api/search?q=${q}`);
  const data = await res.json();
  const ul = document.getElementById("search-results");
  ul.innerHTML = "";
  data.results.forEach(u => {
    const li = document.createElement("li");
    li.textContent = u.name;
    ul.appendChild(li);
  });
});

window.addEventListener("DOMContentLoaded", () => {
  loadTime();
  loadUsers();
  loadChart();
});