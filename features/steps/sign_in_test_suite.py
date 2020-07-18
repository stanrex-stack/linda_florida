from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


ORDERS = (By.ID, "nav-orders")
NEED_HELP = (By.CSS_SELECTOR, ".a-expander-prompt")
SIGN_IN_HEADER = (By.CSS_SELECTOR, "h1")



@when("Click Amazon Orders")
def click_orders_link(context):
    context.app.main_page.wait_for_element_click(*ORDERS)


@then("Verify {page_name} page is opened")
def verify_page_opened(context, page_name):
    context.app.sign_in_page.verify_text(page_name, *SIGN_IN_HEADER)


@when("Open Sign-In page")
def open_sign_in(context):
    context.app.main_page.open_page("ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=usflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&switch_account=)")


@then("Verify {field} Text is {field_text}")
def verify_field_text(context, field, field_text):
    context.app.sign_in_page.verify_field_text(field, field_text)


@when("Click To Assert Need Help Texts")
def click_need_help(context):
    context.app.sign_in_page.wait_for_element_click(*context.app.sign_in_page.NEED_HELP)


@then("Verify {item} Is Clickable")
def verify_clickability(context, item):
    context.app.sign_in_page.verify_item_is_clickable(item)


@then("Verify {dropdown_name} Drop Down Is Functioning: {item1} and {item2} appear and disappear")
def verify_need_help_dropdown(context, dropdown_name, item1, item2):
    context.app.sign_in_page.wait_for_element_click(*context.app.sign_in_page.NEED_HELP)
    context.app.sign_in_page.verify_dropdown_appears(item1, item2)
    context.app.sign_in_page.wait_for_element_click(*context.app.sign_in_page.NEED_HELP)
    context.app.sign_in_page.verify_dropdown_disappears(item1, item2)


@then("Verify {alert} Alert Is Present")
def veirfy_alert(context, alert):
    context.app.sign_in_page.verify_alert(alert)