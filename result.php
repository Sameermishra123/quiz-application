<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Results</title>
    <link rel="stylesheet" href="styles.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <div class="container">
        <div class="result-card">
            <h1>Quiz Results</h1>
            
            <div class="result-summary">
                <div class="summary-item">
                    <span class="summary-label">Total Questions</span>
                    <span class="summary-value" id="totalQuestions">0</span>
                </div>
                <div class="summary-item correct">
                    <span class="summary-label">Correct Answers</span>
                    <span class="summary-value" id="correctAnswers">0</span>
                </div>
                <div class="summary-item incorrect">
                    <span class="summary-label">Incorrect Answers</span>
                    <span class="summary-value" id="incorrectAnswers">0</span>
                </div>
                <div class="summary-item score">
                    <span class="summary-label">Score Percentage</span>
                    <span class="summary-value" id="scorePercentage">0%</span>
                </div>
            </div>
            
            <div class="charts-container">
                <div class="chart-wrapper">
                    <h3>Time Spent Per Question</h3>
                    <canvas id="timeChart"></canvas>
                </div>
                
                <div class="chart-wrapper">
                    <h3>Correct vs Incorrect</h3>
                    <canvas id="pieChart"></canvas>
                </div>
            </div>
            
            <div class="result-actions">
                <button class="btn-primary" onclick="window.location.href='index.php'">Take Another Quiz</button>
                <button class="btn-secondary" onclick="window.location.href='quiz.php'">Review Quiz</button>
            </div>
        </div>
    </div>
    
    <script src="result.js"></script>
</body>
</html>

