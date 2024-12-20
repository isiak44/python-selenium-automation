from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from features.steps.search_result_steps import store_product_name




class CartPage(BasePage):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    ACTUAL_ITEM_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
    ACTUAL_ITEM_PRICE = (By.CSS_SELECTOR, ".h-margin-b-tight span")

    def target_cart_page(self):
        self.open_url('https://www.target.com/cart')

    def verify_empty_cart(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_item_by_name(self, expected_name):
        self.verify_partial_text(expected_name, *self.ACTUAL_ITEM_NAME)

    def verify_item_by_price(self, expected_price):
        self.verify_partial_text(expected_price,  *self.ACTUAL_ITEM_PRICE)