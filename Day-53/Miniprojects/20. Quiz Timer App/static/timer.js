const QUIZ_DURATION = 120; // Must match backend
const bar = document.getElementById('timer-bar');
const text = document.getElementById('timer-text');
const form = document.getElementById('quiz-form');

function fetchTime() {
  fetch('/api/timer')
    .then(res => res.json())
    .then(data => {
      const remaining = data.remaining;
      const percent = Math.round((remaining / QUIZ_DURATION) * 100);
      bar.style.width = `${percent}%`;
      bar.classList.toggle('bg-success', remaining > 30);
      bar.classList.toggle('bg-warning', remaining <= 30 && remaining > 10);
      bar.classList.toggle('bg-danger', remaining <= 10);
      text.textContent = `Time left: ${remaining}s`;

      if (remaining <= 0) {
        form.querySelectorAll('input').forEach(i => i.disabled = true);
        form.querySelector('button[type="submit"]').disabled = true;
        text.textContent = "Time's up!";
        bar.style.width = "100%";
      }
    });
}

// Tick every second
setInterval(fetchTime, 1000);
fetchTime();