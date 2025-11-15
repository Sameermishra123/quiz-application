from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_results_display(driver):

    # Start Quiz
    start_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    start_btn.click()

    # Wait for quiz page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "questions-container"))
    )
    
    # Select first answer
    first_opt = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#questions-container input[type='radio']"))
    )
    first_opt.click()

    # Submit quiz
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()

    # Page must show header
    header = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Results" in header.text or "Your Quiz Results" in header.text

    # Chart canvas must exist
    chart = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "resultsChart"))
    )
    assert chart is not None
