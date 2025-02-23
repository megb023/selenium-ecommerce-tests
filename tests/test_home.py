"""
This script tests the home page functionality of https://demo.opencart.com/.
"""


def test_add_item_to_cart(home_page):
    ITEM_NAME = "iPhone"
    ITEM_COST = "$123.20"

    # When the user adds a product to the cart
    home_page.add_item_to_cart(ITEM_NAME)

    # Then a toast message confirms the product was added
    assert home_page.get_toast_message_text() == f"Success: You have added {ITEM_NAME} to your shopping cart!"

    # And the cart button shows the updated quantity and price
    assert home_page.get_cart_button_text() == f"1 item(s) - {ITEM_COST}"

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