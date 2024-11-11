import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# test_popups.py

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.wait_utils import wait_for_element
from utils.config import AMAZON_URL

class TestPopups(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(AMAZON_URL)

    def test_handle_popups(self):
        #Example of waiting for a popup window
        try:
            popup_close_button = wait_for_element(self.driver, (By.CLASS_NAME, "close-button"))
            popup_close_button.click()
        except:
            print("No pop-up window appears.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
