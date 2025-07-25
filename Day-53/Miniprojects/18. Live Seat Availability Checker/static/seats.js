function fetchSeats() {
  fetch('/api/seats')
    .then(res => res.json())
    .then(data => {
      Object.entries(data).forEach(([label, isAvailable]) => {
        const btn = document.getElementById(`btn-${label}`);
        if (btn) {
          btn.classList.toggle('btn-success', isAvailable);
          btn.classList.toggle('btn-danger', !isAvailable);
        }
      });
    });
}

// Initial fetch
fetchSeats();

// Refresh every 15 seconds
setInterval(fetchSeats, 15000);