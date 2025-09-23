import time
from pages.home_page import HomePage
from pages.search_page import SearchPage
from pages.streamer_page import StreamerPage
from utils.helpers import close_known_modals, take_timestamped_screenshot


def test_twitch_select_streamer_and_screenshot(driver):
    home = HomePage(driver)
    home.go()
    time.sleep(1)
    close_known_modals(driver)

    home.click_search()

    search = SearchPage(driver)
    search.scroll_down(times=2, pause=1.0)
    elems = search.list_streamers()
    assert elems, "No streamers found after scrolling"

    search.select_streamer_by_index(0)

    streamer = StreamerPage(driver)
    streamer.wait_until_loaded(timeout=25)
    close_known_modals(driver)

    path = take_timestamped_screenshot(driver, name_prefix="twitch_streamer")
    assert path.exists()
    print(f"Saved screenshot to: {path}")
