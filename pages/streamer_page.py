import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from utils.helpers import close_known_modals

class StreamerPage(BasePage):
    VIDEO_PLAYER = (By.CSS_SELECTOR, "video, [data-a-player-state], iframe")
    STREAMER_NAME = (By.CSS_SELECTOR, "h1, h2, .tw-c-text-heading-1, .channel-header__user")

    def wait_until_loaded(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(self.STREAMER_NAME)
            )
        except TimeoutException:
            try:
                WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located(self.VIDEO_PLAYER)
                )
            except TimeoutException:
                raise AssertionError("Streamer page did not load expected elements")
        close_known_modals(self.driver)
        time.sleep(1)
