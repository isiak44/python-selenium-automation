from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class TermsAndConsPage(BasePage):


    def verify_t_and_c_opened(self):
        self.verify_partial_url('terms-condition')