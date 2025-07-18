document.addEventListener("DOMContentLoaded", () => {
    const questions = document.querySelectorAll(".faq-question");
    questions.forEach(btn => {
        btn.addEventListener("click", () => {
            const answer = btn.nextElementSibling;
            answer.style.display = answer.style.display === "block" ? "none" : "block";
        });
    });
});