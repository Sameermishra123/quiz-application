document.addEventListener('DOMContentLoaded', function() {
    const quizContainer = document.getElementById('quiz-container');
    const resultContainer = document.getElementById('result-container');
    const timerDisplay = document.getElementById('timer');
    let currentQuestionIndex = 0;
    let score = 0;
    let timer;
    const totalQuestions = 10; // Adjust based on your quiz

    function loadQuestion() {
        fetch('api/get_quiz.php')
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    const question = data[currentQuestionIndex];
                    displayQuestion(question);
                } else {
                    showResults();
                }
            })
            .catch(error => console.error('Error fetching quiz:', error));
    }

    function displayQuestion(question) {
        quizContainer.innerHTML = `
            <h2>${question.question}</h2>
            ${question.answers.map((answer, index) => `
                <div>
                    <input type="radio" name="answer" id="answer${index}" value="${answer}">
                    <label for="answer${index}">${answer}</label>
                </div>
            `).join('')}
            <button id="next-button">Next</button>
        `;
        document.getElementById('next-button').addEventListener('click', checkAnswer);
        startTimer();
    }

    function checkAnswer() {
        const selectedAnswer = document.querySelector('input[name="answer"]:checked');
        if (selectedAnswer) {
            if (selectedAnswer.value === currentQuestion.correctAnswer) {
                score++;
            }
            currentQuestionIndex++;
            if (currentQuestionIndex < totalQuestions) {
                loadQuestion();
            } else {
                showResults();
            }
        } else {
            alert('Please select an answer before proceeding.');
        }
    }

    function showResults() {
        clearInterval(timer);
        quizContainer.style.display = 'none';
        resultContainer.innerHTML = `
            <h2>Your Score: ${score} / ${totalQuestions}</h2>
            <button id="restart-button">Restart Quiz</button>
        `;
        document.getElementById('restart-button').addEventListener('click', restartQuiz);
    }

    function restartQuiz() {
        currentQuestionIndex = 0;
        score = 0;
        resultContainer.innerHTML = '';
        quizContainer.style.display = 'block';
        loadQuestion();
    }

    function startTimer() {
        let timeLeft = 30; // 30 seconds for each question
        timerDisplay.textContent = `Time Left: ${timeLeft}s`;
        timer = setInterval(() => {
            timeLeft--;
            timerDisplay.textContent = `Time Left: ${timeLeft}s`;
            if (timeLeft <= 0) {
                clearInterval(timer);
                alert('Time is up!');
                checkAnswer(); // Automatically check answer if time runs out
            }
        }, 1000);
    }

    loadQuestion();
});