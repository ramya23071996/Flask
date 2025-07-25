const studentList = document.getElementById('student-list');
const scoreDisplay = document.getElementById('score-display');
const loading = document.getElementById('loading');

studentList.addEventListener('click', (e) => {
  const item = e.target.closest('li');
  if (!item) return;
  
  const studentId = item.getAttribute('data-id');
  scoreDisplay.innerHTML = '';
  loading.style.display = 'block';

  fetch(`/api/score/${studentId}`)
    .then(res => res.json())
    .then(data => {
      loading.style.display = 'none';
      if (data.error) {
        scoreDisplay.innerHTML = `<div class="text-danger">${data.error}</div>`;
        return;
      }
      Object.entries(data).forEach(([subject, score]) => {
        const card = document.createElement('div');
        card.className = 'col-md-4';
        card.innerHTML = `
          <div class="card shadow-sm">
            <div class="card-body">
              <h5 class="card-title">${subject}</h5>
              <p class="card-text">Score: ${score}</p>
            </div>
          </div>
        `;
        scoreDisplay.appendChild(card);
      });
    });
});