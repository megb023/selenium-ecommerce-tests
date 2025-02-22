"""
This script tests the search functionality of https://demo.opencart.com/.
"""

from pages.test_home import OpenCartHomePage
from pages.test_search import OpenCartSearchPage

def test_valid_search(browser):
    home_page = OpenCartHomePage(browser)
    result_page = OpenCartSearchPage(browser)
    PHRASE = "Macbook"
  
    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches "Macbook"
    home_page.search(PHRASE)

    # Then the search result title contains "Macbook"
    assert PHRASE.lower() in result_page.get_page_title().lower()

    # And the search results contain "Macbook"
    titles = result_page.get_result_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0 , f"No results contained '{PHRASE}'"

def test_invalid_search(browser):
    home_page = OpenCartHomePage(browser)
    result_page = OpenCartSearchPage(browser)
    PHRASE = "123qwerty"
    INVALID = "There is no product that matches the search criteria."

    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches "123qwerty"
    home_page.search(PHRASE)

    # Then the search result title contains "123qwerty"
    assert PHRASE.lower() in result_page.get_page_title().lower(), f"Search input 'f{PHRASE}' is not shown in page title"

    # And the search result is a no product match message
    actual_message = result_page.get_invalid_message()
    assert actual_message == INVALID, f"Expected message '{INVALID}', but got '{actual_message}'"

def test_empty_search(browser):
    home_page = OpenCartHomePage(browser)
    result_page = OpenCartSearchPage(browser)
    PHRASE = ""

    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches ""
    home_page.search(PHRASE)

    # Then the search result title says "Search" only
    assert result_page.get_page_title() == "Search", "Page title contains something other than 'Search'"