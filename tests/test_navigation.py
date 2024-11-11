import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.navigation_page import NavigationPage
from utils.wait_utils import wait_for_element
from selenium.webdriver.common.by import By
from utils.config import AMAZON_URL

class TestNavigation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.add_argument("--ignore-certificate-errors")
        cls.options.add_argument("--ignore-ssl-errors")
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.get(AMAZON_URL)
        cls.navigation_page = NavigationPage(cls.driver)

    def test_navigation_to_electronics(self):
        self.navigation_page.open_departments_menu()
        self.navigation_page.navigate_to_section(self.navigation_page.electronics_section)

        #Confirm access to the "Electronics" section
        header = wait_for_element(self.driver, (By.XPATH,"//div[@class='hmenu-item hmenu-title ' and @role='heading' and text()='Electronics']"))
        self.assertIsNotNone(header, "You have not navigated to the electronics section.")
        self.navigation_page.close_departments_menu()

    def test_navigation_to_computers(self):
        self.navigation_page.open_departments_menu()
        self.navigation_page.navigate_to_section(self.navigation_page.computers_section)

    #     # Confirm access to the "Computers" section
        header = wait_for_element(self.driver, (By.XPATH,"//div[@class='hmenu-item hmenu-title ' and @role='heading' and text()='Computers']"))
        self.assertIsNotNone(header, "You have not navigated to the Computers section.")
        self.navigation_page.close_departments_menu()

    def test_navigation_to_arts_crafts(self):
        self.navigation_page.open_departments_menu()
        self.navigation_page.navigate_to_section(self.navigation_page.artsCrafts_section)

        # Confirm access to the "Arts & Crafts" section
        header = wait_for_element(self.driver, (By.XPATH,"//div[@class='hmenu-item hmenu-title ' and @role='heading' and text()='Arts & Crafts']"))
        self.assertIsNotNone(header, "You have not navigated to the Arts & Crafts section.")
        self.navigation_page.close_departments_menu()
  
    @classmethod
    def tearDownClass(cls):
        input("click enter")
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
