# Lesson 2 Homework
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

def main():
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)
    homepage_signin_button_xpath = '//a[@data-test="@web/AccountLink"]//span[text()="Sign in"]'
    sidebar_signin_button_xpath = '//a[@data-test="accountNav-signIn"]//span[text()="Sign in"]'
    login_title_text_xpath = '//span[text()="Sign into your Target account"]'
    login_signin_button_xpath = '//button[@id="login"]'

    driver.get("https://www.target.com/")
    driver.find_element(By.XPATH, homepage_signin_button_xpath).click()
    sleep(3) # Wait for sidebar to appear
    driver.find_element(By.XPATH, sidebar_signin_button_xpath).click()
    sleep(3)

    assert driver.find_element(By.XPATH, login_title_text_xpath).text == "Sign into your Target account"
    print(driver.find_element(By.XPATH, login_signin_button_xpath)) # Check for SignIn button

    driver.quit()

# Wanted to get in the habit of using functions.
main()