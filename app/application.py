from python_selenium_automation.ultm_pckg.linda_florida.pages.main_page import MainPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.result_page import ResultPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.sign_in_page import SignInPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.cart_page import CartPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.help_page import HelpPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.register_page import RegisterPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.product_page import ProductPage
from python_selenium_automation.ultm_pckg.linda_florida.pages.alerts import Alerts

class Application:
    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.result_page = ResultPage(self.driver)
        self.sign_in_page = SignInPage(self.driver)
        self.register_page = RegisterPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.help_page = HelpPage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.alerts = Alerts(self.driver)