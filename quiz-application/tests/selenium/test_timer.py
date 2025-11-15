from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_timer_functionality(driver):

    # Start quiz
    start_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    start_btn.click()

    # Wait for quiz page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "questions-container"))
    )
    
    # Timer span
    timer_span = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "time"))
    )

    first = timer_span.text
    time.sleep(2)
    second = timer_span.text

    # Timer must decrease
    assert first != second, "❌ Timer did NOT decrease!"
