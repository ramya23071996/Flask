document.getElementById('feedback-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const name = document.getElementById('name').value.trim();
  const message = document.getElementById('message').value.trim();

  fetch('/api/feedback', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ name, message })
  })
  .then(res => res.json())
  .then(data => {
    if (data.status === 'success') {
      showAlert("Thank you for your feedback!", "success");
      loadFeedback();
      this.reset();
    } else {
      showAlert("Please fill out all fields.", "danger");
    }
  });
});

function showAlert(message, type) {
  document.getElementById('alert-area').innerHTML = `
    <div class="alert alert-${type} mt-2" role="alert">${message}</div>`;
}

function loadFeedback() {
  fetch('/api/feedbacks')
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById('feedback-list');
      list.innerHTML = '';
      data.feedbacks.forEach(fb => {
        const item = document.createElement('li');
        item.className = 'list-group-item';
        item.textContent = `${fb.name}: ${fb.message}`;
        list.appendChild(item);
      });
    });
}

window.onload = loadFeedback;