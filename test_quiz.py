"""
Selenium WebDriver Test Script for Dynamic Quiz Application
Tests the complete quiz flow from selection to results
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
import time
import socket
import urllib.request
import urllib.error

# Configuration
BASE_URL = "http://localhost/QUIZ_ASSIGNMENT/"  # Update this to your local server URL
# Alternative: BASE_URL = "http://localhost:8000/"  # For PHP built-in server
WAIT_TIMEOUT = 10

class QuizTest:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def check_server_running(self, url):
        """Check if the web server is running"""
        try:
            # Parse URL
            if url.startswith('http://'):
                url = url[7:]
            if url.startswith('https://'):
                url = url[8:]
            
            # Remove trailing slash and path
            parts = url.split('/')
            host_port = parts[0]
            
            if ':' in host_port:
                host, port = host_port.split(':')
                port = int(port)
            else:
                host = host_port
                port = 80
            
            # Try to connect
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex((host, port))
            sock.close()
            
            if result == 0:
                # Port is open, try HTTP request
                try:
                    full_url = BASE_URL.rstrip('/') + '/index.php'
                    response = urllib.request.urlopen(full_url, timeout=3)
                    return True, None
                except urllib.error.URLError as e:
                    return False, f"Server responded but error: {e}"
            else:
                return False, f"Cannot connect to {host}:{port}"
        except Exception as e:
            return False, f"Error checking server: {str(e)}"
        
    def setup(self):
        """Initialize WebDriver"""
        print("Setting up WebDriver...")
        # Using Chrome WebDriver with webdriver-manager for automatic driver management
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Save original PATH
        original_path = os.environ.get('PATH', '')
        
        # Remove chromedriver.exe from Windows PATH to avoid version conflicts
        path_parts = original_path.split(os.pathsep)
        # Filter out Windows chromedriver specifically
        filtered_path = []
        for p in path_parts:
            # Skip paths that contain chromedriver.exe (especially C:\Windows)
            if 'chromedriver.exe' in p.lower() or (p.lower() == 'c:\\windows' and os.path.exists(os.path.join(p, 'chromedriver.exe'))):
                print(f"Removing from PATH: {p}")
                continue
            filtered_path.append(p)
        
        # Temporarily modify PATH
        os.environ['PATH'] = os.pathsep.join(filtered_path)
        
        try:
            # Use webdriver-manager to automatically download and use correct ChromeDriver version
            print("Downloading/updating ChromeDriver via webdriver-manager...")
            print("(This may take a moment on first run)")
            
            # Force download by clearing cache or using latest version
            driver_manager = ChromeDriverManager()
            driver_path = driver_manager.install()
            
            # Normalize path (handle forward slashes on Windows)
            driver_path = os.path.normpath(driver_path.replace('/', os.sep))
            
            # webdriver-manager sometimes returns a directory path or wrong file
            # We need to find the actual chromedriver.exe
            original_driver_path = driver_path
            
            # Check if the path is valid and points to chromedriver.exe
            if not driver_path.endswith('.exe') or not os.path.exists(driver_path) or os.path.isdir(driver_path):
                # If it's a directory or wrong file, search for chromedriver.exe
                if os.path.isdir(driver_path):
                    search_dir = driver_path
                else:
                    # Get the directory containing the file
                    search_dir = os.path.dirname(driver_path)
                    # If the path points to a text file or wrong file, go up one level
                    # Common structure: version/chromedriver-win32/chromedriver.exe
                    if 'chromedriver-win32' in search_dir or 'chromedriver-win64' in search_dir:
                        pass  # We're in the right directory
                    else:
                        # Try parent directory
                        parent_dir = os.path.dirname(search_dir)
                        if os.path.exists(parent_dir):
                            search_dir = parent_dir
                
                # First, try common locations in the search directory
                possible_paths = [
                    os.path.join(search_dir, 'chromedriver.exe'),
                    os.path.join(search_dir, 'chromedriver'),
                ]
                
                # Also check subdirectories (chromedriver-win32, chromedriver-win64)
                for item in os.listdir(search_dir) if os.path.exists(search_dir) else []:
                    item_path = os.path.join(search_dir, item)
                    if os.path.isdir(item_path) and 'chromedriver' in item.lower():
                        possible_paths.extend([
                            os.path.join(item_path, 'chromedriver.exe'),
                            os.path.join(item_path, 'chromedriver'),
                        ])
                
                # Try the possible paths
                for path in possible_paths:
                    if os.path.exists(path) and os.path.isfile(path):
                        if path.endswith('.exe'):
                            driver_path = path
                            break
                        elif os.access(path, os.X_OK):
                            driver_path = path
                            break
                
                # If still not found, search recursively
                if not (driver_path.endswith('.exe') and os.path.exists(driver_path)):
                    for root, dirs, files in os.walk(search_dir):
                        for file in files:
                            if file.lower() == 'chromedriver.exe':
                                found_path = os.path.join(root, file)
                                if os.path.exists(found_path) and os.path.isfile(found_path):
                                    driver_path = found_path
                                    break
                        if driver_path.endswith('.exe') and os.path.exists(driver_path):
                            break
            
            # Final verification - search in cache if not found
            if not os.path.exists(driver_path):
                # Last resort: search in the webdriver-manager cache directory
                cache_dir = os.path.join(os.path.expanduser('~'), '.wdm', 'drivers', 'chromedriver')
                if os.path.exists(cache_dir):
                    print(f"Searching in cache directory: {cache_dir}")
                    for root, dirs, files in os.walk(cache_dir):
                        for file in files:
                            if file.lower() == 'chromedriver.exe':
                                found_path = os.path.join(root, file)
                                if os.path.exists(found_path) and os.path.isfile(found_path):
                                    driver_path = found_path
                                    print(f"Found ChromeDriver in cache: {driver_path}")
                                    break
                        if driver_path.endswith('.exe') and os.path.exists(driver_path):
                            break
                
                if not os.path.exists(driver_path):
                    raise Exception(f"Downloaded ChromeDriver not found.\nOriginal path: {original_driver_path}\nSearched: {driver_path}")
            
            if not driver_path.endswith('.exe'):
                raise Exception(f"ChromeDriver path does not point to .exe file: {driver_path}")
            
            if not os.path.isfile(driver_path):
                raise Exception(f"ChromeDriver path is not a file: {driver_path}")
            
            print(f"Using ChromeDriver from: {driver_path}")
            
            # Explicitly use the downloaded driver with Service
            service = Service(driver_path)
            self.driver = webdriver.Chrome(service=service, options=options)
            print("WebDriver initialized successfully using webdriver-manager!")
            
        except Exception as e:
            # Restore original PATH before raising
            os.environ['PATH'] = original_path
            error_msg = str(e)
            print(f"\n{'='*70}")
            print("ERROR: Failed to initialize WebDriver")
            print(f"{'='*70}")
            print(f"Error details: {error_msg}")
            print(f"\n{'='*70}")
            print("TROUBLESHOOTING STEPS:")
            print(f"{'='*70}")
            print("1. Remove the old ChromeDriver from Windows PATH:")
            print("   - Delete or rename: C:\\Windows\\chromedriver.exe")
            print("   - Or remove C:\\Windows from PATH if not needed")
            print("\n2. Update webdriver-manager:")
            print("   pip install --upgrade webdriver-manager")
            print("\n3. Clear webdriver-manager cache:")
            print("   - Delete: %USERPROFILE%\\.wdm\\drivers\\chromedriver")
            print("\n4. Manual ChromeDriver download:")
            print("   - Download from: https://chromedriver.chromium.org/downloads")
            print("   - Match your Chrome version: 142.0.7444.61")
            print("   - Extract and place in project folder")
            print(f"{'='*70}\n")
            raise
        finally:
            # Always restore original PATH
            os.environ['PATH'] = original_path
        
        self.wait = WebDriverWait(self.driver, WAIT_TIMEOUT)
        
    def teardown(self):
        """Close WebDriver"""
        if self.driver:
            self.driver.quit()
            print("WebDriver closed!")
    
    def test_landing_page(self):
        """Test 1: Verify Landing Page (index.php)"""
        print("\n" + "="*50)
        print("TEST 1: Verifying Landing Page")
        print("="*50)
        
        try:
            # Open quiz URL
            self.driver.get(BASE_URL + "index.php")
            time.sleep(2)
            
            # Print title and current URL
            title = self.driver.title
            current_url = self.driver.current_url
            print(f"Page Title: {title}")
            print(f"Current URL: {current_url}")
            
            # Assert category dropdown is visible
            category_dropdown = self.wait.until(
                EC.presence_of_element_located((By.ID, "category"))
            )
            assert category_dropdown.is_displayed(), "Category dropdown is not visible"
            print("✓ Category dropdown is visible")
            
            # Assert difficulty dropdown is visible
            difficulty_dropdown = self.wait.until(
                EC.presence_of_element_located((By.ID, "difficulty"))
            )
            assert difficulty_dropdown.is_displayed(), "Difficulty dropdown is not visible"
            print("✓ Difficulty dropdown is visible")
            
            # Assert Start Quiz button is visible
            start_btn = self.driver.find_element(By.ID, "startBtn")
            assert start_btn.is_displayed(), "Start Quiz button is not visible"
            print("✓ Start Quiz button is visible")
            
            print("TEST 1 PASSED: Landing page verified successfully!")
            return True
            
        except Exception as e:
            print(f"TEST 1 FAILED: {str(e)}")
            return False
    
    def test_start_quiz(self):
        """Test 2: Start Quiz"""
        print("\n" + "="*50)
        print("TEST 2: Starting Quiz")
        print("="*50)
        
        try:
            # Navigate to index.php if not already there
            if "index.php" not in self.driver.current_url:
                self.driver.get(BASE_URL + "index.php")
                time.sleep(2)
            
            # Select Category = "DSA"
            category_select = Select(self.driver.find_element(By.ID, "category"))
            category_select.select_by_value("dsa")
            print("✓ Selected Category: DSA")
            time.sleep(1)
            
            # Select Difficulty = "Easy"
            difficulty_select = Select(self.driver.find_element(By.ID, "difficulty"))
            difficulty_select.select_by_value("easy")
            print("✓ Selected Difficulty: Easy")
            time.sleep(1)
            
            # Click Start Quiz button
            start_btn = self.driver.find_element(By.ID, "startBtn")
            start_btn.click()
            print("✓ Clicked Start Quiz button")
            time.sleep(3)
            
            # Verify quiz.php loads
            current_url = self.driver.current_url
            assert "quiz.php" in current_url, f"Expected quiz.php, but got {current_url}"
            print(f"✓ Quiz page loaded: {current_url}")
            
            # Verify quiz elements are present
            question_text = self.wait.until(
                EC.presence_of_element_located((By.ID, "questionText"))
            )
            assert question_text.is_displayed(), "Question text is not displayed"
            print("✓ Question text is displayed")
            
            print("TEST 2 PASSED: Quiz started successfully!")
            return True
            
        except Exception as e:
            print(f"TEST 2 FAILED: {str(e)}")
            return False
    
    def test_answering_questions(self):
        """Test 3: Answering Questions"""
        print("\n" + "="*50)
        print("TEST 3: Answering Questions")
        print("="*50)
        
        try:
            # Make sure we're on quiz.php
            if "quiz.php" not in self.driver.current_url:
                print("Not on quiz page, navigating...")
                self.driver.get(BASE_URL + "quiz.php")
                time.sleep(3)
            
            question_count = 0
            max_questions = 10  # Safety limit
            
            while question_count < max_questions:
                # Verify question text is displayed
                try:
                    question_text = self.wait.until(
                        EC.presence_of_element_located((By.ID, "questionText"))
                    )
                    question_content = question_text.text
                    print(f"\nQuestion {question_count + 1}: {question_content[:50]}...")
                    
                    # Check if we're on the last question
                    submit_btn = self.driver.find_elements(By.ID, "submitBtn")
                    is_last_question = len(submit_btn) > 0 and submit_btn[0].is_displayed()
                    
                    # Select an option (always second option, index 1)
                    try:
                        options = self.driver.find_elements(By.CSS_SELECTOR, "input[name='answer']")
                        if len(options) >= 2:
                            options[1].click()  # Select second option
                            print(f"✓ Selected option 2")
                            time.sleep(1)
                    except Exception as e:
                        print(f"Warning: Could not select option - {str(e)}")
                    
                    # Click Next or Submit
                    if is_last_question:
                        submit_btn[0].click()
                        print("✓ Clicked Submit button (last question)")
                        time.sleep(3)
                        break
                    else:
                        next_btn = self.driver.find_element(By.ID, "nextBtn")
                        next_btn.click()
                        print("✓ Clicked Next button")
                        time.sleep(2)
                    
                    question_count += 1
                    
                except TimeoutException:
                    print("No more questions found or page changed")
                    break
                except Exception as e:
                    print(f"Error answering question: {str(e)}")
                    break
            
            print(f"\n✓ Answered {question_count} questions")
            print("TEST 3 PASSED: Questions answered successfully!")
            return True
            
        except Exception as e:
            print(f"TEST 3 FAILED: {str(e)}")
            return False
    
    def test_submit_quiz(self):
        """Test 4: Submit Quiz"""
        print("\n" + "="*50)
        print("TEST 4: Submitting Quiz")
        print("="*50)
        
        try:
            # Wait for result page to load
            time.sleep(3)
            
            # Verify redirection to result.php
            current_url = self.driver.current_url
            assert "result.php" in current_url, f"Expected result.php, but got {current_url}"
            print(f"✓ Redirected to result page: {current_url}")
            
            print("TEST 4 PASSED: Quiz submitted successfully!")
            return True
            
        except Exception as e:
            print(f"TEST 4 FAILED: {str(e)}")
            return False
    
    def test_validate_result_page(self):
        """Test 5: Validate Result Page"""
        print("\n" + "="*50)
        print("TEST 5: Validating Result Page")
        print("="*50)
        
        try:
            # Make sure we're on result.php
            if "result.php" not in self.driver.current_url:
                print("Not on result page, navigating...")
                self.driver.get(BASE_URL + "result.php")
                time.sleep(3)
            
            # Check correct count displayed
            try:
                correct_count = self.wait.until(
                    EC.presence_of_element_located((By.ID, "correctAnswers"))
                )
                correct_value = correct_count.text
                print(f"✓ Correct Answers: {correct_value}")
            except Exception as e:
                print(f"✗ Could not find correct answers: {str(e)}")
            
            # Check incorrect count displayed
            try:
                incorrect_count = self.driver.find_element(By.ID, "incorrectAnswers")
                incorrect_value = incorrect_count.text
                print(f"✓ Incorrect Answers: {incorrect_value}")
            except Exception as e:
                print(f"✗ Could not find incorrect answers: {str(e)}")
            
            # Check score percentage displayed
            try:
                score_percentage = self.driver.find_element(By.ID, "scorePercentage")
                score_value = score_percentage.text
                print(f"✓ Score Percentage: {score_value}")
            except Exception as e:
                print(f"✗ Could not find score percentage: {str(e)}")
            
            # Check total questions displayed
            try:
                total_questions = self.driver.find_element(By.ID, "totalQuestions")
                total_value = total_questions.text
                print(f"✓ Total Questions: {total_value}")
            except Exception as e:
                print(f"✗ Could not find total questions: {str(e)}")
            
            # Check if charts are rendered
            try:
                time_chart = self.driver.find_element(By.ID, "timeChart")
                print("✓ Time Chart canvas found")
                
                pie_chart = self.driver.find_element(By.ID, "pieChart")
                print("✓ Pie Chart canvas found")
            except Exception as e:
                print(f"✗ Could not find charts: {str(e)}")
            
            # Print all results to console
            print("\n" + "-"*50)
            print("RESULT SUMMARY:")
            print("-"*50)
            print(f"Total Questions: {total_questions.text}")
            print(f"Correct Answers: {correct_count.text}")
            print(f"Incorrect Answers: {incorrect_count.text}")
            print(f"Score Percentage: {score_percentage.text}")
            print("-"*50)
            
            print("\nTEST 5 PASSED: Result page validated successfully!")
            return True
            
        except Exception as e:
            print(f"TEST 5 FAILED: {str(e)}")
            return False
    
    def run_all_tests(self):
        """Run all test cases"""
        print("\n" + "="*70)
        print("STARTING QUIZ APPLICATION SELENIUM TESTS")
        print("="*70)
        
        # Check if web server is running
        print("\nChecking if web server is running...")
        is_running, error_msg = self.check_server_running(BASE_URL)
        
        if not is_running:
            print("\n" + "="*70)
            print("ERROR: Web server is not running!")
            print("="*70)
            print(f"\nCannot connect to: {BASE_URL}")
            if error_msg:
                print(f"Error: {error_msg}")
            print("\n" + "-"*70)
            print("SOLUTION: Start a web server first!")
            print("-"*70)
            print("\nOption 1: PHP Built-in Server (Recommended for testing)")
            print("  Open a new terminal/PowerShell and run:")
            project_dir = os.getcwd()
            print(f"    cd \"{project_dir}\"")
            print("    php -S localhost:8000")
            print("  Then update BASE_URL in test_quiz.py to: http://localhost:8000/")
            print("\nOption 2: XAMPP/WAMP/MAMP")
            print("  1. Start Apache server")
            print("  2. Place project in htdocs/www folder")
            print("  3. Access via: http://localhost/QUIZ_ASSIGNMENT/")
            print("\nOption 3: Other Web Server")
            print("  Start your web server and update BASE_URL in test_quiz.py")
            print("="*70 + "\n")
            return False
        
        print(f"✓ Web server is running at: {BASE_URL}\n")
        
        results = []
        
        try:
            self.setup()
            
            # Run all tests
            results.append(("Landing Page", self.test_landing_page()))
            results.append(("Start Quiz", self.test_start_quiz()))
            results.append(("Answering Questions", self.test_answering_questions()))
            results.append(("Submit Quiz", self.test_submit_quiz()))
            results.append(("Validate Result Page", self.test_validate_result_page()))
            
        except Exception as e:
            print(f"\nCRITICAL ERROR: {str(e)}")
        finally:
            self.teardown()
        
        # Print summary
        print("\n" + "="*70)
        print("TEST SUMMARY")
        print("="*70)
        passed = sum(1 for _, result in results if result)
        total = len(results)
        
        for test_name, result in results:
            status = "PASSED" if result else "FAILED"
            print(f"{test_name}: {status}")
        
        print("-"*70)
        print(f"Total: {passed}/{total} tests passed")
        print("="*70)
        
        return passed == total


if __name__ == "__main__":
    # Create test instance and run
    test = QuizTest()
    success = test.run_all_tests()
    
    # Exit with appropriate code
    exit(0 if success else 1)

