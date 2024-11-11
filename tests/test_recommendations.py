import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from selenium import webdriver
from pages.product_page import ProductPage
from utils.wait_utils import wait_for_element
from utils.config import Product_URL
from selenium.webdriver.common.by import By

class TestRecommendations(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Product_URL) 

    def test_recommendations(self):
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()
        
        # Check product recommendations
        recommendation_section = wait_for_element(self.driver, (By.ID, "recommendations"))
        self.assertIsNotNone(recommendation_section, "Product recommendations not shown.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
