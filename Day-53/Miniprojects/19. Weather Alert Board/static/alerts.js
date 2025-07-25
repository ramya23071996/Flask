function loadAlerts() {
  fetch('/api/weather/alerts')
    .then(res => res.json())
    .then(data => {
      const container = document.getElementById('alert-container');
      container.innerHTML = '';

      if (data.alerts.length === 0) {
        container.innerHTML = `<div class="alert alert-secondary">No alerts for now 🎉</div>`;
        return;
      }

      data.alerts.forEach(message => {
        const alertBox = document.createElement('div');
        alertBox.className = 'alert alert-warning';
        alertBox.textContent = message;
        container.appendChild(alertBox);
      });
    });
}

// Initial load + refresh every 20 seconds
loadAlerts();
setInterval(loadAlerts, 20000);