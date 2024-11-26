from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')


@when('Open signin navigation')
def open_signin_nav(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()


@when('Click signin button')
def click_signin(context):
    context.driver.find_element(By.XPATH, "//*[@data-test= 'accountNav-signIn']").click()


@then('Verify signin page pops up')
def verify_signin(context):
    expected_result = 'Sign into your Target account'
    # actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into')]").text
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1>span").text
    assert expected_result in actual_result, f'{expected_result} not found in {actual_result}'

@when('Locate and click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@then("Verify cart is empty message")
def verify_cart(context):
    expected_text = 'Your cart is empty'
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_text in actual_text, f'{expected_text} not found in {actual_text}'

    sleep(2)