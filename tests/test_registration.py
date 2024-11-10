import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from pages.registration_page import RegistrationPage
from utils.config import Registration_URL
class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Registration_URL)

    def test_registration(self):
        registration_page = RegistrationPage(self.driver)
        registration_page.register("Test User", "braa1998@gmail.com", "password1234","password1234")

        assert "Authentication required" in self.driver.title or "request" in self.driver.page_source

    def tearDown(self):
        input("click enter")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
