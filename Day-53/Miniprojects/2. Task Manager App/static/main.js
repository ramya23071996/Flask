document.getElementById("task-form").onsubmit = async (e) => {
  e.preventDefault();
  const title = document.getElementById("task-title").value;
  const response = await fetch("/api/tasks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title }),
  });
  const data = await response.json();
  if (response.ok) {
    showAlert("Task added: " + data.title);
    location.reload();
  } else {
    showAlert(data.error, "danger");
  }
};

function showAlert(message, type = "success") {
  const alert = document.getElementById("alert");
  alert.textContent = message;
  alert.className = `alert alert-${type}`;
  alert.classList.remove("d-none");
  setTimeout(() => alert.classList.add("d-none"), 3000);
}