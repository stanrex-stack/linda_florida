from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from python_selenium_automation.ultm_pckg.linda_florida.pages.base_page import Page


class SignInPage(Page):
    #MAIN BODY
    IN_BOX_EMAIL = (By.CSS_SELECTOR, "[for='ap_email']")
    IN_BOX_CONDITIONS_OF_USE = (By.ID, "legalTextRow")
    CREATE_AMAZON_BUTTON = (By.ID, "createAccountSubmit")
    NEW_TO_AMAZON = (By.CSS_SELECTOR, "h5")
    CONTINUE_BUTTON = (By.ID, "continue")
    NEED_HELP = (By.CSS_SELECTOR, ".a-expander-prompt")
    FORGOT_YOUR_PASSWORD = (By.ID, "auth-fpp-link-bottom")
    OTHER_ISSUES = (By.ID, "ap-other-signin-issues-link")
    CONDITIONS_OF_USE = (By.CSS_SELECTOR, "#legalTextRow a")
    PRIVACY_NOTICE = (By.CSS_SELECTOR, "#legalTextRow a:last-child")
    # FOOTER


    LEGAL_FOOTER = (By.CSS_SELECTOR, ".a-size-mini.a-color-secondary")
    CONDITIONS_OF_USE_IN_FOOTER = (By.CSS_SELECTOR, ".auth-footer a")
    PRIVACY_NOTICE_IN_FOOTER = (By.CSS_SELECTOR, ".auth-footer a:nth-of-type(2)")
    HELP_IN_FOOTER = (By.CSS_SELECTOR, ".auth-footer a:last-of-type")


    def verify_field_text(self, field_name, expected_text):
        """
        This function checks that each field has a certain text headline
        :param field_name: field name as typed in Gherkin file
        :param expected_text: headline text
        :return: None
        """
        if field_name == "In-Box Email":
            locator = self.IN_BOX_EMAIL
        elif field_name == "In-Box Conditions Of Use":
            locator = self.IN_BOX_CONDITIONS_OF_USE
        elif field_name == "Create Amazon Button":
            locator = self.CREATE_AMAZON_BUTTON
        elif field_name == "New To Amazon":
            locator = self.NEW_TO_AMAZON
        elif field_name == "Footer":
            locator = self.LEGAL_FOOTER
        elif field_name == "Continue Button":
            locator = self.CONTINUE_BUTTON
        elif field_name == "Need Help":
            locator = self.NEED_HELP
        elif field_name == "Forgot Your Password":
            locator = self.FORGOT_YOUR_PASSWORD
        elif field_name == "Other Issues":
            locator = self.OTHER_ISSUES
        else:
            raise Exception("No such field name found")
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, f"Expected: \"{expected_text}\", but got: \"{actual_text}\""


    def verify_item_is_clickable(self, field_name):
        """
        Verifies an item on the page is clickable
        :param field_name: field name as typed in Gherkin file
        """
        if field_name == "Continue Button":
            locator = self.CONTINUE_BUTTON
        elif field_name == "Conditions Of Use":
            locator = self.CONDITIONS_OF_USE
        elif field_name == "Privacy Notice":
            locator = self.PRIVACY_NOTICE
        elif field_name == "Forgot Your Password":
            locator = self.FORGOT_YOUR_PASSWORD
        elif field_name == "Other Issues":
            locator = self.OTHER_ISSUES
        elif field_name == "Create your Amazon account Button":
            locator = self.CREATE_AMAZON_BUTTON
        elif field_name == "Conditions Of Use In Footer":
            locator = self.CONDITIONS_OF_USE_IN_FOOTER
        elif field_name == "Privacy Notice In Footer":
            locator = self.PRIVACY_NOTICE_IN_FOOTER
        elif field_name == "Footer Help Button":
            locator = self.HELP_IN_FOOTER
        else:
            raise Exception("No such field name found")
        self.driver.wait.until(EC.element_to_be_clickable(locator))


    def verify_dropdown_appears(self, *args):
        for field_name in args:
            if field_name == "Forgot your password?":
                locator = self.FORGOT_YOUR_PASSWORD
            elif field_name == "Other issues with Sign-In":
                locator = self.OTHER_ISSUES
            else:
                raise Exception("No such field name found in the dropdown")
            actual_text = self.driver.find_element(*locator).text
            assert field_name in actual_text, f"Expected: \"{field_name}\", but got: \"{actual_text}\""


    def verify_dropdown_disappears(self, *args):
        for field_name in args:
            if field_name == "Forgot your password?":
                locator = self.FORGOT_YOUR_PASSWORD
            elif field_name == "Other issues with Sign-In":
                locator = self.OTHER_ISSUES
            else:
                raise Exception("No such field name found in the dropdown")
            self.driver.wait.until(EC.invisibility_of_element(locator))
