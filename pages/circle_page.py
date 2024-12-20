from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CirclePage(BasePage):
    BENEFIT_CELLS = (By.CSS_SELECTOR, "[data-test$='CellsComponent/Link']")

    def benefit_cells(self):
        self.find_elements(*self.BENEFIT_CELLS)