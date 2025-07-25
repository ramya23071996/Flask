function updateClock() {
  fetch('/api/time')
    .then(res => res.json())
    .then(data => {
      const { hour, minute, second } = data;
      const formatted = `${hour.toString().padStart(2, '0')} : ${minute.toString().padStart(2, '0')} : ${second.toString().padStart(2, '0')}`;
      document.getElementById('clock-panel').textContent = formatted;
    });
}

// Refresh every second
setInterval(updateClock, 1000);

// Initial tick
updateClock();