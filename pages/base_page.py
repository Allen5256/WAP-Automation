import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

DEFAULT_TIMEOUT = 15

COMMON_MODAL_CLOSE_SELECTORS = [
    "button[aria-label='Close']",
    "button[aria-label='Dismiss']",
    "button[data-a-target='modal-close']",
    ".tw-modal__close",
    ".close",
    "button[title='Close']",
]


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, DEFAULT_TIMEOUT)

    def _is_in_viewport(self, element):
        '''Check if an element is within the viewport'''

        return self.driver.execute_script("""
            var elem = arguments[0],
                box = elem.getBoundingClientRect();
            return (
                box.top >= 0 &&
                box.left >= 0 &&
                box.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                box.right <= (window.innerWidth || document.documentElement.clientWidth)
            );
        """, element)

    def wait_for_element(
        self,
        locator,
        condition=EC.presence_of_element_located
    ):
        return self.wait.until(condition(locator))

    def click_element(
        self,
        locator
    ):
        try:
            el = self.wait_for_element(locator, condition=EC.element_to_be_clickable)
            el.click()
        except TimeoutException as e:
            raise AssertionError(f"Element {locator} not clickable") from e

    def scroll_down(self, times=1):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight || 800);")
            time.sleep(1)

    def wait_for_all_clickable(self, locator, timeout=DEFAULT_TIMEOUT):

        def _all_clickable(driver):
            elements = driver.find_elements(*locator)
            ready = [e for e in elements if e.is_displayed() and e.is_enabled()]
            return ready or False

        return WebDriverWait(self.driver, timeout).until(_all_clickable)

    def close_known_modals(self, driver):
        for sel in COMMON_MODAL_CLOSE_SELECTORS:
            elems = self.wait_for_all_clickable((By.CSS_SELECTOR, sel))
            for ele in elems:
                try:
                    ele.click()
                except Exception:
                    try:
                        driver.execute_script("arguments[0].click();", ele)
                    except Exception:
                        pass
                time.sleep(0.5)
