from time import sleep

from behave import given, when, then


@when('Store original window')
def store_origin_window(context):
    context.original_window = context.app.base_page.get_current_window_handle()


@when('Click on Target terms and conditions link')
def click_terms_and_condition(context):
    context.app.signin_page.open_terms_and_con_page()


@when('Switch to the newly opened window')
def switch_to_window(context):
    context.app.signin_page.switch_to_new_window()


@when('Login with a valid email and password')
def login_credentials(context):
    context.app.signin_page.signin_valid_cred()


@when('Login with an invalid email and password')
def login_invalid_cred(context):
    context.app.signin_page.signin_invalid_cred()


@then('Verify signin page pops up')
def verify_signin_pg(context):
    context.app.signin_page.verify_signin_page()


@then('Verify user is logged in successfully')
def verify_login_success(context):
    context.app.signin_page.verify_signin_success()


@then('Verify error message is displayed')
def verify_login_error(context):
    context.app.signin_page.verify_login_error()