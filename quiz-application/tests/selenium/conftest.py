from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.fixture(scope="module")
def driver():
    """Launch Chrome WebDriver and open the Quiz start page."""

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_window_size(1920, 1080)

    # ❗ UPDATE THIS if your PHP server URL is different
    driver.get("http://localhost:8000/index.php")

    yield driver
    driver.quit()
