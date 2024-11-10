from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.name_field = (By.ID, "ap_customer_name")
        self.email_field = (By.ID, "ap_email")
        self.password_field = (By.ID, "ap_password")
        self.repassword_field = (By.ID, "ap_password_check")
        self.continue_button = (By.ID, "continue")

    def register(self, name, email, password,repassword_field):
        self.enter_text(self.name_field, name)
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.enter_text(self.repassword_field,repassword_field)
        self.click_element(self.continue_button)
