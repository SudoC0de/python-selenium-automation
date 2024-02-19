from selenium.webdriver.common.by import By
from Pages.base_page import Page


class TargetCartSidebar(Page):
    __shared_elements: dict[str, tuple[str, str]] = {
        'LabelAdded': (By.CSS_SELECTOR, 'div[data-test="content-wrapper"] > div > div > h4'),
    }

    def click_add_to_cart_button(self):
        self.click((By.CSS_SELECTOR, "button[data-test='orderPickupButton']"))

    def get_cart_label_text(self) -> str:
        self.wait_until_visible(self.__shared_elements['LabelAdded'])

        return self.find_element(self.__shared_elements['LabelAdded']).text

    def view_cart_after_add(self):
        self.wait_until_visible(self.__shared_elements['LabelAdded'])
        self.click((By.CSS_SELECTOR, "a[href='/cart']"))
