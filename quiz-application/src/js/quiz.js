document.addEventListener('DOMContentLoaded', function() {
    const questionsContainer = document.getElementById('questions-container');
    const quizForm = document.getElementById('quiz-form');
    const timerDisplay = document.getElementById('time');
    let questions = [];
    let timer;
    let timeLeft = 60; // 60 seconds total

    // Fallback static questions - load these immediately
    const fallbackQuestions = [
        {
            question: "What is 2 + 2?",
            options: ["1", "2", "4", "6"],
            answer: "4"
        },
        {
            question: "Which language is used for web apps?",
            options: ["Python", "JavaScript", "C++", "Java"],
            answer: "JavaScript"
        }
    ];

    // Get category from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    const category = urlParams.get('category') || 'general';

    // Load fallback questions immediately so container is populated
    if (questionsContainer) {
        questions = fallbackQuestions;
        renderQuestions(fallbackQuestions);
        startTimer();
    }

    function loadQuestions() {
        // Try multiple API paths
        const apiPaths = [
            `../php/api/get_quiz.php?category=${category}`,
            `/quiz-application/src/php/api/get_quiz.php?category=${category}`,
            `src/php/api/get_quiz.php?category=${category}`
        ];
        
        function tryFetch(pathIndex) {
            if (pathIndex >= apiPaths.length) {
                // All paths failed, keep fallback questions (already loaded)
                console.warn('API fetch failed, using fallback questions');
                return;
            }
            
            fetch(apiPaths[pathIndex])
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    if (data.error) {
                        console.error('Error:', data.error);
                        throw new Error(data.error);
                    }
                    if (!data || data.length === 0) {
                        console.error('No questions received');
                        throw new Error('No questions available');
                    }
                    // Update with API questions if successful
                    questions = data;
                    renderQuestions(data);
                })
                .catch(error => {
                    console.error(`Error fetching quiz from ${apiPaths[pathIndex]}:`, error);
                    // Try next path
                    tryFetch(pathIndex + 1);
                });
        }
        
        // Try to fetch from API in background (fallback already loaded)
        tryFetch(0);
    }

    function renderQuestions(questionsData) {
        if (!questionsContainer) {
            console.error('questions-container element not found');
            return;
        }
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
            window.location.href = 'results.html';
        })
        .catch(error => {
            console.error('Error submitting quiz:', error);
            // Fallback: use localStorage and redirect
            localStorage.setItem('score', JSON.stringify(answers));
            window.location.href = 'results.html';
        });
    }

    if (quizForm) {
        quizForm.addEventListener('submit', function(e) {
            e.preventDefault();
            submitQuiz();
        });
    }

    // Try to load from API (fallback already shown above)
    if (questionsContainer) {
        loadQuestions();
    } else {
        console.error('questions-container element not found in DOM');
    }
});
