from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage


class SearchPage(BasePage):
    STREAMER_LINKS = (
        By.CSS_SELECTOR,
        "a[data-a-target='preview-card-image-link'], a[href*='/videos/'], a[href*='/channel/']",
    )

    def list_streamers(self):
        try:
            self.wait_for_element(
                self.STREAMER_LINKS,
                condition=EC.presence_of_all_elements_located,
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
        if href := target.get_attribute("href"):
            self.driver.get(href)
        else:
            # fallback using click_element
            self.click_element((By.XPATH, f"({self.STREAMER_LINKS[1]})[{index+1}])"))
