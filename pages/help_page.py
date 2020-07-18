from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page
from selenium.webdriver.common.by import By

class HelpPage(Page):

    SEARCHBAR_LOCATOR = (By.ID, 'helpsearch')
    SEARCHBAR_SEARCH_ICON_LOCATOR = (By.ID, 'helpSearchSubmit')
    SEARCH_RESULT_HEADER_WORD_TEXT_LOCATOR = (By.CSS_SELECTOR, 'p b')


    def search_product(self, text: str):
        self.input(text, *self.SEARCHBAR_LOCATOR)
        self.wait_for_element_to_be_clickable(*self.SEARCHBAR_SEARCH_ICON_LOCATOR)

    def verify_search_text(self, expected_text):
        self.wait_for_element_to_be_located(*self.SEARCH_RESULT_HEADER_WORD_TEXT_LOCATOR)
        self.verify_element_text(expected_text, *self.SEARCH_RESULT_HEADER_WORD_TEXT_LOCATOR)
