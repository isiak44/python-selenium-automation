from pages.base_page import BasePage

class HomePage(BasePage):

    def open_home_page(self):
        self.open_url('https://www.target.com/')

