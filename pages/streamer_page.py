import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class StreamerPage(BasePage):
    VIDEO_PLAYER = (
        By.CSS_SELECTOR,
        "video, [data-a-player-state], iframe"
    )

    def wait_until_loaded(self):
        try:
            self.close_known_modals(self.driver)
        except TimeoutException:
            pass  # if no modals, continue

        try:
            # wait for video player or embedded iframe to be visible
            self.wait_for_element(self.VIDEO_PLAYER, condition=EC.visibility_of_element_located)
            time.sleep(2)  # additional wait to ensure full load
            return True

        except TimeoutException:
            return False
