from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then


CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
ACTUAL_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
ACTUAL_ITEM_PRICE = (By.CSS_SELECTOR, ".h-margin-b-tight span")


@when('Open target cart page')
def open_cart_page(context):
    context.app.cart_page.target_cart_page()

@then("Verify cart is empty message")
def verify_cart(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify cart has correct product price')
def verify_product_price(context):
    context.app.cart_page.verify_item_by_price(context.product_price)
    print(f'Product price stored earlier: {context.product_price}')


@then('Verify cart has correct product name')
def verify_product_name(context):
    context.app.cart_page.verify_item_by_name(context.product_name)
    print(f'Product name stored earlier: {context.product_name}')

