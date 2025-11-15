function startTimer(duration, display) {
    let timer = duration, minutes, seconds;
    const interval = setInterval(function () {
        minutes = parseInt(timer / 60, 10);
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;

        display.textContent = minutes + ":" + seconds;

        if (--timer < 0) {
            clearInterval(interval);
            display.textContent = "Time's up!";
            // Trigger quiz submission or any other action when time is up
            submitQuiz();
        }
    }, 1000);
}

function submitQuiz() {
    // Logic to submit the quiz answers
    // This function should be defined in quiz.js or similar
}

// Example usage
window.onload = function () {
    const timeLimit = 300; // 5 minutes
    const display = document.querySelector('#time'); // Ensure there's an element with id 'time'
    startTimer(timeLimit, display);
};