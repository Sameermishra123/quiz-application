<?php
header('Content-Type: application/json');

$quizzes = [
    'science' => [
        [
            'question' => 'What is the chemical symbol for water?',
            'options' => ['H2O', 'O2', 'CO2', 'NaCl'],
            'answer' => 'H2O'
        ],
        [
            'question' => 'What planet is known as the Red Planet?',
            'options' => ['Earth', 'Mars', 'Jupiter', 'Saturn'],
            'answer' => 'Mars'
        ]
    ],
    'math' => [
        [
            'question' => 'What is 2 + 2?',
            'options' => ['3', '4', '5', '6'],
            'answer' => '4'
        ],
        [
            'question' => 'What is the square root of 16?',
            'options' => ['2', '3', '4', '5'],
            'answer' => '4'
        ]
    ]
];

$category = isset($_GET['category']) ? $_GET['category'] : null;

if ($category && array_key_exists($category, $quizzes)) {
    echo json_encode($quizzes[$category]);
} else {
    echo json_encode(['error' => 'Invalid category']);
}
?>