from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep
from selenium.webdriver.remote.webelement import WebElement

product_info = {
    "Label Added CSS": "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div[data-test='product-details'] > div > div > div:nth-child(1) > div:nth-child(1) > a[data-test='product-title']",
    "Label Text" : ""
}

@when('Add Coffee To Cart')
def add_coffee_to_cart(context):
    search_input_css: str = "input#search[data-test='@web/Search/SearchInput']"
    context.driver.find_element(By.CSS_SELECTOR, search_input_css).send_keys("coffee")
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']").click()

    count: int = 0
    count_limit: int = 5

    while (len(context.driver.find_elements(By.CSS_SELECTOR,product_info["Label Added CSS"])) == 0 and
           count < count_limit):
        count += 1
        sleep(1)


    product_info["Label Text"] = context.driver.find_element(By.CSS_SELECTOR, product_info["Label Added CSS"]).text
    add_to_cart_css: str = "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div > button[data-test='chooseOptionsButton']"
    add_button: WebElement = context.driver.find_element(By.CSS_SELECTOR, add_to_cart_css)
    context.driver.execute_script("arguments[0].click()", add_button) # Had to do it this way otherwise a "selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted" would be thrown for some reason

    sidebar_add_to_cart_css: str = "button[data-test='shippingButton']"
    count = 0

    while (len(context.driver.find_elements(By.CSS_SELECTOR, sidebar_add_to_cart_css)) == 0 and
           count < count_limit):
        count += 1
        sleep(1)

    context.driver.find_element(By.CSS_SELECTOR, sidebar_add_to_cart_css).click()

@then('Verify Coffee Added To Cart')
def verify_coffee_added(context):
    view_cart_css = "a[href='/cart']"
    count: int = 0
    count_limit: int = 5

    while (len(context.driver.find_elements(By.CSS_SELECTOR, view_cart_css)) == 0 and
           count < count_limit):
        count += 1
        sleep(1)

    context.driver.find_element(By.CSS_SELECTOR, view_cart_css).click()
    count = 0

    while (len(context.driver.find_elements(By.CSS_SELECTOR, "#cart-summary-heading")) == 0 and
           count < count_limit):
        count += 1
        sleep(1)

    assert product_info["Label Text"] in context.driver.find_element(By.CSS_SELECTOR, "div[data-test='cartItem-title'] > div").text, f"{product_info["Label Text"]} was not added to the cart"
