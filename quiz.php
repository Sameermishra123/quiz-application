<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz - In Progress</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="quiz-card">
            <div class="quiz-header">
                <div class="question-info">
                    <span id="questionNumber">Question 1</span>
                    <span id="totalQuestions">of 5</span>
                </div>
                <div class="timer-container">
                    <span class="timer-label">Time Left:</span>
                    <span id="timer" class="timer">15</span>
                    <span class="timer-unit">s</span>
                </div>
            </div>
            
            <div class="question-container">
                <h2 id="questionText">Loading question...</h2>
                
                <div class="options-container" id="optionsContainer">
                    <!-- Options will be dynamically loaded -->
                </div>
            </div>
            
            <div class="quiz-footer">
                <button id="prevBtn" class="btn-secondary" disabled>Previous</button>
                <button id="nextBtn" class="btn-primary">Next</button>
                <button id="submitBtn" class="btn-success" style="display: none;">Submit Quiz</button>
            </div>
            
            <div class="progress-bar">
                <div id="progressFill" class="progress-fill"></div>
            </div>
        </div>
    </div>
    
    <script src="questions.js"></script>
    <script src="quiz.js"></script>
</body>
</html>

