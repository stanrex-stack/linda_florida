from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page

class ProductPage(Page):

    CART_BUTTON_LOCATOR = (By.ID, "add-to-cart-button")
    NEW_ARRIVALS_NAVIGATOR_LOCATOR = (By.CSS_SELECTOR, '#nav-subnav a:nth-of-type(7) span.nav-a-content')
    NEW_ARRIVALS_TOOLTIP_LOCATOR = (By.ID, 'nav-flyout-aj:https://images-na.ssl-images-amazon.com/images/G/01/softlines/megamenu/prod/megamenu-contents_en_US._TTH_.json:subnav-sl-megamenu-8:0')
    SIGN_IN_POP_UP_LOCATOR = (By.CSS_SELECTOR, '.nav-signin-tt.nav-flyout')
