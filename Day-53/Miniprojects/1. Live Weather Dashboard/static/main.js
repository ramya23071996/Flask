const weatherDiv = document.getElementById("weather-content");
const spinner = document.getElementById("loading-spinner");

async function fetchWeather() {
  spinner.style.display = "inline-block";
  try {
    const res = await fetch("/api/weather");
    const data = await res.json();
    weatherDiv.innerHTML = `
      <p><strong>Temperature:</strong> ${data.temperature}°C</p>
      <p><strong>Humidity:</strong> ${data.humidity}%</p>
      <p><strong>Status:</strong> ${data.status}</p>
      <p><small>Updated: ${data.timestamp}</small></p>
    `;
  } catch (err) {
    weatherDiv.innerHTML = `<div class="alert alert-danger">Failed to load weather data.</div>`;
  } finally {
    spinner.style.display = "none";
  }
}

fetchWeather(); // initial load
setInterval(fetchWeather, 10000); // every 10 seconds