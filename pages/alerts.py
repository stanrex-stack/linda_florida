from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page

class Alerts(Page):

    def create_alert(self):
        self.driver.execute_script('window.alert(\'Hello World\')')

    def create_prompt(self):
        self.driver.execute_script('window.prompt(\'Hello World\')')

    def create_confirm(self):
        self.driver.execute_script('window.confirm(\'Hello World\')')

    def close_alert(self):
        alert = self.wait_until_alert_is_present()
        # self.driver.switch_to_alert
        alert.accept()

    def close_prompt(self):
        alert = self.wait_until_alert_is_present()
        alert.send_keys("Selenium")
        alert.accept()

    def close_confirm(self):
        alert = self.wait_until_alert_is_present()
        alert.dismiss()


