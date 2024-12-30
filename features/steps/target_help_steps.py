from behave import given, when, then
from selenium.webdriver.common.by import By

DD_MENU = (By.CSS_SELECTOR, "select[id*='contentTemplate']")
LEFT_NAV_H2 = (By.CSS_SELECTOR, "#leftNavArea h2")

@given('Open target help page for returns')
def open_target_help_page(context):
    context.app.help_page.open_help_page()


@when('Select help topic {selected_topic} in dropdown')
def select_topic(context, selected_topic):
    context.app.help_page.select_from_help_dd(selected_topic)


@then('Verify help topic {selected_topic} page opened')
def verify_topic(context, selected_topic):
    context.app.help_page.verify_selected_topic(selected_topic)

