from selenium.webdriver.common.by import By
from behave import when, then


SEARCH_RESULT_LIST_LOCATOR = (By.CSS_SELECTOR, 'div.s-search-results div.s-result-item h2')
@then('LF RESULT Verify Amount Of Results Is {number}')
def verify_item_numbers_in_result(context, number):
    context.app.result_page.result_page_element_count(number)

@then('LF RESULT Verify Bestsellers Are Present')
def asert_bestsellers_are_present(context):
    assert context.app.result_page.verify_bestsellers_are_present() == True, f'Bestsellers Are Not Present'

@when('LF RESULT Add Each Besteseller To Cart')
def bestsellers_purchase(context):
    context.app.result_page.open_bestsellers_in_another_window()