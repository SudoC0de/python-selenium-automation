from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@given('Open Target Homepage')
def open_target_homepage(context):
    context.driver.get("https://www.target.com/")


@when('Enter {search_word} into Target search field')
def input_search(context, search_word):
    search: WebElement = context.driver.find_element(By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]')
    search.clear()
    search.send_keys(search_word)


@when('Click on Target search icon')
def click_target_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'button[data-test="@web/Search/SearchButton"]').click()
