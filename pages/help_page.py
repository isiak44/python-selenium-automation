from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

class HelpPage(BasePage):
    DD_MENU = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")
    HEADER_TXT = (By.XPATH, "//h1[text()=' {SUBSTRING}']")

    def get_header_locator(self, text):
        return [self.HEADER_TXT[0], self.HEADER_TXT[1].replace('{SUBSTRING}', text)]

    def open_help_page(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_from_help_dd(self, topic):
        dropdown_menu = self.find_element(*self.DD_MENU)
        select = Select(dropdown_menu)
        select.select_by_value(topic)

    def verify_selected_topic(self, selected_topic):
        locator = self.get_header_locator(selected_topic)
        self.wait_until_visible(*locator)
