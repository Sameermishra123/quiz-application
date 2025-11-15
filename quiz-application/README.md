# Quiz Application

This is a dynamic quiz application built using PHP, HTML, CSS, and JavaScript. The application features a timer for each quiz question and provides result analysis using Chart.js.

## Features

- Dynamic quiz loading based on user-selected categories and difficulty levels.
- Timer functionality for each question to enhance the quiz experience.
- Result analysis with visualizations using Chart.js.
- User-friendly interface for easy navigation.

## Project Structure

```
quiz-application
├── src
│   ├── php
│   │   ├── config.php
│   │   ├── database.php
│   │   ├── quiz.php
│   │   ├── results.php
│   │   └── api
│   │       ├── get_quiz.php
│   │       ├── submit_quiz.php
│   │       └── get_results.php
│   ├── html
│   │   ├── index.html
│   │   ├── quiz.html
│   │   └── results.html
│   ├── css
│   │   ├── style.css
│   │   ├── quiz.css
│   │   └── results.css
│   ├── js
│   │   ├── main.js
│   │   ├── timer.js
│   │   ├── quiz.js
│   │   └── charts.js
├── tests
│   ├── selenium
│   │   ├── test_quiz_flow.py
│   │   ├── test_timer.py
│   │   ├── test_results.py
│   │   └── conftest.py
│   └── requirements.txt
├── public
│   └── index.php
├── package.json
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd quiz-application
   ```
3. Set up a local server (e.g., using XAMPP or MAMP) to run the PHP files.
4. Open `public/index.php` in your web browser to access the application.

## Usage

- On the landing page, select the quiz category and difficulty level.
- Start the quiz and answer the questions within the given time.
- After completing the quiz, view your results and analysis on the results page.

## Testing

To run the Selenium tests, ensure you have the required dependencies installed. You can find the dependencies listed in `tests/requirements.txt`.

Run the tests using:
```
pytest tests/selenium
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.