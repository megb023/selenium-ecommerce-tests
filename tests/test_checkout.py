"""
This script tests the checkout functionality of https://demo.opencart.com/.
"""

from pages.test_home import OpenCartHomePage

def test_checkout_with_items():
  
    # Given the cart has at least one item

    # When you click the checkout tab in the header

    # Then the checkout page should appear

    # And the product that was in the cart should be listed

    # And the total price should be correct

def test_checkout_without_items():

    # Given you are at the home page with no items in the cart

    # When you navigate to the checkout page

    # Then the page should be empty and display message "Your shopping cart is empty!"