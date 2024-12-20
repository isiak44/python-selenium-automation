from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SigninPage(BasePage):

    INPUT_LOGIN = (By.CSS_SELECTOR, "#username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#password")
    LOGIN_BTN = (By.CSS_SELECTOR, "#login")

    SIGNINP_HEADER = (By.CSS_SELECTOR, "h1>span")

    def verify_signin_page(self):
        self.verify_text('Sign into your Target account', *self.SIGNINP_HEADER )

    def signin_to_profile(self):
        self.input_text('tinarm@caychayyy.shop', *self.INPUT_LOGIN)
        self.input_text('*****', *self.INPUT_PASSWORD)
        self.click(*self.LOGIN_BTN)

    def verify_signin_success(self):
        self.wait_until_not_visible(*self.SIGNINP_HEADER)

