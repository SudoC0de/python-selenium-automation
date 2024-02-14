from time import sleep
from typing import List
from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@then('Verify All Results Have Title And Image')
def verify_all_results_have_title_and_image(context):
    elements: dict[str, tuple[str, str]] = {
        'ProductTitles': (By.CSS_SELECTOR, 'div[data-component-title="Product Grid"] a[data-test="product-title"]'),
        'ProductImages': (By.CSS_SELECTOR, 'div[data-component-title="Product Grid"] h3[data-test="@web/ProductCard/ProductCardImage"]'),
        'PageSelectButton': (By.CSS_SELECTOR, 'button[data-test="select"]')
    }

    sleep(3) # if this is not included, the whole page loads without loading search results
    product_title_elements: List[WebElement] = context.driver.find_elements(*elements['ProductTitles'])
    product_image_elements: List[WebElement] = context.driver.find_elements(*elements['ProductImages'])

    assert len(product_title_elements) == len(product_image_elements)
