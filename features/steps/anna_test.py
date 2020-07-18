# from selenium.webdriver.common.by import By
# from behave import when, then
#
# CREATE_ACCOUNT_HEADER_TEXT_LOCATOR = (By.CSS_SELECTOR, 'h1.a-spacing-small')
# NAME_FIELD_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'label[for="ap_customer_name"]')
#
# @then('LF Verify {field_name} is {name_var}')
# def function(context, field_name, name_var):
#     if field_name in 'Create account':
#         context.app.register_page.verify_element_text(name_var, *CREATE_ACCOUNT_HEADER_TEXT_LOCATOR)
#     elif field_name == 'Your name':
#         context.app.register_page.verify_element_text(name_var, *NAME_FIELD_DESCRIPTION_TEXT)