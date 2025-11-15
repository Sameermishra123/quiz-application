<?php
header('Content-Type: application/json');

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $answers = isset($_POST['answers']) ? $_POST['answers'] : [];
    $correctAnswers = 0;
    $totalQuestions = count($answers);

    // Assuming you have a way to get the correct answers
    $correctAnswersList = $_SESSION['correct_answers']; // This should be set when the quiz is loaded

    foreach ($answers as $questionId => $userAnswer) {
        if (isset($correctAnswersList[$questionId]) && $correctAnswersList[$questionId] === $userAnswer) {
            $correctAnswers++;
        }
    }

    $score = ($totalQuestions > 0) ? ($correctAnswers / $totalQuestions) * 100 : 0;

    // Store results in session or database as needed
    $_SESSION['quiz_results'] = [
        'score' => $score,
        'correct_answers' => $correctAnswers,
        'total_questions' => $totalQuestions,
    ];

    echo json_encode([
        'status' => 'success',
        'score' => $score,
        'correct_answers' => $correctAnswers,
        'total_questions' => $totalQuestions,
    ]);
} else {
    echo json_encode([
        'status' => 'error',
        'message' => 'Invalid request method.',
    ]);
}
?>