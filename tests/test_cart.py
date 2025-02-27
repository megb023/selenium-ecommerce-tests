"""
This script tests the cart functionality of https://demo.opencart.com/.
"""

from test_data.products import PRODUCTS

def test_cart_single_item(home_page, cart_page):
    ITEM_NAME = "iPhone"

    # Given there is one item in the cart
    home_page.add_item_to_cart(ITEM_NAME)

    # When the user goes to the cart page
    home_page.wait_for_toast_disappearance()
    home_page.go_to_cart_page()

    # Then the item is in the cart
    assert ITEM_NAME in cart_page.get_item_names()

    # And the correct total price is displayed
    assert cart_page.get_total_price() == PRODUCTS[ITEM_NAME]

    # When the item quantity increases by 1
    cart_page.update_product_quantity(1, 2)

    # Then the price updates correctly
    home_page.wait_for_toast_disappearance()
    assert cart_page.get_total_price() == "$246.40"

    # When you remove the item from the cart
    cart_page.remove_item(1)

    # Then the no item in cart message is displayed
    assert cart_page.check_empty_cart_text()

  
def test_cart_multiple_items(home_page, cart_page):
    FIRST_ITEM = "iPhone"
    SECOND_ITEM = "MacBook"

    # Given there is two different items in the cart
    home_page.add_item_to_cart(FIRST_ITEM)
    home_page.wait_for_toast_disappearance()
    home_page.add_item_to_cart(SECOND_ITEM)

    # When the user goes to the cart page
    home_page.wait_for_toast_disappearance()
    home_page.go_to_cart_page()

    # Then both items are in the cart
    assert FIRST_ITEM in cart_page.get_item_names()
    assert SECOND_ITEM in cart_page.get_item_names()

    # And the correct total price is displayed
    assert cart_page.get_total_price() == "$725.20"

    # When one item quantity is increased by and the other by 2
    cart_page.update_product_quantity(1, 2)
    home_page.wait_for_toast_disappearance()
    cart_page.update_product_quantity(2, 3)
    home_page.wait_for_toast_disappearance()

    # Then the price updates correctly
    assert cart_page.get_total_price() == "$2,052.40"

    # When you remove both items from the cart
    cart_page.remove_item(1)
    home_page.wait_for_toast_disappearance()
    cart_page.remove_item(1)

    # Then the no item in cart message is displayed
    assert cart_page.check_empty_cart_text()
  
def test_cart_persistence(home_page, cart_page):
    ITEM_NAME = "iPhone"

    # Given there is one item in the cart
    home_page.add_item_to_cart(ITEM_NAME)

    # When you refresh the page
    home_page.refresh_page()
    

    # Then the item should still be in the cart
    home_page.go_to_cart_page()
    assert ITEM_NAME in cart_page.get_item_names()