from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.base_page import Page


class TargetCirclePage(Page):
    def open_circle_page(self):
        self.open("https://www.target.com/circle")

    def get_benefit_box_elements(self) -> List[WebElement]:
        return self.find_elements((By.CSS_SELECTOR, 'div > section > ul > li'))
