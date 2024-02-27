import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import Page


class TargetSigninPage(Page):
    def wait_until_signin_button_visible(self) -> WebElement:
        signin_button: tuple[str, str] = (By.CSS_SELECTOR, "button#login")

        self.wait_until_visible(signin_button)

        return self.find_element(signin_button)

    def sign_in(self):
        username_input: tuple[str, str] = (By.ID, 'username')

        self.wait_until_visible(username_input)
        self.enter_text('****', username_input)
        self.enter_text('****', (By.ID, 'password'))
        self.click((By.ID, 'login'))
        self.wait_until_invisible((By.ID, 'login'))

    def invalid_sign_in(self):
        # Could make this more dynamic for credentials but this is quicker
        username_input: tuple[str, str] = (By.ID, 'username')
        letters: str = string.ascii_letters + string.digits

        self.wait_until_visible(username_input)
        self.enter_text(str(''.join(random.choices(letters, k=8))) + '@gmail.com', username_input)
        self.enter_text(str(''.join(random.choices(letters, k=8))), (By.ID, 'password'))
        self.click((By.ID, 'login'))

    def verify_signin_error_message_shown(self):
        message_from_element: tuple[str, str] = (By.CSS_SELECTOR, 'div[data-test="authAlertDisplay"] > div')
        error_message: str = 'We can\'t find your account.'

        self.wait_until_located(message_from_element)
        assert self.find_element(message_from_element).text == error_message, \
            f'Expected Sign In Error: \"{error_message}\", Received: \"{message_from_element}\"'

    def switch_to_terms_and_conditions(self):
        terms_and_conditions_link: tuple[str, str] = (By.CSS_SELECTOR, 'a[aria-label*="terms & conditions"]')

        self.wait_until_clickable(terms_and_conditions_link)

        signin_window: str = self.driver.current_window_handle

        self.click(terms_and_conditions_link)
        self.wait_until_new_window_opened(2)
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.wait_until_visible((By.CSS_SELECTOR, 'h1[data-test="page-title"]'))
        self.close_window()
        self.driver.switch_to.window(signin_window)
        self.wait_until_signin_button_visible()
