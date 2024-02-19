from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.base_page import Page


class TargetSigninPage(Page):
    def wait_until_signin_button_visible(self) -> WebElement:
        signin_button: tuple[str, str] = (By.CSS_SELECTOR, "button#login")

        self.wait_until_visible(signin_button)

        return self.find_element(signin_button)
