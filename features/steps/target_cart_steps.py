from time import sleep
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

@when('Open target cart page')
def open_cart_page(context):
    context.app.cart_page.target_cart_page()

@then("Verify cart is empty message")
def verify_cart(context):
    context.app.cart_page.verify_empty_cart()


@then('Verify cart has correct product price')
def verify_product_price(context):
    actual_price = context.driver.find_element(By.CSS_SELECTOR, ".h-margin-b-tight span").text
    print(f'Actual product price is: {actual_price}')
    print(f'Product price stored earlier: {context.product_price}')
    assert context.product_price in actual_price, f'{context.product_price} is not  {actual_price}'


@then('Verify cart has correct product name')
def verify_product_name(context):
    actual_name = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print(f'Actual product in cart name: {actual_name}')
    print(f'Product name stored earlier: {context.product_name}')
    assert context.product_name in actual_name, f"Expected {context.product_name} but got {actual_name}"


