import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from pages.search_page import SearchPage
from utils.config import AMAZON_URL

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(AMAZON_URL)

    def test_search_product(self):
        search_page = SearchPage(self.driver)
        search_page.search_for_product("laptop")
        result_text = search_page.get_first_result_text()

        self.assertIn("laptop", result_text.lower())

    def tearDown(self):
        input("click enter")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
