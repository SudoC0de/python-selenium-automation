from behave import then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@then('Target results for {product_search} are shown')
def verify_target_results(context, product_search):
    assert product_search in context.app.target_search_results_page.get_search_results_heading()
