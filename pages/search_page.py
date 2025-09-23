import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from .base_page import BasePage
from utils.helpers import close_known_modals


class SearchPage(BasePage):
    STREAMER_LINKS = (
        By.CSS_SELECTOR,
        "a[data-a-target='preview-card-image-link'], a[href*='/videos/'], a[href*='/channel/']",
    )

    def scroll_down(self, times: int = 2, pause: float = 1.0):
        for _ in range(times):
            self.driver.execute_script("window.scrollBy(0, window.innerHeight || 800);")
            time.sleep(pause)
            close_known_modals(self.driver)

    def list_streamers(self):
        try:
            self.wait_for_element(
                self.STREAMER_LINKS,
                condition=lambda loc: len(self.driver.find_elements(*loc)) > 0,
            )
        except TimeoutException:
            return []
        elems = self.driver.find_elements(*self.STREAMER_LINKS)
        return [e for e in elems if e.is_displayed()]

    def select_streamer_by_index(self, index=0):
        elems = self.list_streamers()
        if not elems:
            raise AssertionError("No streamers found on search/list page")
        target = elems[index]
        href = target.get_attribute("href")
        if href:
            self.driver.get(href)
        else:
            # fallback using click_element
            self.click_element((By.XPATH, f"({self.STREAMER_LINKS[1]})[{index+1}])"))
