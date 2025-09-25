import time
import allure

from utils.helpers import close_known_modals, take_timestamped_screenshot


class TestTwitchWAP:
    @allure.title("Twitch WAP: Verify search and Screenshot Streamer Page")
    @allure.description("End-to-end test navigating Twitch mobile site, searching for a streamer, and taking a screenshot.")
    def test_twitch_select_streamer_and_screenshot(self, driver, home_page, search_page, streamer_page):

        with allure.step("Navigate to Twitch mobile homepage"):
            home_page.go()
            time.sleep(1)
            close_known_modals(driver)

        with allure.step("Search for 'starCraft II'"):
            home_page.search("starCraft II")

        with allure.step("View all streamer/channel search results"):
            search_page.view_all_channels()

        with allure.step("Scroll through search results"):
            search_page.scroll_down(times=2, pause=1.0)
            assert search_page.list_streamers(), "No streamers found after scrolling"

        with allure.step("Select the first streamer from the list"):
            search_page.select_streamer_by_index(0)
        
        with allure.step("Wait for the streamer page to load and handle any popups/modals"):
            streamer_page.wait_until_loaded()
            close_known_modals(driver)

        with allure.step("Take a timestamped screenshot of the streamer page"):
            path = take_timestamped_screenshot(driver, name_prefix="twitch_streamer")
            assert path.exists()
            print(f"Saved screenshot to: {path}")
