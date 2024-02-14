from typing import List
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


@given('Open Men\'s Knit Shirt Jacket Page')
def open_knitshirt_jacket_page(context):
    context.driver.get("https://www.target.com/p/men-s-knit-shirt-jacket-goodfellow-co/-/A-88569969")

@then('Verify Cycling Colors')
def verify_cycling_colors(context):
    elements: dict[str, tuple[str,str]] = {
        'Colors': (By.CSS_SELECTOR, 'div[data-test="@web/VariationComponent"] div.children img'),
        'ColorText': (By.XPATH, '//div[@data-test="@web/VariationComponent"]//div[contains(text(),"Red Brown")]')
    }

    colors: List[WebElement] = context.driver.find_elements(*elements["Colors"])

    for color in colors:
        context.wait.until(EC.element_to_be_clickable(color))
        color.click()

        image_label: str = color.get_attribute('alt')
        elements['ColorText'] = (By.XPATH, f'//div[@data-test="@web/VariationComponent"]//div[contains(text(),"{image_label}")]')

        assert context.driver.find_element(*elements["ColorText"])
