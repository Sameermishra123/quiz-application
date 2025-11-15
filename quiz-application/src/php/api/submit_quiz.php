<?php
header('Content-Type: application/json');

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $json = file_get_contents('php://input');
    $data = json_decode($json, true);
    
    $answers = isset($data['answers']) ? $data['answers'] : [];
    $questions = isset($data['questions']) ? $data['questions'] : [];
    
    $correctAnswers = 0;
    $totalQuestions = count($questions);

    // Calculate correct answers by comparing user answers with question answers
    foreach ($answers as $questionId => $userAnswer) {
        if (isset($questions[$questionId]) && isset($questions[$questionId]['answer'])) {
            if ($questions[$questionId]['answer'] === $userAnswer) {
                $correctAnswers++;
            }
        }
    }

    $score = ($totalQuestions > 0) ? ($correctAnswers / $totalQuestions) * 100 : 0;

    // Store results in session
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