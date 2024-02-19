from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


@given('Open Target Homepage')
def open_target_homepage(context):
    context.app.target_homepage.open_target_homepage()


#@when('Enter {search_word} into Target search field')
#def input_search(context, search_word):
    # search: WebElement = context.driver.find_element(By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]')
    # search.clear()
    # search.send_keys(search_word)
    #context.app.target_homepage.enter_text(search_word, (By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]'))


@when('Search for {search_word}')
def homepage_search(context, search_word):
    context.app.target_homepage.execute_search(search_word)
