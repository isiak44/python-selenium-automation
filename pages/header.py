from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):

    SEARCH_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")

    def search_products(self, product):
        self.clear(*self.SEARCH_BOX)
        self.input_text(product, *self.SEARCH_BOX)
        self.click(*self.SEARCH_BTN)
        sleep(2)

    def cart_icon(self):
        self.click(*self.CART_BTN)
