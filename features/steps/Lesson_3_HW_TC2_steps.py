from behave import when, then


@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.app.target_homepage.click_cart_button()

@then('Cart Empty Message Shown')
def verify_cart_empty_message(context):
    error_msg: str = "Empty cart page failed to open or cart has items in it"

    assert context.app.target_cart_page.get_cart_empty_message() == "Your cart is empty", error_msg
