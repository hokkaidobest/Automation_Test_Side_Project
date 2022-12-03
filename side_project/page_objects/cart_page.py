from page_objects.action_utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class CartPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_item_id_locator = (By.XPATH, "//div[@class = 'cart__item-id']")
    get_item_name_locator = (By.XPATH, "//div[@class = 'cart__item-name']")
    get_item_color_locator = (By.XPATH, "//div[@class = 'cart__item-color']")
    get_item_size_locator = (By.XPATH, "//div[@class = 'cart__item-size']")
    get_item_quantity_locator = (By.XPATH, "//select[@class = 'cart__item-quantity-selector']")
    get_item_price_locator = (By.XPATH, "//div[@class = 'cart__item-price-content']")
    get_item_subprice = (By.XPATH, "//div[@class = 'cart__item-subtotal-content']")
    get_icon_cart_number_locator = (By.XPATH, "//div[@class = 'header__link-icon-cart-number']")
    get_item_delete_btn_locator = (By.XPATH, "//div[@class = 'cart__delete-button']")

    def get_cart_item_info(self):
        item = {
            "id": self.find_present_elem(self.get_item_id_locator).text,
            "title": self.find_present_elem(self.get_item_name_locator).text,
            "color": self.find_present_elem(self.get_item_color_locator).text.split("｜")[1],
            "size": self.find_present_elem(self.get_item_size_locator).text.split("｜")[1],
            "quantity": int(Select(self.find_present_elem(self.get_item_quantity_locator)).first_selected_option.text),
            "price": int(self.find_present_elem(self.get_item_price_locator).text.split(".")[1])
        }

        item["sub_total"] = item["quantity"] * item["price"]

        return item
    
    def get_cart_number(self):
        return self.find_present_elem(self.get_icon_cart_number_locator).text

    def delect_item(self):
        self.find_clickable_elem(self.get_item_delete_btn_locator).click()

    def edit_item_quantity(self, new_quantity):
        select = Select(self.find_present_elem(self.get_item_quantity_locator))
        select.select_by_index(new_quantity)

    def get_edit_sub_total(self):
        updated_quantity = int(Select(self.find_present_elem(self.get_item_quantity_locator)).first_selected_option.text)
        price = int(self.find_present_elem(self.get_item_price_locator).text.split(".")[1])
        LOGGER.info(f"[DATA] update_quantity :{updated_quantity}, update_sub_price: {updated_quantity * price}")

        return price * updated_quantity