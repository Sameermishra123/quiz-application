from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_timer_functionality(driver):

    # Start Quiz
    start_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    start_btn.click()

    # Locate timer span
    timer_value = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "time"))
    )

    first = timer_value.text
    time.sleep(2)
    second = timer_value.text

    assert first != second, "❌ Timer did NOT decrease!"
