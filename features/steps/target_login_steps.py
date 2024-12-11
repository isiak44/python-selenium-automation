from selenium.webdriver.common.by import By
from behave import given, when, then



@then('Verify signin page pops up')
def verify_signin(context):
    expected_result = 'Sign into your Target account'
    # actual_result = context.driver.find_element(By.XPATH, "//*[contains(text(), 'Sign into')]").text
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "h1>span").text
    assert expected_result in actual_result, f'{expected_result} not found in {actual_result}'
