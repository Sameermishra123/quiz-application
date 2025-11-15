from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_results_display(driver):
    """Test that results page displays all required elements"""
    
    print("\n" + "="*60)
    print("TEST: Results Display")
    print("="*60)
    
    # Step 1: Start quiz from landing page
    print("\n1. Starting quiz from landing page...")
    category_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "category"))
    ))
    category_select.select_by_value("os")
    print("   ✓ Selected category: OS")
    
    difficulty_select = Select(driver.find_element(By.ID, "difficulty"))
    difficulty_select.select_by_value("easy")
    print("   ✓ Selected difficulty: Easy")
    time.sleep(1)
    
    start_btn = driver.find_element(By.ID, "startBtn")
    start_btn.click()
    print("   ✓ Clicked Start Quiz")
    time.sleep(3)
    
    # Step 2: Wait for quiz page
    print("\n2. Waiting for quiz page...")
    WebDriverWait(driver, 10).until(
        lambda d: "quiz.php" in d.current_url
    )
    print("   ✓ Quiz page loaded")
    
    # Step 3: Wait for options container (CORRECT ID)
    options_container = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "optionsContainer"))
    )
    print("   ✓ Options container found")
    
    # Step 4: Answer one question
    print("\n3. Answering question...")
    first_opt = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#optionsContainer input[type='radio']"))
    )
    first_opt.click()
    print("   ✓ Selected answer")
    time.sleep(2)
    
    # Step 5: Try to submit or wait for timer
    print("\n4. Submitting quiz...")
    try:
        submit_btn = driver.find_element(By.ID, "submitBtn")
        if submit_btn.is_displayed():
            submit_btn.click()
            print("   ✓ Clicked Submit")
        else:
            # Click Next until we find Submit
            for _ in range(10):
                try:
                    next_btn = driver.find_element(By.ID, "nextBtn")
                    if next_btn.is_displayed():
                        next_btn.click()
                        time.sleep(1)
                        # Try to answer
                        try:
                            opt = driver.find_element(By.CSS_SELECTOR, "#optionsContainer input[type='radio']")
                            opt.click()
                            time.sleep(1)
                        except:
                            pass
                    else:
                        break
                except:
                    break
            
            # Now try submit again
            submit_btn = driver.find_element(By.ID, "submitBtn")
            submit_btn.click()
            print("   ✓ Clicked Submit after navigating")
    except:
        print("   ! Waiting for auto-submit...")
        time.sleep(15)
    
    # Step 6: Wait for results page
    print("\n5. Waiting for results page...")
    WebDriverWait(driver, 20).until(
        lambda d: "result.php" in d.current_url
    )
    print("   ✓ Results page loaded")
    
    # Step 7: Verify all result elements
    print("\n6. Verifying result elements...")
    
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Results" in header.text or "Quiz Results" in header.text
    print(f"   ✓ Header: {header.text}")
    
    # Score elements
    score = driver.find_element(By.ID, "scorePercentage")
    assert score.is_displayed()
    print(f"   ✓ Score displayed: {score.text}")
    
    correct = driver.find_element(By.ID, "correctAnswers")
    assert correct.is_displayed()
    print(f"   ✓ Correct answers: {correct.text}")
    
    incorrect = driver.find_element(By.ID, "incorrectAnswers")
    assert incorrect.is_displayed()
    print(f"   ✓ Incorrect answers: {incorrect.text}")
    
    total = driver.find_element(By.ID, "totalQuestions")
    assert total.is_displayed()
    print(f"   ✓ Total questions: {total.text}")
    
    # Charts
    time_chart = driver.find_element(By.ID, "timeChart")
    assert time_chart is not None
    print("   ✓ Time chart canvas exists")
    
    pie_chart = driver.find_element(By.ID, "pieChart")
    assert pie_chart is not None
    print("   ✓ Pie chart canvas exists")
    
    print("\n" + "="*60)
    print("✅ TEST PASSED: All result elements displayed correctly!")
    print("="*60)