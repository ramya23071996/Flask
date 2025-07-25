function pollMessageCount() {
  fetch('/api/messages/count')
    .then(res => res.json())
    .then(data => {
      const countEl = document.getElementById('msg-count');
      countEl.textContent = data.count;
    });
}

// Initial fetch
pollMessageCount();

// Poll every 5 seconds
setInterval(pollMessageCount, 5000);