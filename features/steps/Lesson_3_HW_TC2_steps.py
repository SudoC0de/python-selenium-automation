from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()

@then('Cart Empty Message Shown')
def verify_cart_empty_message(context):
    elements: dict[str, tuple[str, str]] = {
        'EmptyCartHTMLContainer': (By.CSS_SELECTOR, "div[data-test='emptyCartContainer']"),
        'EmptyCartMessage': (By.CSS_SELECTOR, "div[data-test='emptyCartContainer'] > div[data-test='boxEmptyMsg'] > h1")
    }

    context.wait.until(EC.visibility_of_element_located(elements['EmptyCartHTMLContainer']))

    cart_message: str = context.driver.find_element(*elements['EmptyCartMessage']).text

    assert cart_message == "Your cart is empty", "Empty cart page failed to open or cart has items in it"
