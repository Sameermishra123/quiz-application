<?php
// Configuration settings for the PHP application

// Database connection settings (if applicable)
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASS', '');
define('DB_NAME', 'quiz_application');

// Other environment settings
define('APP_ENV', 'development');
define('APP_DEBUG', true);
define('APP_URL', 'http://localhost/quiz-application');

// Set the timezone
date_default_timezone_set('America/New_York');
?>