from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element
from selenium.common.exceptions import TimeoutException

class NavigationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.departments_menu = (By.ID, "nav-hamburger-menu")
        self.close_menu = (By.ID, "hmenu-close-icon")
        self.electronics_section = (By.LINK_TEXT, "Electronics")
        self.computers_section = (By.LINK_TEXT, "Computers")
        self.artsCrafts_section = (By.LINK_TEXT, "Arts & Crafts")

    def open_departments_menu(self):
        try:
            menu = wait_for_element(self.driver, self.departments_menu)
            menu.click()  
        except TimeoutException:
            print("Side menu not found.")
    def close_departments_menu(self):
        menu = wait_for_element(self.driver, self.close_menu)
        menu.click()

    def navigate_to_section(self, section_locator):
        try:
            section = wait_for_element(self.driver, section_locator)
            section.click()
        except TimeoutException:
            print("The requested section was not found.")
