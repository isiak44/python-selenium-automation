from pages.base_page import BasePage
from pages.cart_page import CartPage
from pages.header import Header
from pages.main_page import HomePage
from pages.search_result import SearchResult
from pages.signin_page import SigninPage
from pages.circle_page import CirclePage
from pages.terms_and_cons_page import TermsAndConsPage

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.base_page = BasePage(self.driver)
        self.header = Header(self.driver)
        self.main_page = HomePage(self.driver)
        self.search_result = SearchResult(self.driver)
        self.cart_page = CartPage(self.driver)
        self.signin_page = SigninPage(self.driver)
        self.circle_page = CirclePage(self.driver)
        self.terms_and_cons_page = TermsAndConsPage(self.driver)