from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_utils import wait_for_element
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return wait_for_element(self.driver,locator)

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def enter_text(self, locator, text):
        self.wait_for_element(locator).send_keys(text)
