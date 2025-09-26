from selenium.common.exceptions import (ElementClickInterceptedException,
                                        TimeoutException)
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

BASE_URL = 'https://m.twitch.tv/'


class HomePage(BasePage):
    # Page locators
    BROWSE_ICON = (
        By.CSS_SELECTOR,
        'a[href="/directory"]',
    )
    SEARCH_INPUT = (
        By.CSS_SELECTOR,
        'input[type="search"]',
    )

    def go(self):
        self.driver.get(BASE_URL)

    def click_browse(self):
        try:
            el = self.wait_for_element(
                self.BROWSE_ICON, condition=EC.element_to_be_clickable
            )
            try:
                el.click()
            except ElementClickInterceptedException:
                self.driver.execute_script('arguments[0].click();', el)
        except TimeoutException as e:
            raise AssertionError('Browse icon not found on home page') from e

    def search(self, keyword):
        self.click_browse()
        search_input = self.wait_for_element(self.SEARCH_INPUT)
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.RETURN)
