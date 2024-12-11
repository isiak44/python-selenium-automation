from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, "[data-test$='CellsComponent/Link']")

@then ('Locate 14 benefit cells')
def locate_benefit_cells(context):
    cells=context.driver.find_elements(*BENEFIT_CELLS)
    print(len(cells))

