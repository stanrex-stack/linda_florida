from selenium.webdriver.common.by import By
from behave import when, then

#  TEXT ASSERTION BUNDLE


CREATE_ACCOUNT_HEADER_TEXT_LOCATOR = (By.CSS_SELECTOR, 'h1.a-spacing-small')
@then('LF REGISTER Verify Header Text Is {create_account}')
def register_header_assertion(context, create_account):
    context.app.main_page.verify_element_text(create_account, *CREATE_ACCOUNT_HEADER_TEXT_LOCATOR)


NAME_FIELD_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'label[for="aps_customer_name"]')
@then('LF REGISTER Verify Name Field Text Is {your_name}')
def register_name_field_text(context, your_name):
    context.app.main_page.verify_element_text(your_name, *NAME_FIELD_DESCRIPTION_TEXT)


EMAIL_FIELD_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'label[for="ap_email"]')
@then('LF REGISTER Verify Email Field Text Is {email}')
def register_email_field_text(context, email):
    context.app.main_page.verify_element_text(email, *EMAIL_FIELD_DESCRIPTION_TEXT)


PASSWORD_FIELD_DESCRIPTION_TEXT = (By.CSS_SELECTOR, 'label[for="ap_password"]')
@then('LF REGISTER Verify Password Field Text Is {password_text}')
def register_password_field_text(context, password_text):
    context.app.main_page.verify_element_text(password_text, *PASSWORD_FIELD_DESCRIPTION_TEXT)


INPUT_FIELD_FOR_PASSWORD_LOCATOR = (By.ID, 'ap_password')
@then('LF REGISTER Verify Password Input Field Text Is {password_disclaimer}')
def register_password_input_field_text(context, password_disclaimer):
    attrribute_value = context.app.main_page.get_attribute_value('placeholder', *INPUT_FIELD_FOR_PASSWORD_LOCATOR)
    assert password_disclaimer in attrribute_value


PASSWORD_FIELD_DISCLAIMER_ICON_LOCATOR = (By.CSS_SELECTOR, 'div.a-alert-container i')
@then('LF REGISTER Verify Password Disclaimer Icon Is Present')
def register_password_input_icon(context):
    context.app.main_page.wait_for_element_to_be_located(*PASSWORD_FIELD_DISCLAIMER_ICON_LOCATOR)

PASSWORD_FIELD_DISCLAIMER_TEXT_LOCATOR = (By.CSS_SELECTOR, 'div.a-alert-container div.a-alert-content') #TODO Bad Locator
@then('LF REGISTER Verify Password Disclaimer Text Is {password_disclaimer}')
def register_password_disclaimer_text(context, password_disclaimer):
    context.app.main_page.verify_element_text(password_disclaimer, *PASSWORD_FIELD_DISCLAIMER_TEXT_LOCATOR)


REENTER_PASSWORD_FIELD_TEXT_LOCATOR = (By.CSS_SELECTOR, 'label[for="ap_password_check"]')
@then('LF REGISTER Verify Re-Enter Password Text Is {re_enter}')
def register_reenter_text(context, re_enter):
    context.app.main_page.verify_element_text(re_enter, *REENTER_PASSWORD_FIELD_TEXT_LOCATOR)


CREATE_AMAZON_BUTTON_TEXT_LOCATOR = (By.ID, 'a-autoid-0-announce')
@then('LF REGISTER Verify That Create Your Amazon Account Button Text Is {button_text}')
def register_create_button_text(context, button_text):
    context.app.main_page.verify_element_text(button_text, *CREATE_AMAZON_BUTTON_TEXT_LOCATOR)


DIVIDER_TEXT_LOCATOR = (By.XPATH, "//div[@class = 'a-row' and contains(text(), 'Already have an account?')]")
# TODO Find a good Locator
@then('LF REGISTER Verify Divider Text Is {divider_text}')
def divider(context, divider_text):
    context.app.main_page.verify_element_text(divider_text, *DIVIDER_TEXT_LOCATOR)


# INPUT BUNDLE

NAME_INPUT_FIELD_LOCATOR = (By.ID, 'ap_customer_name')
@then('LF REGISTER Input Name {name_string}')
def register_new_name(context, name_string):
    context.app.main_page.input(name_string, *NAME_INPUT_FIELD_LOCATOR)


EMAIL_INPUT_FIELD_LOCATOR = (By.ID, 'ap_email')
@then('LF REGISTER Input Email {email_string}')
def register_new_email(context, email_string):
    context.app.main_page.input(email_string, *EMAIL_INPUT_FIELD_LOCATOR)


PASSWORD_INPUT_FIELD_LOCATOR = (By.ID, 'ap_password')
@then('LF REGISTER Input Password {password_string}')
def register_new_email(context, password_string):
    context.app.main_page.input(password_string, *PASSWORD_INPUT_FIELD_LOCATOR)


REENTER_PASSWORD_INPUT_FIELD_LOCATOR = (By.ID, 'ap_password_check')
@then('LF REGISTER Input Reenter Password {password_string}')
def register_new_email(context, password_string):
    context.app.main_page.input(password_string, *REENTER_PASSWORD_INPUT_FIELD_LOCATOR)


CREATE_AMAZON_BUTTON_LOCATOR = (By.ID, 'continue')
@then('LF REGISTER Click On Create Amazon Account')
def click_on_create_amazon(context):
    context.app.main_page.click(*CREATE_AMAZON_BUTTON_LOCATOR)


SIGN_IN_DROPDOWN_LOCATOR = (By.CSS_SELECTOR, 'a.a-link-emphasis')
@then('LF REGISTER Click On Sing In Drop Down')
def click_on_signin(context):
    context.app.main_page.click(*SIGN_IN_DROPDOWN_LOCATOR)

