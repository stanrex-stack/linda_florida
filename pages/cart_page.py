from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    CART_PAGE_EMPTY_CART_TEXT_LOCATOR = (By.CSS_SELECTOR, 'div h2')
    EXPECTED_EMPTY_CART_TEXT = 'Your Amazon Cart is empty'

    def verify_empty_cart_text(self):
        self.wait_for_element_to_be_located(*self.CART_PAGE_EMPTY_CART_TEXT_LOCATOR)
        self.verify_element_text(self.EXPECTED_EMPTY_CART_TEXT, *self.CART_PAGE_EMPTY_CART_TEXT_LOCATOR)