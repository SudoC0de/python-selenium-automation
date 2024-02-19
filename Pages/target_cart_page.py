from selenium.webdriver.common.by import By
from Pages.base_page import Page


class TargetCartPage(Page):
    def get_cart_empty_message(self) -> str:
        elements: dict[str, tuple[str, str]] = {
            'EmptyCartHTMLContainer': (By.CSS_SELECTOR, "div[data-test='emptyCartContainer']"),
            'EmptyCartMessage': (
            By.CSS_SELECTOR, "div[data-test='emptyCartContainer'] > div[data-test='boxEmptyMsg'] > h1")
        }

        self.wait_until_visible(elements['EmptyCartHTMLContainer'])

        return self.find_element(elements['EmptyCartMessage']).text

    def get_cart_title_text(self) -> str:
        self.wait_until_visible((By.CSS_SELECTOR, "#cart-summary-heading"))

        return self.find_element((By.CSS_SELECTOR, "div[data-test='cartItem-title'] > div")).text
