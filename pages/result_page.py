from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page
from selenium.webdriver.common.by import By

class ResultPage(Page):
    RESULT_PAGE_HEADER_TEXT_LOCATOR = (By.CSS_SELECTOR, 'h1 div span.a-color-state.a-text-bold')
    SEARCH_RESULT_LIST_LOCATOR = (By.CSS_SELECTOR, 'div.s-search-results div.s-result-item h2')
    BESTSELLERS_LOGO_LOCATOR = (By.CSS_SELECTOR, 'span[data-a-badge-color = "sx-orange"]')



    def result_page_static_result_text(self, expected_text):
        self.verify_element_text(expected_text, *self.RESULT_PAGE_HEADER_TEXT_LOCATOR)

    def result_page_element_count(self, expected_number):
        self.wait_for_element_to_appear(*self.SEARCH_RESULT_LIST_LOCATOR)
        self.verify_element_count(expected_number, *self.SEARCH_RESULT_LIST_LOCATOR)




