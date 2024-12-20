from selenium.webdriver.common.by import By
from behave import given, when, then




@then ('Locate 14 benefit cells')
def locate_benefit_cells(context):
    benefit_cells = context.app.circle_page.benefit_cells()

