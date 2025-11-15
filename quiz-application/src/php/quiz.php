<?php
session_start();

$questions = [
    [
        'question' => 'What is the capital of France?',
        'options' => ['Berlin', 'Madrid', 'Paris', 'Rome'],
        'answer' => 'Paris'
    ],
    [
        'question' => 'Which planet is known as the Red Planet?',
        'options' => ['Earth', 'Mars', 'Jupiter', 'Saturn'],
        'answer' => 'Mars'
    ],
    [
        'question' => 'What is the largest ocean on Earth?',
        'options' => ['Atlantic Ocean', 'Indian Ocean', 'Arctic Ocean', 'Pacific Ocean'],
        'answer' => 'Pacific Ocean'
    ],
    // Add more questions as needed
];

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $_SESSION['quiz_answers'] = $_POST['answers'];
    header('Location: results.php');
    exit();
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../css/quiz.css">
    <title>Quiz Application</title>
</head>
<body>
    <div class="quiz-container">
        <h1>Quiz</h1>
        <form method="POST" id="quiz-form">
            <?php foreach ($questions as $index => $question): ?>
                <div class="question">
                    <p><?php echo ($index + 1) . '. ' . $question['question']; ?></p>
                    <?php foreach ($question['options'] as $option): ?>
                        <label>
                            <input type="radio" name="answers[<?php echo $index; ?>]" value="<?php echo $option; ?>" required>
                            <?php echo $option; ?>
                        </label>
                    <?php endforeach; ?>
                </div>
            <?php endforeach; ?>
            <button type="submit">Submit Quiz</button>
        </form>
    </div>
    <script src="../js/timer.js"></script>
    <script src="../js/quiz.js"></script>
</body>
</html>