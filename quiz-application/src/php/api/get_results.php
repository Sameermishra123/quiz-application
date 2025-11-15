<?php
header('Content-Type: application/json');

session_start();

if (!isset($_SESSION['quiz_results'])) {
    echo json_encode(['error' => 'No results found.']);
    exit();
}

$results = $_SESSION['quiz_results'];
$score = $results['score'];
$totalQuestions = $results['total_questions'];
$correctAnswers = $results['correct_answers'];

$response = [
    'score' => $score,
    'total_questions' => $totalQuestions,
    'correct_answers' => $correctAnswers,
    'percentage' => ($score / $totalQuestions) * 100,
];

echo json_encode($response);
?>