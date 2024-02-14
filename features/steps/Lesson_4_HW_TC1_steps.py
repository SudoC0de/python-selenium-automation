from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@then('Target results for {product_search} are shown')
def verify_target_results(context, product_search):
    search_heading_element: tuple[str, str] = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"] > span')

    context.wait.until(EC.presence_of_element_located(search_heading_element))

    search_heading_text: str = context.driver.find_element(*search_heading_element).text

    assert product_search in search_heading_text
