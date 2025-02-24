"""
This script tests the cart functionality of https://demo.opencart.com/.
"""

def test_cart_single_item(home_page, cart_page):
    # Given there is one item in the cart

    # When the user goes to the cart page

    # Then the item is in the cart

    # And the correct total price is displayed

    # When the item quantity increases by 1

    # Then the price updates correctly

    # When you remove the item from the cart

    # Then the no item in cart message is displayed

  
def test_cart_multiple_items(home_page):
    # Given there is two different items in the cart

    # When the user goes to the cart page

    # Then both items are in the cart

    # And the correct total price is displayed

    # When one item quantity is increased and the other is decreased by 1

    # Then the price updates correctly

    # When you remove both items from the cart

    # Then the no item in cart message is displayed
  
def test_cart_persistence(home_page):
    # Given there is one item in the cart

    # When you refresh the page

    # Then the item should still be in the cart