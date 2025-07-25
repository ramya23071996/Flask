document.getElementById('convert-btn').addEventListener('click', () => {
  const amount = document.getElementById('amount').value;
  const currency = document.getElementById('currency').value;

  fetch(`/api/convert?amount=${amount}&to=${currency}`)
    .then(res => res.json())
    .then(data => {
      const result = data.result ? data.result : "Conversion error";
      document.getElementById('result-area').textContent = `Converted Amount: ${result} ${currency}`;
    });
});