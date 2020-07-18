from selenium.webdriver.common.by import By
from behave import when, then
from time import sleep

HAMBURGER_MENU_MUSIC_LIST_LOCATOR = (By.XPATH, '//ul/li/a/div[contains(text(), "Amazon Music")]')
HAMBURGER_MENU_MUSIC_LIST_ITEMS_LOCATOR = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")



@when('LF Click On Hamburger Menu')
def main_page_click_on_hamburger_menu(context):
    context.app.main_page.header_hamburger_menu_click()


@when('LF Click On Amazon Music Menu Item')
def hamburger_menu_click_on_music_list(context):
    context.app.main_page.wait_for_element_to_be_clickable(*HAMBURGER_MENU_MUSIC_LIST_LOCATOR)

@then('LF {items_count} Menu Items Are Present')
def ham_menu_music_list_count_items(context, items_count):
    items_count = int(items_count)
    context.driver.wait.until(correct_menu_items_present(HAMBURGER_MENU_MUSIC_LIST_ITEMS_LOCATOR, items_count),
                              "Amount of items is incorrect")
    # use a custom made Explicit Wait
    actual = len(context.driver.find_elements(*HAMBURGER_MENU_MUSIC_LIST_ITEMS_LOCATOR))

    assert items_count == actual, f'Expected {items_count} items, but got {actual} items'

# the custom made explicit wait here
class correct_menu_items_present(object):
    def __init__(self, locator, amount):
        self.locator = locator
        self.amount = amount


    def __call__(self, driver):
        elements = driver.find_elements(*self.locator)
        if len(elements) == self.amount:
            return elements
        else:
            return False

