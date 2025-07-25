let prevCount = parseInt(document.getElementById("userCountBadge").textContent);

function fetchUserCount() {
  fetch("/api/users/count")
    .then(res => res.json())
    .then(data => {
      const badge = document.getElementById("userCountBadge");
      const flashAlert = document.getElementById("flashAlert");

      if (data.count > prevCount) {
        flashAlert.classList.remove("d-none");
        setTimeout(() => flashAlert.classList.add("d-none"), 3000);
      }

      badge.textContent = data.count;
      prevCount = data.count;
    })
    .catch(() => {
      console.error("Count fetch failed.");
    });
}

// Poll every 5 seconds
setInterval(fetchUserCount, 5000);