from selenium.webdriver.common.by import By
from Pages.base_page import Page


class TargetSearchResultsPage(Page):
    def get_search_results_heading(self) -> str:
        search_heading_element: tuple[str, str] = (By.CSS_SELECTOR, 'div[data-test="resultsHeading"] > span')

        self.wait_until_located(search_heading_element)

        return self.find_element(search_heading_element).text

    def verify_first_result_present(self):
        self.wait_until_located((By.CSS_SELECTOR, "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div[data-test='product-details'] > div > div > div:nth-child(1) > div:nth-child(1) > a[data-test='product-title']"))

    def add_to_cart_first_result(self):
        add_to_cart_button: tuple[str, str] = (By.CSS_SELECTOR, "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(2) > div > div > button[data-test='chooseOptionsButton']")

        self.wait_until_located((By.CSS_SELECTOR,
                                 "div[data-component-title='Product Grid'] > div > div > section > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(2) > div[data-test='product-details'] > div > div > div:nth-child(1) > div:nth-child(1) > a[data-test='product-title']"))
        self.alt_click(add_to_cart_button)

    def get_product_title_elements_length(self) -> int:
        return len(self.find_elements(
            (By.CSS_SELECTOR,
             'div[data-component-title="Product Grid"] a[data-test="product-title"]')))

    def get_product_image_elements_length(self) -> int:
        return len(self.find_elements(
            (By.CSS_SELECTOR,
             'div[data-component-title="Product Grid"] h3[data-test="@web/ProductCard/ProductCardImage"]')))
