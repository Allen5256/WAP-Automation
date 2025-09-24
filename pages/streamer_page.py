import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.helpers import close_known_modals

from .base_page import BasePage


class StreamerPage(BasePage):
    STREAMER_NAME = (
        By.CSS_SELECTOR,
        "h1, h2, .tw-c-text-heading-1, .channel-header__user",
    )
    VIDEO_PLAYER = (
        By.CSS_SELECTOR,
        "video, [data-a-player-state], iframe"
    )

    def wait_until_loaded(self):
        try:
            self.wait_for_element(self.STREAMER_NAME)
        except TimeoutException:
            try:
                self.wait_for_element(self.VIDEO_PLAYER)
            except TimeoutException:
                raise AssertionError("Streamer page did not load expected elements")
        close_known_modals(self.driver)
        time.sleep(1)
