"""
This module contains page object for the search page of https://demo.opencart.com/
"""

from selenium.webdriver.common.by import By

class OpenCartSearchPage:

    SEARCH_RESULTS = (By.CSS_SELECTOR, "#product-list .description>h4>a")
    SEARCH_TITLE = (By.CSS_SELECTOR, "#content>h1")

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def search_result_titles(self):
        results = self.browser.find_elements(*self.SEARCH_RESULTS)
        result_titles = [result.text for result in results]
        return result_titles
    
    def search_page_title(self):
        page_title = self.browser.find_element(*self.SEARCH_TITLE).text
        return page_title
    
    def check_for_no_results(self):
        results = self.browser.find_elements(*self.SEARCH_RESULTS)
        return len(results) > 0


