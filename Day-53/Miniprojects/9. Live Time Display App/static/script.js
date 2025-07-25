const badge = document.getElementById("time-badge");

function updateTime() {
  fetch("/api/time")
    .then(response => response.json())
    .then(data => {
      badge.style.opacity = 0.5;
      badge.textContent = data.time;
      setTimeout(() => badge.style.opacity = 1, 200); // simple fade-in
    });
}

setInterval(updateTime, 1000);