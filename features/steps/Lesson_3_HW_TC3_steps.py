from behave import when, then


@when('Click on Sign In icon')
def click_on_sign_in_icon(context):
    context.app.target_homepage.click_sign_in_icon()


@then('Click on sidebar Sign In Icon')
def click_on_sidebar_sign_in_icon(context):
    context.app.target_homepage_account_sidebar.click_on_sidebar_sign_in_icon()


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    assert context.app.target_signin_page.wait_until_signin_button_visible(), "Sign In form failed to open"
