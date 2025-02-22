"""
This script tests the cart functionality of https://demo.opencart.com/.
"""

from pages.test_home import OpenCartHomePage

def test_add_item_to_cart():

    # Given the opencart home page is displayed

    # When the user adds a product to the cart

    # Then a toast message confirms the product was added

    # And the cart button shows the updated quantity and price

    # And navigating to the cart shows the product in the cart

def test_remove_item_from_cart():

    # Given the user already at least one item in the cart

    # When the user removes all items from the cart

    # Then a toast message confirms the product was removed

    # And the cart button shows the cart is empty

    # And navigating to the cart confirms no products remain


    """ 
    def test_cart_persistence():
        # TODO
    def test_update_cart_quantity():
        # TODO
    """