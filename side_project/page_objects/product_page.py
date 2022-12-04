from page_objects.action_utils import *
from sql_objects.color import Color
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

class ProductPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_input_search_text_locator = (By.XPATH, "//input[@class = 'header__search-input']")
    get_color_locator = (By.CLASS_NAME, "product__color")
    get_selected_color_locator = (By.CLASS_NAME, "product__color--selected")
    get_size_locator = (By.XPATH, "//div[@class = 'product__size']")
    get_add_quantity_btn_locator = (By.XPATH, "//div[@class = 'product__quantity-add']")
    get_current_quantity_btn_locator = (By.XPATH, "//div[@class = 'product__quantity-value']")
    get_minus_quantity_btn_locator = (By.XPATH, "//div[@class = 'product__quantity-minus']")
    get_add_to_cart_btn_locator = (By.XPATH, "//button[@class = 'product__add-to-cart-button']")
    get_icon_cart_number_locator = (By.XPATH, "//div[@class = 'header__link-icon-cart-number']")
    get_id_locator = (By.XPATH, "//div[@class = 'product__id']")
    get_title_locator = (By.XPATH, "//div[@class = 'product__title']")
    get_price_locator = (By.XPATH, "//div[@class = 'product__price']")
    get_selected_size_locator = (By.XPATH, "//div[@class = 'product__size product__size--selected']")
    get_added_quantity_locator = (By.XPATH, "//div[@class = 'product__quantity-value']")

    def input_search_text(self, keyword):
        elem = self.find_element()
        elem.send_keys(keyword)
        elem.send_keys(Keys.ENTER)

    def find_element(self):
        return self.find_clickable_elem(self.get_input_search_text_locator)

    def click_product(self, product_id):
        self.find_clickable_elem((By.CSS_SELECTOR, f'a[href="./product.html?id={product_id}"]')).click()

    def get_color(self):
        return self.find_present_elems(self.get_color_locator)

    def get_selected_color(self):
        return self.find_clickable_elem(self.get_selected_color_locator)

    def get_size(self):
        return self.find_present_elems(self.get_size_locator)

    def click_add_quantity_btn(self, quantity = 1):
        for _ in range(quantity):
            self.find_clickable_elem(self.get_add_quantity_btn_locator).click()

    def get_current_quantity_value(self):
        return self.find_present_elem(self.get_current_quantity_btn_locator).text

    def click_size_btn(self):
        self.find_present_elem(self.get_size_locator).click()

    def click_minus_quantity_btn(self, quantity = 1):
        for _ in range(quantity):
            self.find_clickable_elem(self.get_minus_quantity_btn_locator).click()

    def click_add_to_cart_btn(self):
        self.find_clickable_elem(self.get_add_to_cart_btn_locator).click()

    def get_cart_number(self):
        return self.find_present_elem(self.get_icon_cart_number_locator).text

    def get_selected_product_info(self):
        product = {
            "id": self.find_present_elem(self.get_id_locator).text,
            "title": self.find_present_elem(self.get_title_locator).text,
            "color": self.get_color_name_by_code(self.find_present_elem(self.get_selected_color_locator).get_attribute("data_id")[-6:]),
            "size": self.find_present_elem(self.get_selected_size_locator).text,
            "quantity": int(self.find_present_elem(self.get_added_quantity_locator).text),
            "price": int(self.find_present_elem(self.get_price_locator).text.split(".")[1])
        }

        product["sub_total"] = product["quantity"] * product["price"]

        return product

    def get_color_name_by_code(self, code):
        color_sql = Color()
        color_name = color_sql.get_color_name_by_code(code)
        LOGGER.info(f"[DB] Color info: code: {code}, name: {color_name}")

        return color_name