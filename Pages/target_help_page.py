from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from Pages.base_page import Page


class TargetHelpPage(Page):
    def open_help_page(self):
        self.open("https://help.target.com/help")

    def get_help_title_element(self) -> WebElement:
        return self.find_element((By.CSS_SELECTOR, 'form > section > div > div > div > h2'))

    def get_search_box_element(self) -> WebElement:
        return self.find_element((By.CSS_SELECTOR, '.search-input'))

    def get_search_button_element(self) -> WebElement:
        return self.find_element((By.CSS_SELECTOR, '.search-btn'))

    def get_todo_container_length(self) -> int:
        todo_container: List[WebElement] = self.find_elements((By.XPATH,
                                                               '//div[contains(text(),"track") or contains(text('
                                                               '),"view") or contains(text(),"pickup") or '
                                                               'contains(text(),"returns") or contains(text(),'
                                                               '"check GiftCard") or contains(text(),"fix")]'))

        return len(todo_container)

    def get_manage_container_length(self) -> int:
        return len(self.find_elements((By.XPATH, '//h3[text()="manage my"]')))

    def get_contact_recall_container_length(self) -> int:
        contact_recall_container: List[WebElement] = self.find_elements((By.XPATH,
                                                                         '//h3[text()="contact us" or text('
                                                                         ')="product recalls"]'))

        return len(contact_recall_container)

    def get_browse_all_title_element(self) -> WebElement:
        return self.find_element((By.XPATH, '//h2[text()="Browse all Help pages"]'))
