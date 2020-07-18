from selenium.webdriver.common.by import By
from behave import when, then



CART_PAGE_EMPTY_CART_TEXT_LOCATOR = (By.CSS_SELECTOR, 'div h2')

@when('LF Click On Cart')
def main_page_click_on_cart(context):
    context.app.main_page.header_cart_click()

@then('LF Verify Empty Cart Text Is Present')
def cart_page_verify_empty_text(context):
    context.app.cart_page.verify_empty_cart_text()

