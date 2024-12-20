from time import sleep

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Header(BasePage):

    SEARCH_BOX = (By.CSS_SELECTOR, "#search")
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    CART_BTN = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    SIGNIN_BTN = (By.XPATH, "//*[@data-test= 'accountNav-signIn']")
    SIGNIN_NAV = (By.ID, 'account-sign-in')
    CIRCLE_PAGE_BTN = (By.CSS_SELECTOR, "#utilityNav-circle")

    def search_products(self, product):
        self.clear(*self.SEARCH_BOX)
        self.input_text(product, *self.SEARCH_BOX)
        self.click(*self.SEARCH_BTN)
        sleep(2)

    def cart_icon(self):
        self.click(*self.CART_BTN)

    def signin_btn(self):
        self.click(*self.SIGNIN_BTN)

    def signin_nav_btn(self):
        self.click(*self.SIGNIN_NAV)

    def click_circle_page_btn(self):
        self.click(*self.CIRCLE_PAGE_BTN)

