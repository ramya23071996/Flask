const quoteText = document.getElementById("quoteText");
const getQuoteBtn = document.getElementById("getQuoteBtn");
const loadingSpinner = document.getElementById("loadingSpinner");

getQuoteBtn.addEventListener("click", () => {
  loadingSpinner.classList.remove("d-none");
  fetch("/api/quote")
    .then((response) => response.json())
    .then((data) => {
      quoteText.textContent = data.quote;
    })
    .catch((error) => {
      quoteText.textContent = "Oops! Something went wrong.";
    })
    .finally(() => {
      loadingSpinner.classList.add("d-none");
    });
});