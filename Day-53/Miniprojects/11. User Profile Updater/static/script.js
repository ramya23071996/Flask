document.getElementById("edit-form").addEventListener("submit", function(e) {
  e.preventDefault();

  const updatedData = {
    name: document.getElementById("name").value,
    email: document.getElementById("email").value,
    location: document.getElementById("location").value
  };

  fetch("/api/user/1", {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(updatedData)
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === "success") {
      showFlash("Profile updated successfully!", "success");
      setTimeout(() => location.reload(), 1000);
    } else {
      showFlash("Failed to update profile.", "danger");
    }
  });
});

function showFlash(message, type) {
  document.getElementById("flash-area").innerHTML = `
    <div class="alert alert-${type} mt-3" role="alert">${message}</div>`;
}