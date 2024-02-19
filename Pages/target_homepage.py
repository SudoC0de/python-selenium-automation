from selenium.webdriver.common.by import By
from Pages.base_page import Page


class TargetHomepage(Page):
    def open_target_homepage(self):
        self.open("https://www.target.com/")

    def execute_search(self, search_text: str):
        self.enter_text(search_text, (By.CSS_SELECTOR, 'input[data-test="@web/Search/SearchInput"]'))
        self.click((By.CSS_SELECTOR, 'button[data-test="@web/Search/SearchButton"]'))

    def click_sign_in_icon(self):
        self.click((By.CSS_SELECTOR, "a[data-test='@web/AccountLink']"))

    def click_cart_button(self):
        self.click((By.CSS_SELECTOR, "div[data-test='@web/CartIcon']"))
