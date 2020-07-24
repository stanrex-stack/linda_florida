from python_selenium_automation.linda_florida.pages.base_page import Page
from selenium.webdriver.common.by import By

class MainPage(Page):

    # header section
    MAIN_PAGE_SEARCHBAR_LOCATOR = (By.ID, 'twotabsearchtextbox')
    MAIN_PAGE_CLICK_ICON_LOCATOR = (By.CSS_SELECTOR, 'div.nav-search-submit input.nav-input')
    MAIN_PAGE_ORDER_LOCATOR = (By.ID, 'nav-orders')
    MAIN_PAGE_CART_LOCATOR = (By.ID, 'nav-cart')
    MAIN_PAGE_TRY_PRIME_LOCATOR = (By.ID, 'nav-link-prime')
    MAIN_PAGE_ACCOUNT_N_LISTS_LOCATOR = (By.ID, 'nav-link-accountList')
    MAIN_PAGE_NAV_LOGO_LOCATOR = (By.ID, 'nav-logo')
    MAIN_PAGE_LANGUAGE_LOCATOR = (By.ID, 'icp-nav-flyout')
    MAIN_PAGE_HAM_MENU_LOCATOR = (By.ID, 'nav-hamburger-menu')
    MAIN_PAGE_HEADER_SEARCHBAR_SELECT_LOCATOR = (By.ID, 'searchDropdownBox')


    def main_open(self):
        self.open_page()

    def header_search_product(self, text: str):
        self.input(text, *self.MAIN_PAGE_SEARCHBAR_LOCATOR)
        self.click(*self.MAIN_PAGE_CLICK_ICON_LOCATOR)

    def header_orders_click(self):
        self.click(*self.MAIN_PAGE_ORDER_LOCATOR)

    def header_cart_click(self):
        self.click(*self.MAIN_PAGE_CART_LOCATOR)

    def header_prime_click(self):
        self.click(*self.MAIN_PAGE_TRY_PRIME_LOCATOR)

    def header_account_click(self):
        self.click(*self.MAIN_PAGE_ACCOUNT_N_LISTS_LOCATOR)

    def header_amazon_logo_click(self):
        self.click(*self.MAIN_PAGE_NAV_LOGO_LOCATOR)

    def header_language_selector_click(self):
        self.click(*self.MAIN_PAGE_LANGUAGE_LOCATOR)


    def header_hamburger_menu_click(self):
        self.click(*self.MAIN_PAGE_HAM_MENU_LOCATOR)