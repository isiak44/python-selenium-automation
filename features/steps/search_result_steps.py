from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
ADD_TO_CART_BTN_SIDENAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
PRODUCT_LIST = (By.CSS_SELECTOR, "[data-test*='ProductCardWrapper']")
PRODUCT_IMAGES = (By.CSS_SELECTOR, "img")
PRODUCT_NAMES = (By.CSS_SELECTOR, "div [data-test*='product-title']")

@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.driver.wait.until(EC.visibility_of_element_located(ADD_TO_CART_BTN))
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('store product price')
def store_product_price(context):
    context.product_price = context.driver.find_element(*PRODUCT_PRICE).text


@when('store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*PRODUCT_NAME).text


@when('Click Add to cart button from side nav')
def confirm_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BTN_SIDENAV)).click()
    # context.driver.find_element(*ADD_TO_CART_BTN_SIDENAV).click()


@then('verify {product} in search result')
def verify_search_result(context, product):
    context.app.search_result.verify_search(product)


@then('Verify each product has a product name and image')
def verify_product_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    #find all products in search result
    list_of_products = context.driver.find_elements(*PRODUCT_LIST)
    #print(list_of_products)
    assert len(list_of_products) > 0, f'no product found'


    for product in list_of_products:
        title = product.find_element(*PRODUCT_NAMES).text
        assert title, 'product name not found'
        #print(title)
        product.find_element(*PRODUCT_IMAGES)