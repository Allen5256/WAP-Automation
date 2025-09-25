import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages import initialize_pages

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

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    initialize_pages(driver)
    return driver.home_page


@pytest.fixture
def search_page(driver):
    initialize_pages(driver)
    return driver.search_page


@pytest.fixture
def streamer_page(driver):
    initialize_pages(driver)
    return driver.streamer_page
