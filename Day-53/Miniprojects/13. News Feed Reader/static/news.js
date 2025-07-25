document.addEventListener('DOMContentLoaded', () => {
  const categorySelect = document.getElementById('category-select');
  const accordion = document.getElementById('newsAccordion');
  const loading = document.getElementById('loading');

  function fetchNews(category) {
    loading.style.display = 'block';
    accordion.innerHTML = '';

    fetch(`/api/news?category=${category}`)
      .then(res => res.json())
      .then(data => {
        loading.style.display = 'none';
        const headlines = data.headlines;
        headlines.forEach((title, idx) => {
          const item = document.createElement('div');
          item.className = 'accordion-item';
          item.innerHTML = `
            <h2 class="accordion-header" id="heading${idx}">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${idx}" aria-expanded="false" aria-controls="collapse${idx}">
                ${title}
              </button>
            </h2>
            <div id="collapse${idx}" class="accordion-collapse collapse" aria-labelledby="heading${idx}" data-bs-parent="#newsAccordion">
              <div class="accordion-body">More details about: ${title}</div>
            </div>
          `;
          accordion.appendChild(item);
        });
      });
  }

  fetchNews(categorySelect.value);

  categorySelect.addEventListener('change', () => {
    fetchNews(categorySelect.value);
  });
});