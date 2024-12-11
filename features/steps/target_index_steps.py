from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_BOX = (By.CSS_SELECTOR, "#search")
SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
CIRCLE_PAGE_BTN = (By.CSS_SELECTOR, "#utilityNav-circle")
SIGNIN_BTN = (By.XPATH, "//*[@data-test= 'accountNav-signIn']")
CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


@given('Open Target page')
def open_main_page(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Open signin navigation')
def open_signin_nav(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()


@when('Click signin button')
def click_signin(context):
    context.driver.find_element(*SIGNIN_BTN).click()


@when('Locate and click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_BTN).click()


@when('locate target search box')
def search_box(context):
    context.driver.find_element(*SEARCH_BOX).clear()


@when('input {product} to target search box')
def input_to_search_box(context, product):
    context.driver.find_element(*SEARCH_BOX).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(2)


@when('Open Target circle page from header')
def open_circle_page(context):
    context.driver.find_element(*CIRCLE_PAGE_BTN).click()
