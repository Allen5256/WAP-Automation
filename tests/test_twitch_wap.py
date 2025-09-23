import time
from pages import initialize_pages
from utils.helpers import close_known_modals, take_timestamped_screenshot


class TestTwitchWAP:
    def test_twitch_select_streamer_and_screenshot(driver):

        initialize_pages(driver)
        
        # Navigate to home page
        home = driver.home_page
        home.go()
        time.sleep(1)
        close_known_modals(driver)

        # Click the search icon and search for a keyword
        home.click_search()
        home.search("starCraft II")

        # On the search page, scroll and list streamers
        search = driver.search_page
        search.scroll_down(times=2, pause=1.0)
        elems = search.list_streamers()
        assert elems, "No streamers found after scrolling"

        # Select the first streamer from the list
        search.select_streamer_by_index(0)

        # On the streamer page, wait until loaded and handle the popups or modals
        streamer = driver.streamer_page
        streamer.wait_until_loaded(timeout=25)
        close_known_modals(driver)

        # Take a timestamped screenshot of the streamer page
        path = take_timestamped_screenshot(driver, name_prefix="twitch_streamer")
        assert path.exists()
        print(f"Saved screenshot to: {path}")
