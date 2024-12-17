from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchResult(BasePage):
    SEARCH_RESULT = (By.XPATH, "//div[@data-test='resultsHeading']")

    def verify_search(self, product):
        actual_result = self.find_element(*self.SEARCH_RESULT).text
        assert product in actual_result, f'Expected text {product} not in {actual_result}'


