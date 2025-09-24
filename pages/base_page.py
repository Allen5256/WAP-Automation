import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import close_known_modals

DEFAULT_TIMEOUT = 15


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)

    def wait_for_element(
        self,
        locator,
        condition=EC.presence_of_element_located
    ):
        return self.wait.until(condition(locator))

    def click_element(
        self,
        locator,
        condition=EC.element_to_be_clickable,
        timeout=DEFAULT_TIMEOUT,
    ):
        try:
            el = self.wait_for_element(locator, condition=condition)
            try:
                el.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", el)
        except TimeoutException:
            raise AssertionError(f"Element {locator} not clickable")

    def scroll_down(self, times=1, pause=1.0):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight || 800);")
            time.sleep(pause)
            close_known_modals(self.driver)
