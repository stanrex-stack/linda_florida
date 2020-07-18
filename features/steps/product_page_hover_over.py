from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
#
# SIGN_IN_POP_UP_LOCATOR = (By.CSS_SELECTOR, '.nav-signin-tt.nav-flyout')
# NEW_ARRIVALS_NAVIGATOR_LOCATOR = (By.CSS_SELECTOR, '#nav-subnav a:nth-of-type(7) span.nav-a-content')
@when('LF Hover Over New Arrivals')
def hover_over_cart(context):
    context.app.product_page.wait_for_element_to_dissappear(*context.app.product_page.SIGN_IN_POP_UP_LOCATOR)
    context.app.product_page.hover_over_element(*context.app.product_page.NEW_ARRIVALS_NAVIGATOR_LOCATOR)

@then('LF Verify That A Tooltip Appears')
def verify_tooltip(context):
    context.app.product_page.wait_for_element_to_appear(*context.app.product_page.NEW_ARRIVALS_TOOLTIP_LOCATOR)


