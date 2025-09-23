from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DEFAULT_TIMEOUT = 15

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)

    def wait_for_element(self, locator, condition=EC.presence_of_element_located, timeout: int = DEFAULT_TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(condition(locator))

    def click_element(self, locator, condition=EC.element_to_be_clickable, timeout: int = DEFAULT_TIMEOUT):
        try:
            el = self.wait_for_element(locator, condition=condition, timeout=timeout)
            try:
                el.click()
            except Exception:
                self.driver.execute_script("arguments[0].click();", el)
        except TimeoutException:
            raise AssertionError(f"Element {locator} not clickable")
