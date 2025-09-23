from .home_page import HomePage
from .search_page import SearchPage
from .streamer_page import StreamerPage


def initialize_pages(driver):
    driver.home_page = HomePage(driver)
    driver.search_page = SearchPage(driver)
    driver.streamer_page = StreamerPage(driver)
