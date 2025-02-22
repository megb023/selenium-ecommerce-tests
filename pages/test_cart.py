"""
Page object for the cart of https://demo.opencart.com/
"""

class OpenCartCartPage: 
    
    
    SEARCH_INPUT = (By.NAME, 'search')

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    