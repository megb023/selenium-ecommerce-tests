"""
Page object for the search page of https://demo.opencart.com/
"""

from selenium.webdriver.common.by import By

class OpenCartSearchPage:

    SEARCH_RESULTS = (By.CSS_SELECTOR, "#product-list .description>h4>a")
    SEARCH_TITLE = (By.CSS_SELECTOR, "#content>h1")
    INVALID_RESULTS = (By.CSS_SELECTOR, "#content p")

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def get_result_titles(self):
        results = self.browser.find_elements(*self.SEARCH_RESULTS)
        result_titles = [result.text for result in results]
        return result_titles
    
    def get_page_title(self):
        page_title = self.browser.find_element(*self.SEARCH_TITLE).text
        return page_title
    
    def get_invalid_message(self):
        invalid_message = self.browser.find_element(*self.INVALID_RESULTS).text
        return invalid_message


