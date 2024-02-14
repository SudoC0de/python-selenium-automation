# Lesson 2 Optional Test Case
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
    search_term: str = "coffee"  # Same product as shown in class

    driver.get("https://www.target.com/")
    driver.find_element(By.ID, "search").send_keys(search_term)
    driver.find_element(By.XPATH, '//button[@data-test="@web/Search/SearchButton"]').click()

    assert search_term in driver.find_element(By.XPATH, '//div[@data-test="resultsHeading"]').text

    driver.quit()


# Wanted to get in the habit of using functions.
main()
