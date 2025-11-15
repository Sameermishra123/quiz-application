<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Quiz Application - Select Category & Difficulty</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <div class="selection-card">
            <h1>Welcome to Quiz Application</h1>
            <p class="subtitle">Select your category and difficulty level to begin</p>
            
            <form id="quizForm">
                <div class="form-group">
                    <label for="category">Select Category:</label>
                    <select id="category" name="category" required>
                        <option value="">-- Choose Category --</option>
                        <option value="os">Operating Systems (OS)</option>
                        <option value="dsa">Data Structures & Algorithms (DSA)</option>
                        <option value="networks">Computer Networks</option>
                        <option value="dbms">DBMS</option>
                    </select>
                </div>
                
                <div class="form-group">
                    <label for="difficulty">Select Difficulty:</label>
                    <select id="difficulty" name="difficulty" required>
                        <option value="">-- Choose Difficulty --</option>
                        <option value="easy">Easy</option>
                        <option value="medium">Medium</option>
                        <option value="hard">Hard</option>
                    </select>
                </div>
                
                <button type="submit" class="btn-primary" id="startBtn">Start Quiz</button>
            </form>
        </div>
    </div>
    
    <script>
        document.getElementById('quizForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const category = document.getElementById('category').value;
            const difficulty = document.getElementById('difficulty').value;
            
            if (category && difficulty) {
                // Save selections to localStorage
                localStorage.setItem('selectedCategory', category);
                localStorage.setItem('selectedDifficulty', difficulty);
                
                // Redirect to quiz page
                window.location.href = 'quiz.php';
            } else {
                alert('Please select both category and difficulty!');
            }
        });
    </script>
</body>
</html>

