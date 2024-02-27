from behave import then

@then('Sign In with invalid credentials')
def sign_in_invalid_credentials(context):
    context.app.target_signin_page.invalid_sign_in()

@then('Verify "Can\'t Find Account" Message is shown')
def verify_cannot_find_account_message(context):
    context.app.target_signin_page.verify_signin_error_message_shown()
