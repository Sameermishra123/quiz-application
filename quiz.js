// Quiz state management
let currentQuestionIndex = 0;
let questions = [];
let userAnswers = [];
let timeSpent = [];
let timerInterval = null;
let currentTimer = 0;
let timerDuration = 15; // Default 15 seconds per question

// Initialize quiz
document.addEventListener('DOMContentLoaded', function() {
    const category = localStorage.getItem('selectedCategory');
    const difficulty = localStorage.getItem('selectedDifficulty');
    
    if (!category || !difficulty) {
        alert('Please select category and difficulty first!');
        window.location.href = 'index.php';
        return;
    }
    
    // Load questions based on category and difficulty
    if (quizData[category] && quizData[category][difficulty]) {
        questions = quizData[category][difficulty];
        
        // Initialize arrays
        userAnswers = new Array(questions.length).fill(null);
        timeSpent = new Array(questions.length).fill(0);
        
        // Set timer duration based on difficulty
        if (difficulty === 'easy') {
            timerDuration = 20;
        } else if (difficulty === 'medium') {
            timerDuration = 15;
        } else {
            timerDuration = 10;
        }
        
        // Load first question
        loadQuestion(0);
    } else {
        alert('Questions not found for selected category and difficulty!');
        window.location.href = 'index.php';
    }
});

// Load question at given index
function loadQuestion(index) {
    if (index < 0 || index >= questions.length) return;
    
    // Clear previous timer
    clearInterval(timerInterval);
    
    currentQuestionIndex = index;
    const question = questions[index];
    
    // Update question number
    document.getElementById('questionNumber').textContent = `Question ${index + 1}`;
    document.getElementById('totalQuestions').textContent = `of ${questions.length}`;
    
    // Update question text
    document.getElementById('questionText').textContent = question.question;
    
    // Load options
    const optionsContainer = document.getElementById('optionsContainer');
    optionsContainer.innerHTML = '';
    
    question.options.forEach((option, optionIndex) => {
        const optionDiv = document.createElement('div');
        optionDiv.className = 'option-item';
        
        const radio = document.createElement('input');
        radio.type = 'radio';
        radio.name = 'answer';
        radio.id = `option${optionIndex}`;
        radio.value = optionIndex;
        
        // Check if user has already answered
        if (userAnswers[index] === optionIndex) {
            radio.checked = true;
        }
        
        radio.addEventListener('change', function() {
            userAnswers[index] = parseInt(this.value);
            saveProgress();
        });
        
        const label = document.createElement('label');
        label.htmlFor = `option${optionIndex}`;
        label.textContent = option;
        
        optionDiv.appendChild(radio);
        optionDiv.appendChild(label);
        optionsContainer.appendChild(optionDiv);
    });
    
    // Update navigation buttons
    document.getElementById('prevBtn').disabled = index === 0;
    
    if (index === questions.length - 1) {
        document.getElementById('nextBtn').style.display = 'none';
        document.getElementById('submitBtn').style.display = 'inline-block';
    } else {
        document.getElementById('nextBtn').style.display = 'inline-block';
        document.getElementById('submitBtn').style.display = 'none';
    }
    
    // Update progress bar
    const progress = ((index + 1) / questions.length) * 100;
    document.getElementById('progressFill').style.width = progress + '%';
    
    // Start timer
    startTimer();
}

// Start timer for current question
function startTimer() {
    currentTimer = timerDuration;
    document.getElementById('timer').textContent = currentTimer;
    
    timerInterval = setInterval(function() {
        currentTimer--;
        document.getElementById('timer').textContent = currentTimer;
        timeSpent[currentQuestionIndex] = timerDuration - currentTimer;
        
        if (currentTimer <= 0) {
            clearInterval(timerInterval);
            handleTimerExpiry();
        }
    }, 1000);
}

// Handle timer expiry
function handleTimerExpiry() {
    // Auto-save current answer (if any)
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    if (selectedOption) {
        userAnswers[currentQuestionIndex] = parseInt(selectedOption.value);
    }
    
    // Save time spent
    timeSpent[currentQuestionIndex] = timerDuration;
    
    saveProgress();
    
    // Move to next question or submit
    if (currentQuestionIndex < questions.length - 1) {
        loadQuestion(currentQuestionIndex + 1);
    } else {
        submitQuiz();
    }
}

// Save progress to localStorage
function saveProgress() {
    const quizProgress = {
        category: localStorage.getItem('selectedCategory'),
        difficulty: localStorage.getItem('selectedDifficulty'),
        userAnswers: userAnswers,
        timeSpent: timeSpent,
        questions: questions
    };
    localStorage.setItem('quizProgress', JSON.stringify(quizProgress));
}

// Previous button handler
document.getElementById('prevBtn').addEventListener('click', function() {
    if (currentQuestionIndex > 0) {
        // Save current answer before moving
        const selectedOption = document.querySelector('input[name="answer"]:checked');
        if (selectedOption) {
            userAnswers[currentQuestionIndex] = parseInt(selectedOption.value);
        }
        saveProgress();
        loadQuestion(currentQuestionIndex - 1);
    }
});

// Next button handler
document.getElementById('nextBtn').addEventListener('click', function() {
    if (currentQuestionIndex < questions.length - 1) {
        // Save current answer before moving
        const selectedOption = document.querySelector('input[name="answer"]:checked');
        if (selectedOption) {
            userAnswers[currentQuestionIndex] = parseInt(selectedOption.value);
        }
        saveProgress();
        loadQuestion(currentQuestionIndex + 1);
    }
});

// Submit button handler
document.getElementById('submitBtn').addEventListener('click', function() {
    // Save current answer before submitting
    const selectedOption = document.querySelector('input[name="answer"]:checked');
    if (selectedOption) {
        userAnswers[currentQuestionIndex] = parseInt(selectedOption.value);
    }
    submitQuiz();
});

// Submit quiz
function submitQuiz() {
    clearInterval(timerInterval);
    
    // Calculate results
    let correctAnswers = 0;
    let incorrectAnswers = 0;
    
    questions.forEach((question, index) => {
        if (userAnswers[index] !== null && userAnswers[index] === question.answer) {
            correctAnswers++;
        } else {
            incorrectAnswers++;
        }
    });
    
    // Save final results
    const results = {
        totalQuestions: questions.length,
        correctAnswers: correctAnswers,
        incorrectAnswers: incorrectAnswers,
        scorePercentage: ((correctAnswers / questions.length) * 100).toFixed(2),
        timeSpent: timeSpent,
        userAnswers: userAnswers,
        questions: questions
    };
    
    localStorage.setItem('quizResults', JSON.stringify(results));
    
    // Redirect to result page
    window.location.href = 'result.php';
}

