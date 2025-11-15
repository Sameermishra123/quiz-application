from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def test_timer_functionality(driver):
    """Test that the timer counts down properly"""
    
    print("\n" + "="*60)
    print("TEST: Timer Functionality")
    print("="*60)
    
    # Step 1: Start quiz
    print("\n1. Starting quiz...")
    category_select = Select(WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "category"))
    ))
    category_select.select_by_value("dbms")
    print("   ✓ Selected category: DBMS")
    
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
    
    # Step 4: Find and verify timer element
    print("\n3. Testing timer...")
    timer_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "timer"))
    )
    assert timer_span.is_displayed()
    print("   ✓ Timer element found and visible")
    
    # Step 5: Check timer is counting down
    first_value = timer_span.text
    print(f"   ✓ Initial timer value: {first_value}s")
    
    # Wait 3 seconds
    print("   ⏱ Waiting 3 seconds...")
    time.sleep(3)
    
    second_value = timer_span.text
    print(f"   ✓ Timer value after 3s: {second_value}s")
    
    # Step 6: Verify timer decreased
    try:
        first_int = int(first_value)
        second_int = int(second_value)
        
        assert second_int < first_int, f"Timer did not decrease! Before: {first_int}, After: {second_int}"
        difference = first_int - second_int
        
        print(f"   ✓ Timer decreased by {difference} seconds")
        assert difference >= 2 and difference <= 4, f"Timer change unexpected: {difference}s (expected ~3s)"
        print("   ✓ Timer countdown rate is correct")
        
    except ValueError:
        # If values aren't integers, just check they're different
        assert first_value != second_value, f"Timer did not change! Value: {first_value}"
        print("   ✓ Timer value changed")
    
    print("\n" + "="*60)
    print("✅ TEST PASSED: Timer is functioning correctly!")
    print("="*60)