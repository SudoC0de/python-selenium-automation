from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when('Add Coffee To Cart')
def add_coffee_to_cart(context):
    context.app.target_homepage.execute_search("coffee")
    context.app.target_search_results_page.add_to_cart_first_result()
    context.app.target_cart_sidebar.click_add_to_cart_button()

@then('Verify Coffee Added To Cart')
def verify_coffee_added(context):
    label_text: str = context.app.target_cart_sidebar.get_cart_label_text()

    context.app.target_cart_sidebar.view_cart_after_add()

    cart_text: str = context.app.target_cart_page.get_cart_title_text()

    assert label_text in cart_text, f"\"{label_text}\" was not added to the cart. \"{cart_text}\" was added instead."
