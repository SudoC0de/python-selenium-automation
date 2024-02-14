from behave import when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when('Add Coffee To Cart')
def add_coffee_to_cart(context):
    elements: dict[str, tuple[str, str]] = {
        'SearchResult': (By.CSS_SELECTOR, "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div[data-test='product-details'] > div > div > div:nth-child(1) > div:nth-child(1) > a[data-test='product-title']"),
        'SearchInput': (By.CSS_SELECTOR, "input#search[data-test='@web/Search/SearchInput']"),
        'SearchButton': (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']"),
        'AddToCartButton': (By.CSS_SELECTOR, "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div > button[data-test='chooseOptionsButton']"),
        'SidebarAddToCartButton': (By.CSS_SELECTOR, "button[data-test='orderPickupButton']")
    }

    context.driver.find_element(*elements['SearchInput']).send_keys("coffee")
    context.driver.find_element(*elements['SearchButton']).click()
    context.wait.until(EC.presence_of_element_located(elements['SearchResult']))
    context.wait.until(EC.element_to_be_clickable(elements['AddToCartButton']))
    context.driver.execute_script("arguments[0].click()", context.driver.find_element(*elements['AddToCartButton'])) # Had to do it this way otherwise a "selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted" would be thrown for some reason
    context.wait.until(EC.element_to_be_clickable(elements['SidebarAddToCartButton'])) # "element_to_be_clickable" does not work 100% of the time for some reason
    context.driver.find_element(*elements['SidebarAddToCartButton']).click()

@then('Verify Coffee Added To Cart')
def verify_coffee_added(context):
    elements: dict[str, tuple[str, str]] = {
        'LabelAdded': (By.CSS_SELECTOR, 'div[data-test="content-wrapper"] > div > div > h4'),
        'ViewCartCSS': (By.CSS_SELECTOR, "a[href='/cart']"),
        'CartHeading': (By.CSS_SELECTOR, "#cart-summary-heading"),
        'CartTitle': (By.CSS_SELECTOR, "div[data-test='cartItem-title'] > div")
    }

    context.wait.until(EC.visibility_of_element_located(elements['LabelAdded']))

    label_text: str = context.driver.find_element(*elements['LabelAdded']).text

    context.wait.until(EC.element_to_be_clickable(elements['ViewCartCSS']))
    context.driver.find_element(*elements['ViewCartCSS']).click()
    context.wait.until(EC.visibility_of_element_located(elements['CartHeading']))

    cart_text: str = context.driver.find_element(*elements['CartTitle']).text

    assert label_text in cart_text, f"\"{label_text}\" was not added to the cart. \"{cart_text}\" was added instead."
