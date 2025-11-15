import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="module")
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")

    # USE LOCAL CHROMEDRIVER (NO INTERNET REQUIRED)
    service = Service("C:/QUIZ_ASSIGNMENT/chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.set_window_size(1920, 1080)

    driver.get("http://localhost:8000/src/html/index.html")

    yield driver
    driver.quit()
