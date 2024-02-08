from typing import List
from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.remote.webelement import WebElement


@given('Open Target Circle Page')
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")


@then('Verify 5 Benefit Boxes Shown')
def verify_5_benefit_boxes_shown(context):
    benefits_container: List[WebElement] = context.driver.find_elements(By.CSS_SELECTOR, 'div > section > ul > li')

    assert len(benefits_container) == 5, f"Expected 5 benefits but got {len(benefits_container)}"
