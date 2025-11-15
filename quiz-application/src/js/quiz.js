document.addEventListener('DOMContentLoaded', function() {
    const questionsContainer = document.getElementById('questions-container');
    const quizForm = document.getElementById('quiz-form');
    const timerDisplay = document.getElementById('time');
    let questions = [];
    let timer;
    let timeLeft = 60; // 60 seconds total

    // Get category from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const category = urlParams.get('category') || 'science';

    function loadQuestions() {
        // Use absolute path from server root
        const apiPath = `/quiz-application/src/php/api/get_quiz.php?category=${category}`;
        fetch(apiPath)
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                if (data.error) {
                    console.error('Error:', data.error);
                    questionsContainer.innerHTML = `<p>Error loading questions: ${data.error}</p>`;
                    return;
                }
                if (!data || data.length === 0) {
                    console.error('No questions received');
                    questionsContainer.innerHTML = '<p>No questions available for this category.</p>';
                    return;
                }
                questions = data;
                renderQuestions(data);
                startTimer();
            })
            .catch(error => {
                console.error('Error fetching quiz:', error);
                questionsContainer.innerHTML = `<p>Error loading quiz: ${error.message}</p>`;
            });
    }

    function renderQuestions(questionsData) {
        questionsContainer.innerHTML = '';
        questionsData.forEach((question, index) => {
            const questionDiv = document.createElement('div');
            questionDiv.className = 'question-item';
            questionDiv.innerHTML = `
                <h3>${question.question}</h3>
                ${question.options.map((option, i) => `
                    <div>
                        <input type="radio" name="question${index}" id="q${index}opt${i}" value="${option}">
                        <label for="q${index}opt${i}">${option}</label>
                    </div>
                `).join('')}
            `;
            questionsContainer.appendChild(questionDiv);
        });
    }

    function startTimer() {
        if (timer) clearInterval(timer);
        timeLeft = 60;
        if (timerDisplay) {
            timerDisplay.textContent = timeLeft;
        }
        timer = setInterval(() => {
            timeLeft--;
            if (timerDisplay) {
                timerDisplay.textContent = timeLeft;
            }
            if (timeLeft <= 0) {
                clearInterval(timer);
                submitQuiz();
            }
        }, 1000);
    }

    function submitQuiz() {
        clearInterval(timer);
        const formData = new FormData(quizForm);
        const answers = {};
        
        questions.forEach((question, index) => {
            const selected = document.querySelector(`input[name="question${index}"]:checked`);
            if (selected) {
                answers[index] = selected.value;
            }
        });

        fetch('/quiz-application/src/php/api/submit_quiz.php', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ answers, questions })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            window.location.href = '/quiz-application/src/html/results.html';
        })
        .catch(error => {
            console.error('Error submitting quiz:', error);
            alert('Error submitting quiz. Please try again.');
        });
    }

    quizForm.addEventListener('submit', function(e) {
        e.preventDefault();
        submitQuiz();
    });

    loadQuestions();
});