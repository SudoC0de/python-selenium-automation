from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

@when('Click on Sign In icon')
def click_on_sign_in_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()

@then('Click on sidebar Sign In Icon')
def click_on_sidebar_sign_in_icon(context):
    count: int = 0

    while (len(context.driver.find_elements(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']")) == 0 and
           count < 60):
        count += 1
        sleep(1)

    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()

@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    count: int = 0

    while (len(context.driver.find_elements(By.CSS_SELECTOR, "button#login")) == 0 and
           count < 60):
        count += 1
        sleep(1)

    assert context.driver.find_element(By.CSS_SELECTOR, "button#login").is_displayed() == True, "Sign In form failed to open"