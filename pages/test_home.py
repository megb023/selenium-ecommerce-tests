"""
Page object for the homepage of https://demo.opencart.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OpenCartHomePage: 
    
    URL = 'https://demo.opencart.com/'
    SEARCH_INPUT = (By.NAME, 'search')
    ITEM_NAMES = (By.CSS_SELECTOR, '.description>h4')
    ADD_TO_CART = (By.CSS_SELECTOR, '.button-group>button:nth-child(1)')
    ITEM_PRICE = (By.CLASS_NAME, 'price-new')
    TOAST_MESSAGE = (By.CLASS_NAME, 'alert-success')
    CART_BUTTON = (By.CSS_SELECTOR, "button[data-bs-toggle='dropdown']")

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def add_item_to_cart(self, item):
        # Find the index of item and scroll to bottom of page
        featured_items = self.browser.find_elements(*self.ITEM_NAMES)
        item_names = [i.text for i in featured_items]
        item_location = item_names.index(item)
        actions = ActionChains(self.browser)
        actions.scroll_by_amount(0, 1000).perform()

        # Click the add to cart button for the corresponding item
        self.browser.find_elements(*self.ADD_TO_CART)[item_location].click()

        # Wait until the cart button text updates
        WebDriverWait(self.browser, 3).until(
            EC.text_to_be_present_in_element(
                self.CART_BUTTON, "1 item(s)"
            )
        )



    def get_toast_message_text(self):
        return self.browser.find_element(*self.TOAST_MESSAGE).text

    def get_cart_button_text(self):
        return self.browser.find_element(*self.CART_BUTTON).text