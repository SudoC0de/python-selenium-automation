# 01/20/2024 Lesson 2 Lesson-Practice
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def main():
    driver: webdriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    destination_website: str = "https://www.amazon.com/"
    web_elements = {}

    driver.get(destination_website)
    web_elements.update({
        "Department Select Dropdown": driver.find_element(By.CSS_SELECTOR, '#searchDropdownBox.nav-search-dropdown')
    })
    web_elements["Department Select Dropdown"].click()

    driver.quit()

main()
