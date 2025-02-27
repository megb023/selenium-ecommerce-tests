"""
This script tests the home page functionality of https://demo.opencart.com/.
"""

from test_data.products import PRODUCTS
ITEM_NAME = "iPhone"
ITEM_COST = PRODUCTS[ITEM_NAME]

def test_add_item_to_cart(home_page):
    # When the user adds a product to the cart
    home_page.add_item_to_cart(ITEM_NAME)

    # Then a toast message confirms the product was added
    assert home_page.get_toast_message_text() == f"Success: You have added {ITEM_NAME} to your shopping cart!"

    # And the cart button shows the updated quantity and price
    assert home_page.get_cart_button_text() == f"1 item(s) - {ITEM_COST}"

    # And the cart button dropdown menu has the added item
    home_page.wait_for_toast_disappearance()
    home_page.click_cart_button_dropdown()
    dropdown_item = home_page.get_item_from_dropdown()
    assert dropdown_item == ITEM_NAME

def test_remove_item_from_cart(home_page):
    # Given the user already has at least one item in the cart
    home_page.add_item_to_cart(ITEM_NAME)
    home_page.wait_for_toast_disappearance()

    # When the user removes all items from the cart
    home_page.click_cart_button_dropdown()
    home_page.remove_item_dropdown()

    # Then a toast message confirms the product was removed
    assert home_page.get_toast_message_text() == "Success: You have removed an item from your shopping cart!"

    # And the cart button shows the cart is empty
    assert home_page.get_cart_button_text() == "0 item(s) - $0.001"

    # And the cart button dropdown menu is empty
    home_page.wait_for_toast_disappearance()
    home_page.click_cart_button_dropdown()
    assert home_page.get_empty_dropdown_text() == "Your shopping cart is empty!"

