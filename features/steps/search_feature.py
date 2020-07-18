from selenium.webdriver.common.by import By
from behave import given, when, then

@given('LF Open Amazon Main Page')
def get_amazon_main_page(context):
    context.app.main_page.main_open()
#     TODO Imperfect link. Had to create a
#      When for Open Page in help searchbar
#      and mess up main and base page

@when('LF Search for {search_word}')
def amazon_main_page_search(context, search_word):
    context.app.main_page.header_search_product(search_word)

@then('LF Search result for {expected_text} is shown in header')
def amazon_result_page_header_verifier(context, expected_text):
    context.app.result_page.result_page_static_result_text(expected_text)

@when('LF Select {search_word} In Select Menu')
def select_text_in_select_menu(context, search_word):
   context.app.main_page.select_by_name(search_word, *context.app.main_page.MAIN_PAGE_HEADER_SEARCHBAR_SELECT_LOCATOR)

