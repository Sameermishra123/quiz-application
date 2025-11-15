document.addEventListener('DOMContentLoaded', function() {
    const startQuizBtn = document.getElementById("start-quiz");

    if (startQuizBtn) {
        startQuizBtn.addEventListener("click", function (e) {
            e.preventDefault();
            // Redirect to quiz page
            window.location.href = "quiz.html";
        });
    }
});
