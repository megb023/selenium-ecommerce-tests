"""
This script tests the search functionality of https://demo.opencart.com/.
"""

from pages.test_home import OpenCartHomePage
from pages.test_search import OpenCartSearchPage

def test_valid_search(browser):
    home_page = OpenCartHomePage(browser)
    result_page = OpenCartSearchPage(browser)
    PHRASE = "123"
  
    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches "Macbook"
    home_page.search(PHRASE)

    # Then the search result title contains "Macbook"
    assert PHRASE.lower() in result_page.search_page_title().lower()

    # And the search results contain "Macbook"
    titles = result_page.search_result_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0 , f"No results contained '{PHRASE}'"
