from selenium.webdriver.chrome.webdriver import WebDriver
from Pages.base_page import Page
from Pages.target_cart_page import TargetCartPage
from Pages.target_cart_sidebar import TargetCartSidebar
from Pages.target_circle_page import TargetCirclePage
from Pages.target_help_page import TargetHelpPage
from Pages.target_homepage import TargetHomepage
from Pages.target_homepage_account_sidebar import TargetHomepageAccountSidebar
from Pages.target_mens_knit_shirt_jacket_page import TargetMensKnitShirtJacketPage
from Pages.target_search_results_page import TargetSearchResultsPage
from Pages.target_signin_page import TargetSigninPage

class Application:
    def __init__(self, driver: WebDriver):
        self.pages: Page = Page(driver)
        self.target_cart_page: TargetCartPage = TargetCartPage(driver)
        self.target_cart_sidebar: TargetCartSidebar = TargetCartSidebar(driver)
        self.target_circle_page: TargetCirclePage = TargetCirclePage(driver)
        self.target_help_page: TargetHelpPage = TargetHelpPage(driver)
        self.target_homepage: TargetHomepage = TargetHomepage(driver)
        self.target_homepage_account_sidebar: TargetHomepageAccountSidebar = TargetHomepageAccountSidebar(driver)
        self.target_mens_knit_shirt_jacket_page: TargetMensKnitShirtJacketPage = TargetMensKnitShirtJacketPage(driver)
        self.target_search_results_page: TargetSearchResultsPage = TargetSearchResultsPage(driver)
        self.target_signin_page: TargetSigninPage = TargetSigninPage(driver)
