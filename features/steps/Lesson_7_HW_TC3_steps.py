from behave import then


@then('Sign In Using Test Credentials')
def test_signin(context):
    context.app.target_signin_page.sign_in()
