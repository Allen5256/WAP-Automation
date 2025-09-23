import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from utils.helpers import close_known_modals


class StreamerPage(BasePage):
    STREAMER_NAME = (
        By.CSS_SELECTOR,
        "h1, h2, .tw-c-text-heading-1, .channel-header__user",
    )
    VIDEO_PLAYER = (
        By.CSS_SELECTOR, 
        "video, [data-a-player-state], iframe"
    )

    def wait_until_loaded(self, timeout=30):
        try:
            self.wait_for_element(
                self.STREAMER_NAME,
                timeout=timeout,
            )
        except TimeoutException:
            try:
                self.wait_for_element(
                    self.VIDEO_PLAYER,
                    timeout=timeout,
                )
            except TimeoutException:
                raise AssertionError("Streamer page did not load expected elements")
        close_known_modals(self.driver)
        time.sleep(1)
