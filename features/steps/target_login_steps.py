from behave import given, when, then



@then('Verify signin page pops up')
def verify_signin_Pg(context):
    context.app.signin_page.verify_signin_page()


@when('Login with a valid email and password')
def login_credentials(context):
    context.app.signin_page.signin_to_profile()

@then('Verify user is logged in successfully')
def verify_login_success(context):
    context.app.signin_page.verify_signin_success()