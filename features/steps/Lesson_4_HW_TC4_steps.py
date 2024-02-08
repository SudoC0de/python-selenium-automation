from time import sleep
from typing import List
from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.remote.webelement import WebElement


@given('Open Target Help Page')
def open_target_circle_page(context):
    context.driver.get("https://help.target.com/help")
    sleep(3)  # Needed this as the page loads so fast that the ToDo container would not fully load all its elements
    # before going to the next step


@then('Verify Target Help UI Elements')
def verify_target_help_page(context):
    help_title: WebElement = context.driver.find_element(By.CSS_SELECTOR, 'form > section > div > div > div > h2')
    search_input_box: WebElement = context.driver.find_element(By.CSS_SELECTOR, '.search-input')
    search_button: WebElement = context.driver.find_element(By.CSS_SELECTOR, '.search-btn')
    todo_container: List[WebElement] = context.driver.find_elements(By.XPATH,
                                                                    '//div[contains(text(),"track") or contains(text('
                                                                    '),"view") or contains(text(),"pickup") or '
                                                                    'contains(text(),"returns") or contains(text(),'
                                                                    '"check GiftCard") or contains(text(),"fix")]')
    manage_container: List[WebElement] = context.driver.find_elements(By.XPATH, '//h3[text()="manage my"]')
    todo_container_length:int = len(todo_container)
    manage_container_length:int = len(manage_container)

    assert todo_container_length == 6 and manage_container_length == 1, f"Expected 6 ToDo items, got {todo_container_length} and 1 Manage items, got {manage_container_length}"

    contact_recall_container: List[WebElement] = context.driver.find_elements(By.XPATH,
                                                                              '//h3[text()="contact us" or text('
                                                                              ')="product recalls"]')
    contact_recall_container_length:int = len(contact_recall_container)

    assert contact_recall_container_length == 2, f"Expected 2 Contact Recall items, got {contact_recall_container_length}"

    browse_all_help_pages_title: WebElement = context.driver.find_element(By.XPATH,
                                                                          '//h2[text()="Browse all Help pages"]')
