from behave import given, when, then




@then('Verify Terms and Conditions page is opened')
def verify_terms_and_cons_opened(context):
    context.app.terms_and_cons_page.verify_t_and_c_opened()


@then('User can close new window and switch back to original')
def close_window_and_switch_to_original_window(context):
    context.app.base_page.close_current_window()
    context.app.base_page.switch_window_by_id(context.original_window)


