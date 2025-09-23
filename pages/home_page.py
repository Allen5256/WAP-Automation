from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from .base_page import BasePage

BASE_URL = "https://m.twitch.tv/"

class HomePage(BasePage):
    SEARCH_ICON = (By.CSS_SELECTOR, "button[data-a-target='search-button'], button[aria-label='Search']")

    def go(self):
        self.driver.get(BASE_URL)

    def click_search(self):
        try:
            el = self.wait_for_element(self.SEARCH_ICON, condition=EC.element_to_be_clickable)
            try:
                el.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", el)
        except TimeoutException:
            raise AssertionError("Search icon not found on home page")
