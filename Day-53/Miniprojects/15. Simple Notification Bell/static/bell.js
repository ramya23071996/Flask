function fetchNotifications() {
  fetch('/api/notifications')
    .then(res => res.json())
    .then(data => {
      const badge = document.getElementById('notif-badge');
      const list = document.getElementById('notif-list');

      badge.textContent = data.unread_count || 0;
      list.innerHTML = '';

      if (data.notifications.length === 0) {
        list.innerHTML = `<div class="text-muted">You're all caught up!</div>`;
      } else {
        data.notifications.forEach(n => {
          const div = document.createElement('div');
          div.className = 'alert alert-info mb-2';
          div.textContent = n.message;
          list.appendChild(div);
        });
      }
    });
}

// Initial fetch
fetchNotifications();

// Refresh every 10 seconds
setInterval(fetchNotifications, 10000);