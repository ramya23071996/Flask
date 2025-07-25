const ctx = document.getElementById("myChart").getContext("2d");
const myChart = new Chart(ctx, {
  type: "bar", // or "pie", "line", etc.
  data: {
    labels: ["Python", "JavaScript", "C++", "Go"],
    datasets: [{
      label: "Votes",
      data: [12, 19, 3, 5],
      backgroundColor: ["#007bff", "#28a745", "#ffc107", "#dc3545"]
    }]
  },
  options: {
    responsive: true,
    scales: {
      y: { beginAtZero: true }
    }
  }
});