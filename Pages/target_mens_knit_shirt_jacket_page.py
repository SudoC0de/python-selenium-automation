from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.base_page import Page


class TargetMensKnitShirtJacketPage(Page):
    def open_page(self):
        self.driver.get("https://www.target.com/p/men-s-knit-shirt-jacket-goodfellow-co/-/A-88569969")

    def cycle_colors(self):
        elements: dict[str, tuple[str, str]] = {
            'Colors': (By.CSS_SELECTOR, 'div[data-test="@web/VariationComponent"] div.children img'),
            'ColorText': (By.XPATH, '//div[@data-test="@web/VariationComponent"]//div[contains(text(),"Red Brown")]')
        }

        colors: List[WebElement] = self.find_elements(elements["Colors"])

        for color in colors:
            self.click_element(color)

            image_label: str = color.get_attribute('alt')
            elements['ColorText'] = (
            By.XPATH, f'//div[@data-test="@web/VariationComponent"]//div[contains(text(),"{image_label}")]')

            color_text_element: WebElement = self.find_element(elements["ColorText"])
