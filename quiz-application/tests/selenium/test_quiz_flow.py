from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_quiz_flow(driver):

    # Click Start Quiz
    start_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    start_btn.click()

    # Wait for quiz title on next page
    quiz_heading = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Quiz" in quiz_heading.text

    # Wait for questions container to be present and then for questions to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "questions-container"))
    )
    
    # Wait for dynamically loaded questions (radio buttons)
    first_option = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#questions-container input[type='radio']"))
    )
    first_option.click()

    # Submit quiz
    submit_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_btn.click()

    # Results page loaded
    result_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )
    assert "Results" in result_title.text or "Your Quiz Results" in result_title.text
