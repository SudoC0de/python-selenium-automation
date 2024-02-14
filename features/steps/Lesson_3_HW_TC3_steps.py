from selenium.webdriver.common.by import By
from behave import when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click on Sign In icon')
def click_on_sign_in_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()


@then('Click on sidebar Sign In Icon')
def click_on_sidebar_sign_in_icon(context):
    context.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")))
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    assert context.wait.until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, "button#login")
    )), "Sign In form failed to open"
