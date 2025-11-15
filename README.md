# Dynamic Quiz Application with Timer + Result Analysis

A fully functional quiz application built with PHP, HTML, CSS, JavaScript, and Chart.js. Features dynamic question loading, per-question timers, and comprehensive result analysis with visualizations.

## 🚀 Features

- **Category Selection**: Choose from OS, DSA, Networks, or DBMS
- **Difficulty Levels**: Easy, Medium, Hard
- **Dynamic Question Loading**: Questions loaded based on user selection
- **Per-Question Timer**: 10-20 seconds per question (based on difficulty)
- **Answer Tracking**: Tracks user answers and time spent per question
- **Result Analysis**: 
  - Score percentage
  - Correct/Incorrect count
  - Bar chart showing time spent per question
  - Pie chart showing correct vs incorrect answers
- **Responsive Design**: Works on Desktop, Tablet, and Mobile
- **localStorage**: All data persisted in browser localStorage

## 📁 Project Structure

```
/QUIZ_ASSIGNMENT
│── index.php              // Category + difficulty selection
│── quiz.php               // Quiz interface
│── result.php             // Final result analysis
│── styles.css             // Responsive styling
│── questions.js           // All category-wise questions
│── quiz.js                // Timer + quiz logic
│── result.js              // Result page logic + Chart.js
│── test_quiz.py           // Selenium WebDriver test script
│── requirements.txt       // Python dependencies
└── README.md              // This file
```

## 🛠️ Setup Instructions

### 1. Web Server Setup

Since this uses PHP, you need a web server:

**Option A: Using XAMPP/WAMP/MAMP**
1. Install XAMPP, WAMP, or MAMP
2. Copy the project folder to `htdocs` (XAMPP) or `www` (WAMP/MAMP)
3. Start Apache server
4. Access via `http://localhost/QUIZ_ASSIGNMENT/`

**Option B: Using PHP Built-in Server**
```bash
cd QUIZ_ASSIGNMENT
php -S localhost:8000
```
Then access via `http://localhost:8000/`

### 2. Python Selenium Testing Setup

1. Install Python (3.7+)
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. **Fix ChromeDriver Version Conflicts (IMPORTANT)**:
   
   If you get a ChromeDriver version mismatch error:
   
   **Quick Fix - Run the helper script:**
   ```bash
   python fix_chromedriver.py
   ```
   This will help you identify and fix ChromeDriver conflicts.
   
   **Manual Fix:**
   - The error usually means you have an old `chromedriver.exe` in your PATH (often in `C:\Windows\`)
   - **Option 1 (Recommended)**: Rename the old chromedriver:
     ```bash
     # Run as Administrator in PowerShell
     Rename-Item C:\Windows\chromedriver.exe C:\Windows\chromedriver.exe.old
     ```
   - **Option 2**: Delete the old chromedriver (if you're sure you don't need it)
   - **Option 3**: Remove the directory containing chromedriver from your system PATH
   
   The `webdriver-manager` package will automatically download the correct ChromeDriver version once the old one is removed from PATH.

4. **Start the Web Server** (REQUIRED before running tests):
   
   **Option A: Use the helper script (Easiest)**
   ```bash
   python start_server.py
   ```
   This will start PHP built-in server on `localhost:8000`
   
   **Option B: Manual PHP server**
   ```bash
   php -S localhost:8000
   ```
   
   **Option C: XAMPP/WAMP/MAMP**
   - Start Apache server
   - Place project in `htdocs` or `www` folder
   
5. Update `BASE_URL` in `test_quiz.py` if needed:
```python
BASE_URL = "http://localhost:8000/"  # For PHP built-in server
# OR
BASE_URL = "http://localhost/QUIZ_ASSIGNMENT/"  # For XAMPP/WAMP
```

6. Run tests (in a new terminal while server is running):
```bash
python test_quiz.py
```

**Note**: The test script will automatically check if the server is running and provide helpful error messages if it's not.

## 📝 Usage

1. **Start Quiz**:
   - Open `index.php` in browser
   - Select a category (OS, DSA, Networks, DBMS)
   - Select difficulty (Easy, Medium, Hard)
   - Click "Start Quiz"

2. **Take Quiz**:
   - Answer questions one at a time
   - Timer counts down for each question
   - Use Previous/Next buttons to navigate
   - Timer auto-advances when it reaches 0

3. **View Results**:
   - After submitting, view your score
   - See time spent per question (Bar Chart)
   - See correct vs incorrect breakdown (Pie Chart)

## 🎨 Question Format

Questions are stored in `questions.js`:

```javascript
const quizData = {
  category: {
    difficulty: [
      {
        question: "Question text?",
        options: ["Option 1", "Option 2", "Option 3", "Option 4"],
        answer: 0  // Index of correct answer (0-based)
      }
    ]
  }
};
```

## 🧪 Testing

The Selenium test script (`test_quiz.py`) automates:
1. Landing page verification
2. Category and difficulty selection
3. Starting the quiz
4. Answering questions
5. Submitting the quiz
6. Validating result page

### Troubleshooting Test Issues

**ChromeDriver Version Mismatch:**
- Error: "This version of ChromeDriver only supports Chrome version X"
- Solution: Run `python fix_chromedriver.py` to identify and fix the issue
- Or manually remove/rename the old chromedriver.exe from `C:\Windows\`

**WebDriver Not Found:**
- Ensure Chrome browser is installed
- Update webdriver-manager: `pip install --upgrade webdriver-manager`
- Clear cache: Delete `%USERPROFILE%\.wdm\drivers\chromedriver`

## 📊 Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Backend**: PHP (for page routing)
- **Charts**: Chart.js (CDN)
- **Storage**: localStorage
- **Testing**: Selenium WebDriver (Python)

## 🎯 Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari

## 📱 Responsive Breakpoints

- **Desktop**: > 768px
- **Tablet**: 480px - 768px
- **Mobile**: < 480px

## 🔧 Customization

- **Timer Duration**: Edit `timerDuration` in `quiz.js` (lines 7-13)
- **Questions**: Add/edit questions in `questions.js`
- **Styling**: Modify `styles.css`
- **Chart Colors**: Edit chart configurations in `result.js`

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests.

---

**Note**: Make sure your web server is running before testing the application!

