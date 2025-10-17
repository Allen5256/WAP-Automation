import allure

from utils.helpers import take_screenshot


class TestTwitchWAP:

    @allure.title("Twitch WAP: Verify search and Screenshot Streamer Page")
    @allure.description("End-to-end test navigating Twitch mobile site, searching for a streamer, and taking a screenshot.")
    def test_twitch_select_streamer_and_screenshot(self, driver, home_page, search_page, streamer_page):

        with allure.step("Navigate to Twitch mobile homepage"):
            home_page.go()

        with allure.step("Search for 'starCraft II'"):
            home_page.search("starCraft II")

        with allure.step("View all streamer/channel search results"):
            search_page.view_all_channels()

        with allure.step("Scroll down 2 times"):
            search_page.scroll_down(times=2)

        with allure.step("Select the first streamer from the list"):
            search_page.select_random_visible_streamer()

        with allure.step("Wait for the streamer page to load and handle any popups/modals"):
            loaded = streamer_page.wait_until_loaded()
            assert loaded, "Streamer page did not load properly"

        with allure.step("Take a timestamped screenshot of the streamer page"):
            take_screenshot(driver, prefix="success")
