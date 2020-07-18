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

    def verify_bestsellers_are_present(self):
        list = self.driver.find_elements(*self.BESTSELLERS_LOGO_LOCATOR)
        if len(list) > 0:
            return True
        else:
            return False

    def open_bestsellers_in_another_window(self):
       a =  self.driver.find_elements(*self.SEARCH_RESULT_LIST_LOCATOR)
       for index in range(len(a)):
           b = a[index].find_elements(*self.BESTSELLERS_LOGO_LOCATOR)
           print(b)


