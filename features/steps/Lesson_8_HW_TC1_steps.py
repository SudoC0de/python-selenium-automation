from behave import then


@then('Switch to Terms and Conditions')
def switch_to_terms_and_conditions(context):
    context.app.target_signin_page.switch_to_terms_and_conditions()
