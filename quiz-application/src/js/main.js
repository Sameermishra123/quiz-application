document.addEventListener('DOMContentLoaded', function() {
    const startButton = document.getElementById('start-quiz');
    const quizContainer = document.getElementById('quiz-container');
    const resultsContainer = document.getElementById('results-container');
    const timerDisplay = document.getElementById('timer');
    let timer;
    let timeLeft = 60; // Set the timer for 60 seconds

    startButton.addEventListener('click', function() {
        startQuiz();
    });

    function startQuiz() {
        quizContainer.style.display = 'block';
        startButton.style.display = 'none';
        loadQuestions();
        startTimer();
    }

    function loadQuestions() {
        // Fetch questions from the API
        fetch('api/get_quiz.php')
            .then(response => response.json())
            .then(data => {
                // Render questions in the quiz container
                renderQuestions(data);
            })
            .catch(error => console.error('Error fetching quiz questions:', error));
    }

    function renderQuestions(questions) {
        // Logic to display questions in the quiz container
        questions.forEach((question, index) => {
            const questionElement = document.createElement('div');
            questionElement.innerHTML = `
                <h3>${question.question}</h3>
                ${question.options.map((option, i) => `
                    <label>
                        <input type="radio" name="question${index}" value="${option}">
                        ${option}
                    </label>
                `).join('')}
            `;
            quizContainer.appendChild(questionElement);
        });
    }

    function startTimer() {
        timer = setInterval(function() {
            if (timeLeft <= 0) {
                clearInterval(timer);
                submitQuiz();
            } else {
                timerDisplay.textContent = timeLeft + ' seconds remaining';
                timeLeft--;
            }
        }, 1000);
    }

    function submitQuiz() {
        clearInterval(timer);
        const answers = Array.from(quizContainer.querySelectorAll('input[type="radio"]:checked')).map(input => input.value);
        fetch('api/submit_quiz.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ answers })
        })
        .then(response => response.json())
        .then(data => {
            displayResults(data);
        })
        .catch(error => console.error('Error submitting quiz:', error));
    }

    function displayResults(data) {
        quizContainer.style.display = 'none';
        resultsContainer.style.display = 'block';
        // Logic to display results and charts using Chart.js
        renderResults(data);
    }

    function renderResults(data) {
        // Example of rendering results
        resultsContainer.innerHTML = `
            <h2>Your Score: ${data.score}</h2>
            <canvas id="resultsChart"></canvas>
        `;
        const ctx = document.getElementById('resultsChart').getContext('2d');
        const chart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.labels,
                datasets: [{
                    label: 'Score',
                    data: data.scores,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                }
            }
        });
    }
});