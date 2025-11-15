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
    ],
    'general' => [
        [
            'question' => 'What is the capital of France?',
            'options' => ['London', 'Berlin', 'Paris', 'Madrid'],
            'answer' => 'Paris'
        ],
        [
            'question' => 'What is the largest ocean?',
            'options' => ['Atlantic', 'Indian', 'Arctic', 'Pacific'],
            'answer' => 'Pacific'
        ]
    ],
    'history' => [
        [
            'question' => 'In which year did World War II end?',
            'options' => ['1943', '1944', '1945', '1946'],
            'answer' => '1945'
        ],
        [
            'question' => 'Who was the first President of the United States?',
            'options' => ['Thomas Jefferson', 'John Adams', 'George Washington', 'Benjamin Franklin'],
            'answer' => 'George Washington'
        ]
    ]
];

$category = isset($_GET['category']) ? $_GET['category'] : 'science';

if (array_key_exists($category, $quizzes)) {
    echo json_encode($quizzes[$category]);
} else {
    // Default to science if category not found
    echo json_encode($quizzes['science']);
}
?>