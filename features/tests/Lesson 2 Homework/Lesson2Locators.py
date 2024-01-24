# Lesson 2 Homework
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def main():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    # Copied link from the homework PDF was long so I made it multiline string here
    driver.get("https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid"
               ".return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&"
               "openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fident"
               "ifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&"
               "openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fide"
               "ntifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")

    print(f"Amazon Logo: {driver.find_element(By.XPATH, '//i[@aria-label="Amazon"]')}")
    print(f"Email Input Field: {driver.find_element(By.ID, 'ap_email')}")
    print(f"Continue Button: {driver.find_element(By.ID, 'continue')}")
    print(f"Conditions of Use Link: {driver.find_element(By.XPATH, '//a[text()="Conditions of Use"]')}")
    print(f"Privacy Notice Link: {driver.find_element(By.XPATH, '//a[text()="Privacy Notice"]')}")
    print(f"Need Help Link: {driver.find_element(By.XPATH, '//span[@class="a-expander-prompt"]')}") # I found it weird that this was the only way to return the element as it seemed there was no ID to refer from its attributes or in its parent element

    driver.find_element(By.XPATH, '//i[@class="a-icon a-icon-expand"]').click()

    print(f"Forgot Password Link: {driver.find_element(By.ID, 'auth-fpp-link-bottom')}")
    print(f"Other Issues with Sign-In Link: {driver.find_element(By.ID, 'ap-other-signin-issues-link')}")
    print(f"Create Amazon Account Button: {driver.find_element(By.ID, 'createAccountSubmit')}")

    driver.quit()

# Wanted to get in the habit of using functions.
main()