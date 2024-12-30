from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResult(BasePage):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='chooseOptionsButton']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-test='product-price']")
    ADD_TO_CART_BTN_SIDENAV = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    FAV_BTN = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAV_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def verify_search(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULT)

    def verify_search_url(self, product):
        self.verify_partial_url(product)

    def add_item_to_cart(self):
        self.wait_until_visible_and_click(*self.ADD_TO_CART_BTN)

    def store_item_name(self):
        return self.find_element(*self.PRODUCT_NAME).text

    def store_item_price(self):
        return self.find_element(*self.PRODUCT_PRICE).text

    def add_to_cart_from_nav(self):
        self.wait_and_click(*self.ADD_TO_CART_BTN_SIDENAV)

    def hover_fav_icon(self):
        self.hover_element(*self.FAV_BTN)

    def verify_fav_icon(self):
        self.wait_until_visible(*self.FAV_TOOLTIP_TXT)

