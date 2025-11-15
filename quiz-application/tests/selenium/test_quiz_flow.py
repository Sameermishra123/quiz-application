from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

def test_quiz_flow(driver):
    """Test complete quiz flow from landing page to results"""
    
    print("\n" + "="*70)
    print("TEST: Complete Quiz Flow")
    print("="*70)
    
    # Step 1: Verify landing page elements
    print("\n1. Verifying landing page...")
    category_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "category"))
    )
    assert category_dropdown.is_displayed()
    print("   ✓ Category dropdown found")
    
    difficulty_dropdown = driver.find_element(By.ID, "difficulty")
    assert difficulty_dropdown.is_displayed()
    print("   ✓ Difficulty dropdown found")
    
    # Step 2: Select category and difficulty
    print("\n2. Selecting quiz options...")
    category_select = Select(category_dropdown)
    category_select.select_by_value("dsa")
    print("   ✓ Selected Category: DSA")
    time.sleep(1)
    
    difficulty_select = Select(difficulty_dropdown)
    difficulty_select.select_by_value("easy")
    print("   ✓ Selected Difficulty: Easy")
    time.sleep(1)
    
    # Step 3: Click Start Quiz
    print("\n3. Starting quiz...")
    start_btn = driver.find_element(By.ID, "startBtn")
    start_btn.click()
    print("   ✓ Clicked Start Quiz button")
    time.sleep(3)
    
    # Step 4: Wait for quiz.php to load
    print("\n4. Waiting for quiz page...")
    WebDriverWait(driver, 10).until(
        lambda d: "quiz.php" in d.current_url
    )
    print(f"   ✓ Quiz page loaded: {driver.current_url}")
    
    # Step 5: Verify quiz page elements
    print("\n5. Verifying quiz page elements...")
    question_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "questionText"))
    )
    assert question_text.text != "Loading question..."
    print(f"   ✓ Question loaded: {question_text.text[:60]}...")
    
    options_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "optionsContainer"))
    )
    assert options_container.is_displayed()
    print("   ✓ Options container found")
    
    timer = driver.find_element(By.ID, "timer")
    assert timer.is_displayed()
    print(f"   ✓ Timer found: {timer.text}s")
    
    # Step 6: Go through all questions
    print("\n6. Answering all questions...")
    question_num = 1
    max_questions = 10  # Safety limit
    
    while question_num <= max_questions:
        # Answer current question
        try:
            option = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "#optionsContainer input[type='radio']"))
            )
            option.click()
            print(f"   ✓ Selected answer for question {question_num}")
            time.sleep(1)
        except:
            print(f"   ! Could not select answer for question {question_num}")
        
        # Check if Submit button is visible (last question)
        try:
            submit_btn = driver.find_element(By.ID, "submitBtn")
            if submit_btn.is_displayed():
                print(f"   ✓ Reached last question ({question_num} total)")
                submit_btn.click()
                print("   ✓ Clicked Submit button")
                break
        except NoSuchElementException:
            pass  # Submit button doesn't exist yet
        
        # Not last question, click Next
        try:
            next_btn = driver.find_element(By.ID, "nextBtn")
            if next_btn.is_displayed() and next_btn.is_enabled():
                next_btn.click()
                print(f"   ✓ Clicked Next")
                time.sleep(2)
                question_num += 1
            else:
                print("   ! Next button not clickable")
                break
        except NoSuchElementException:
            print("   ! No Next button found - should be on last question")
            # Try to submit
            try:
                submit_btn = driver.find_element(By.ID, "submitBtn")
                submit_btn.click()
                print("   ✓ Clicked Submit button")
                break
            except:
                print("   ! No Submit button either, waiting for auto-submit...")
                time.sleep(20)
                break
    
    # Step 7: Wait for results page
    print("\n7. Waiting for results page...")
    time.sleep(2)
    print(f"   Current URL: {driver.current_url}")
    
    try:
        WebDriverWait(driver, 25).until(
            lambda d: "result.php" in d.current_url
        )
        print(f"   ✓ Result page loaded: {driver.current_url}")
    except TimeoutException:
        print(f"   ✗ TIMEOUT: Still on {driver.current_url}")
        # Check page source for debugging
        print("   → Page title:", driver.title)
        driver.save_screenshot("test_failure_quiz_flow.png")
        print("   → Screenshot saved as test_failure_quiz_flow.png")
        raise
    
    # Step 8: Verify results page
    print("\n8. Verifying results...")
    
    result_heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Results" in result_heading.text or "Quiz Results" in result_heading.text
    print(f"   ✓ Results heading: {result_heading.text}")
    
    # Verify result elements exist
    score = driver.find_element(By.ID, "scorePercentage")
    print(f"   ✓ Score: {score.text}")
    
    correct = driver.find_element(By.ID, "correctAnswers")
    print(f"   ✓ Correct answers: {correct.text}")
    
    incorrect = driver.find_element(By.ID, "incorrectAnswers")
    print(f"   ✓ Incorrect answers: {incorrect.text}")
    
    total = driver.find_element(By.ID, "totalQuestions")
    print(f"   ✓ Total questions: {total.text}")
    
    # Verify charts exist
    time_chart = driver.find_element(By.ID, "timeChart")
    assert time_chart.is_displayed()
    print("   ✓ Time chart displayed")
    
    pie_chart = driver.find_element(By.ID, "pieChart")
    assert pie_chart.is_displayed()
    print("   ✓ Pie chart displayed")
    
    print("\n" + "="*70)
    print("✅ TEST PASSED: Complete quiz flow working!")
    print("="*70)