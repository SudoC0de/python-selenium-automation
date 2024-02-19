from typing import List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(self.driver, 10)

    def open(self, url: str):
        self.driver.get(url)

    def find_element(self, locator: tuple[str, str]) -> WebElement:
        return self.driver.find_element(*locator)

    def find_elements(self, locator: tuple[str, str]) -> List[WebElement]:
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_element(self, element: WebElement):
        self.wait.until(EC.element_to_be_clickable(element)).click()

    def alt_click(self, locator: tuple[str, str]):
        # Had to offer this option because otherwise a "selenium.common.exceptions.ElementClickInterceptedException: Message: element click intercepted" would be thrown
        self.wait.until(EC.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].click()", self.find_element(locator))

    def enter_text(self, text: str, locator: tuple[str, str]):
        text_input: WebElement = self.driver.find_element(*locator)
        text_input.clear()
        text_input.send_keys(text)

    def wait_until_located(self, locator: tuple[str, str]):
        self.wait.until(EC.presence_of_element_located(locator))

    def wait_until_visible(self, locator: tuple[str, str]):
        self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_clickable(self, locator: tuple[str, str]):
        self.wait.until(EC.element_to_be_clickable(locator))
