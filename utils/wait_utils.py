from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))

def fluent_wait_for_element(driver, locator, timeout=30, poll_frequency=2):
    wait = WebDriverWait(driver, timeout, poll_frequency=poll_frequency)
    return wait.until(EC.visibility_of_element_located(locator))