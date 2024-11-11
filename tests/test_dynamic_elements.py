import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from pages.search_page import SearchPage
from utils.wait_utils import wait_for_element
from utils.config import AMAZON_URL

class TestDynamicElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(AMAZON_URL)

    def test_dynamic_elements(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product("laptop")
        
        # نستخدم Explicit Wait للتأكد من ظهور النتائج
        first_result = wait_for_element(self.driver, search_page.result_title, timeout=15)
        self.assertIsNotNone(first_result, "The results did not appear on time.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
