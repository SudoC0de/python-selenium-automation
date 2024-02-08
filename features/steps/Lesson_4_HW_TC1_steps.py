from selenium.webdriver.common.by import By
from behave import then
from time import sleep


@then('Target results for {product_search} are shown')
def verify_target_results(context, product_search):
    count: int = 0
    count_limit: int = 5

    while (len(context.driver.find_elements(By.CSS_SELECTOR, 'div[data-test="resultsHeading"]')) == 0 and
           count < count_limit):
        count += 1
        sleep(1)

    search_heading_text: str = context.driver.find_element(By.CSS_SELECTOR, 'div[data-test="resultsHeading"] > span').text

    assert product_search in search_heading_text
