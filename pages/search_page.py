import random

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class SearchPage(BasePage):
    CHANNELS_VIEW_ALL = (
        By.CSS_SELECTOR,
        'p[aria-label="View All Channel Search Results"]',
    )

    STREAMER_CARDS = (
        By.CSS_SELECTOR,
        "button.tw-link"
    )

    def view_all_channels(self):
        try:
            self.click_element(
                self.CHANNELS_VIEW_ALL
            )
        except TimeoutException as e:
            raise AssertionError("View All Channels link not found on search page") from e

    def select_random_visible_streamer(self, only_viewport=True):
        try:
            elems = self.wait_for_all_clickable(self.STREAMER_CARDS)
        except TimeoutException as e:
            raise AssertionError("No streamer links found on search results page") from e

        if only_viewport:
            elems = [e for e in elems if self._is_in_viewport(e)]

        if not elems:
            raise AssertionError("No streamer links are visible in viewport")

        target = random.choice(elems)
        target.click()
