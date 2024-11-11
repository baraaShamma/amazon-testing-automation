import unittest
from selenium import webdriver
from pages.product_page import ProductPage
from utils.config import Product_URL

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Product_URL) 

    def test_add_to_cart(self):
        product_page = ProductPage(self.driver)
        product_page.add_to_cart()

        assert "Added to Cart" in self.driver.page_source

    def tearDown(self):
        input("click enter")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
