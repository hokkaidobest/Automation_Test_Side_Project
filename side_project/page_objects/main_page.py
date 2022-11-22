import time

from page_objects.action_utils import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class MainPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_input_search_text_locator = (By.XPATH, "//input[@class = 'header__search-input']")
    get_search_result_locator = (By.XPATH, "//div[@class = 'product__title']")

    def input_search_text(self):
        return self.find_clickable_elem(self.get_input_search_text_locator)

    def get_search_result(self):
        return self.find_present_elems(self.get_search_result_locator)
    
    def get_products_count_with_empty_keyword(self):
        self.scroll_page()

        products = self.driver.find_elements(By.XPATH, "//a[@class = 'product']")

        return len(products)
 
    def check_element_exists_by_xpath(self):
        try:
            self.driver.find_element(By.XPATH, "//div[@class = 'product']")
        except NoSuchElementException:
            return False
        
        return True
    
    def click_category_button(self, category):
        self.find_clickable_elem((By.CSS_SELECTOR, f'a[href="./index.html?category={category}"]')).click()

    def get_products_id_list_by_category(self):
        self.scroll_page()

        result = []
        for element in self.driver.find_elements(By.XPATH, "//div[@class = 'product__title']"):
            result.append(element.text)

        return result

    def scroll_page(self):
        SCROLL_PAUSE_TIME = 1

        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height