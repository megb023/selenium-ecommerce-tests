"""
This script tests the search functionality of https://demo.opencart.com/.
"""

def test_valid_search(home_page, search_page):
    PHRASE = "Macbook"
  
    # When the user searches "Macbook"
    home_page.search(PHRASE)

    # Then the search result title contains "Macbook"
    assert PHRASE.lower() in search_page.get_page_title().lower()

    # And the search results contain "Macbook"
    titles = search_page.get_result_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0 , f"No results contained '{PHRASE}'"

def test_invalid_search(home_page, search_page):
    PHRASE = "123qwerty"
    INVALID_MSG = "There is no product that matches the search criteria."

    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches "123qwerty"
    home_page.search(PHRASE)

    # Then the search result title contains "123qwerty"
    assert PHRASE.lower() in search_page.get_page_title().lower(), f"Search input 'f{PHRASE}' is not shown in page title"

    # And the search result is a no product match message
    actual_message = search_page.get_invalid_message()
    assert actual_message == INVALID_MSG, f"Expected message '{INVALID_MSG}', but got '{actual_message}'"

def test_empty_search(home_page, search_page):
    PHRASE = ""

    # Given the opencart home page is displayed
    home_page.load()

    # When the user searches ""
    home_page.search(PHRASE)

    # Then the search result title says "Search" only
    assert search_page.get_page_title() == "Search", "Page title contains something other than 'Search'"