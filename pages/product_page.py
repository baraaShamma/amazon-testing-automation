from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.add_to_cart_button = (By.ID, "add-to-cart-button")

    def add_to_cart(self):
        self.click_element(self.add_to_cart_button)
