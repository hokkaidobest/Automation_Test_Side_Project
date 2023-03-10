from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionUtils():
    def __init__(self, driver):
        self.driver = driver

    def find_present_elem(self, locator, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )
        return elem

    def find_present_elems(self, locator, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elem

    def find_clickable_elem(self, locator, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        return elem

    def check_elem_exist(self, locator, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until_not(
            EC.presence_of_element_located(locator)
        )
        return elem

    def alert_is_present(self, timeout = 10):
        elem = WebDriverWait(self.driver, timeout).until(
            EC.alert_is_present()
        )
        return elem

    def load_page(self, url):
        url = env["UAT_URL"] + url

        self.driver.get(url)

    def switch_to_iframe(self, locater):
        self.driver.switch_to.frame(locater)

    def switch_back_main_page(self):
        self.driver.switch_to.default_content()