from time import sleep
from typing import List
from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.remote.webelement import WebElement


@given('Open Target Help Page')
def open_target_help_page(context):
    context.app.target_help_page.open_help_page()
    sleep(3)  # Needed this as the page loads so fast that the ToDo container would not fully load all its elements
    # before going to the next step


@then('Verify Target Help UI Elements')
def verify_target_help_page(context):
    help_title: WebElement = context.app.target_help_page.get_help_title_element()
    search_input_box: WebElement = context.app.target_help_page.get_search_box_element()
    search_button: WebElement = context.app.target_help_page.get_search_button_element()
    todo_container_length: int = context.app.target_help_page.get_todo_container_length()
    manage_container_length: int = context.app.target_help_page.get_manage_container_length()

    assert todo_container_length == 6 and manage_container_length == 1, f"Expected 6 ToDo items, got {todo_container_length} and 1 Manage items, got {manage_container_length}"

    contact_recall_container_length: int = context.app.target_help_page.get_contact_recall_container_length()

    assert contact_recall_container_length == 2, f"Expected 2 Contact Recall items, got {contact_recall_container_length}"

    browse_all_help_pages_title: WebElement = context.app.target_help_page.get_browse_all_title_element()
