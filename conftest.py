import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

MOBILE_DEVICE_NAME = "Pixel 2"

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    mobile_emulation = {"deviceName": MOBILE_DEVICE_NAME}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    if os.getenv("HEADLESS", "0") == "1":
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=412,915")

    # driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()
