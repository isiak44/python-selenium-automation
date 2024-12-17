from selenium.webdriver.common.by import By
from behave import given, when, then


CIRCLE_PAGE_BTN = (By.CSS_SELECTOR, "#utilityNav-circle")
SIGNIN_BTN = (By.XPATH, "//*[@data-test= 'accountNav-signIn']")


@given('Open Target page')
def open_main_page(context):
    context.app.main_page.open_home_page()



@when('Open signin navigation')
def open_signin_nav(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()


@when('Click signin button')
def click_signin(context):
    context.driver.find_element(*SIGNIN_BTN).click()


@when('Locate and click on cart icon')
def click_cart_icon(context):
    context.app.header.cart_icon()


@when('input {product} to target search box')
def input_to_search_box(context, product):
    context.app.header.search_products(product)


@when('Open Target circle page from header')
def open_circle_page(context):
    context.driver.find_element(*CIRCLE_PAGE_BTN).click()
