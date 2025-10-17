import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages import initialize_pages
from utils.helpers import take_screenshot

MOBILE_DEVICE_NAME = "Pixel 2"
HEADLESS = 1  # Set to 1 to run tests in headless mode


@pytest.fixture(name="driver", scope="function")
def init_driver():
    chrome_options = Options()
    service = Service(ChromeDriverManager().install())
    mobile_emulation = {"deviceName": MOBILE_DEVICE_NAME}
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    chrome_options.add_argument("--window-size=412,915")
    if HEADLESS:
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

    chrome_driver = webdriver.Chrome(service=service, options=chrome_options)
    chrome_driver.implicitly_wait(2)
    yield chrome_driver
    chrome_driver.quit()


@pytest.fixture(name="home_page")
def init_home_page(driver):
    initialize_pages(driver)
    return driver.home_page


@pytest.fixture(name="search_page")
def init_search_page(driver):
    initialize_pages(driver)
    return driver.search_page


@pytest.fixture(name="streamer_page")
def init_streamer_page(driver):
    initialize_pages(driver)
    return driver.streamer_page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''Capture screenshot on test failure and attach to Allure report'''

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            take_screenshot(driver, prefix="failed", test_name=item.name)
