# Lesson 2 Homework
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def main():
    driver_path: str = ChromeDriverManager().install()
    service: Service = Service(driver_path)
    driver: WebDriver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    homepage_signin_button_xpath: str = '//a[@data-test="@web/AccountLink"]//span[text()="Sign in"]'
    sidebar_signin_button_xpath: str = '//a[@data-test="accountNav-signIn"]//span[text()="Sign in"]'
    login_title_text_xpath: str = '//span[text()="Sign into your Target account"]'
    login_signin_button_xpath: str = '//button[@id="login"]'

    driver.get("https://www.target.com/")
    driver.find_element(By.XPATH, homepage_signin_button_xpath).click()
    driver.find_element(By.XPATH, sidebar_signin_button_xpath).click()

    assert driver.find_element(By.XPATH, login_title_text_xpath).text == "Sign into your Target account"

    print(driver.find_element(By.XPATH, login_signin_button_xpath)) # Check for SignIn button
    driver.quit()

# Wanted to get in the habit of using functions.
main()