from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def target_cart_page(self):
        self.open_url('https://www.target.com/cart')


    def verify_empty_cart(self):
        expected_text = 'Your cart is empty'
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert expected_text in actual_text, f'{expected_text} not found in {actual_text}'