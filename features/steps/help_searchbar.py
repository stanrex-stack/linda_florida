from selenium.webdriver.common.by import By
from behave import given, when, then

@when('LF Open {link_string}')
def open_amazon_linked_page(context, link_string):
    context.app.main_page.open_page(link_string)

@when('LF Help Search For {search_text}')
def help_search_for_text(context, search_text):
    context.app.help_page.search_product(search_text)

@then('LF Help Verify {search_text} Has Been Found')
def help_verify_text(context, search_text):
    context.app.help_page.verify_search_text(search_text)