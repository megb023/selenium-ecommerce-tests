"""
Page object for the cart of https://demo.opencart.com/
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class OpenCartCartPage:

    PRODUCT_NAMES = (By.CSS_SELECTOR, '.text-wrap>a')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '#shopping-cart tbody>tr>td:nth-child(6)')
    PRODUCT_QTY = (By.CSS_SELECTOR, "input[name='quantity']")
    SUBTOTAL_PRICE = (By.CSS_SELECTOR, '#checkout-total > tr:nth-child(1)>td:nth-child(2)')
    ECO_TAX = (By.CSS_SELECTOR, '#checkout-total > tr:nth-child(2)>td:nth-child(2)')
    VAT = (By.CSS_SELECTOR, '#checkout-total > tr:nth-child(3)>td:nth-child(2)')
    TOTAL_PRICE = (By.CSS_SELECTOR, '#checkout-total > tr:nth-child(4)>td:nth-child(2)')
    REMOVE_BTNS = (By.CSS_SELECTOR, "#shopping-cart .input-group>button.btn-danger")

    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods

    def get_item_names(self):
       items = self.browser.find_elements(*self.PRODUCT_NAMES)
       item_names = [item.text for item in items]
       return item_names
    
    def get_total_price(self):
        return self.browser.find_element(*self.TOTAL_PRICE).text

    def update_product_quantity(self, itemNum, qty):
        indexNum = itemNum - 1
        selected_item = self.browser.find_elements(*self.PRODUCT_QTY)[indexNum]
        selected_item.clear()
        selected_item.send_keys(str(qty) + Keys.RETURN)

    def remove_item(self, itemNum):
        indexNum = itemNum - 1
        selected_item = self.browser.find_elements(*self.REMOVE_BTNS)[indexNum]
        selected_item.click()

    def check_empty_cart_text(self):
        return self.browser.find_element(By.XPATH, "//*[contains(text(), 'Your shopping cart is empty!')]")






