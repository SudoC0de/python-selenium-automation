from selenium.webdriver.common.by import By
from Pages.base_page import Page


class TargetHomepageAccountSidebar(Page):
    def click_on_sidebar_sign_in_icon(self):
        self.click((By.CSS_SELECTOR, "a[data-test='accountNav-signIn']"))
