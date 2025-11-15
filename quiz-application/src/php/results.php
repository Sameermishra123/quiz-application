<?php
session_start();

if (!isset($_SESSION['quiz_results'])) {
    header("Location: ../html/index.html");
    exit();
}

$results = $_SESSION['quiz_results'];
$totalQuestions = count($results);
$correctAnswers = array_filter($results, function($result) {
    return $result['is_correct'];
});
$score = count($correctAnswers);
$percentage = ($score / $totalQuestions) * 100;

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/results.css">
    <title>Quiz Results</title>
</head>
<body>
    <div class="results-container">
        <h1>Your Quiz Results</h1>
        <p>Total Questions: <?php echo $totalQuestions; ?></p>
        <p>Correct Answers: <?php echo $score; ?></p>
        <p>Score: <?php echo $percentage; ?>%</p>

        <canvas id="resultsChart"></canvas>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <script src="../js/charts.js"></script>
    <script>
        const results = <?php echo json_encode($results); ?>;
        const correctAnswers = results.filter(result => result.is_correct).length;
        const incorrectAnswers = results.length - correctAnswers;

        const ctx = document.getElementById('resultsChart').getContext('2d');
        const resultsChart = new Chart(ctx, {
            type: 'pie',
            data: {
                labels: ['Correct Answers', 'Incorrect Answers'],
                datasets: [{
                    data: [correctAnswers, incorrectAnswers],
                    backgroundColor: ['#4CAF50', '#F44336']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: true,
                        text: 'Quiz Results Distribution'
                    }
                }
            }
        });
    </script>
</body>
</html>