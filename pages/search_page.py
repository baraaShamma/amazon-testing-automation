from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_bar = (By.ID, "twotabsearchtextbox")
        self.search_button = (By.ID, "nav-search-submit-button")
        self.result_title = (By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")

    def search_for_product(self, product_name):
        self.enter_text(self.search_bar, product_name)
        self.click_element(self.search_button)

    def get_first_result_text(self):
        return self.wait_for_element(self.result_title).text
