from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

@when('Click on Cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='@web/CartIcon']").click()

@then('Cart Empty Message Shown')
def verify_cart_empty_message(context):
    count: int = 0

    while (len(context.driver.find_elements(By.CSS_SELECTOR, "div[data-test='emptyCartContainer']")) == 0 and
           count < 60):
        count += 1
        sleep(1)

    cart_message: str = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='emptyCartContainer'] > div[data-test='boxEmptyMsg'] > h1").text

    assert cart_message == "Your cart is empty", "Empty cart page failed to open or cart has items in it"
