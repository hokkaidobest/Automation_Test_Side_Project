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
    get_ckeckout_btn_locator = (By.XPATH, "//button[@class = 'checkout-button']")
    get_checkout_form_name_input_locator = (By.XPATH, "//div[text() = '收件人姓名']/following-sibling::input")
    get_checkout_form_email_input_locator = (By.XPATH, "//div[text() = 'Email']/following-sibling::input")
    get_checkout_form_phone_input_locator = (By.XPATH, "//div[text() = '手機']/following-sibling::input")
    get_checkout_form_address_input_locator = (By.XPATH, "//div[text()='地址']/following-sibling::input")
    get_checkout_form_deliver_time_morning_locator = (By.XPATH, "//label[text() = '08:00-12:00']/child::input")
    get_checkout_form_deliver_time_afternoon_locator = (By.XPATH, "//label[text() = '14:00-18:00']/child::input")
    get_checkout_form_deliver_time_anytime_locator = (By.XPATH, "//label[text() = '不指定']/child::input")
    get_card_number_iframe_locator = (By.XPATH, "//div[@id = 'card-number']/iframe")
    get_card_number_input_locator = (By.ID, "cc-number")
    get_expiration_date_iframe_locator = (By.XPATH, "//div[@id = 'card-expiration-date']/iframe")
    get_expiration_date_input_locator = (By.ID, "cc-exp")
    get_ccv_iframe_locator = (By.XPATH, "//div[@id = 'card-ccv']/iframe")
    get_ccv_input_locator = (By.ID, "cc-ccv")
    get_order_quantity_locator = (By.XPATH, "//div[@class = 'cart__item-quantity-title']/following-sibling::div")
    get_order_total_amount_locator = (By.XPATH, "//div[@class = 'payable']/child::div[@class = 'total__amount']")
    get_order_reveiver_locator = (By.XPATH, "//div[text() = '收件人: ']/following-sibling::div")
    get_order_email_locator = (By.XPATH, "//div[text() = 'Email: ']/following-sibling::div")
    get_order_mobile_locator = (By.XPATH, "//div[text() = '手機: ']/following-sibling::div")
    get_order_address_locator = (By.XPATH, "//div[text() = '地址: ']/following-sibling::div")
    get_order_deliver_locator = (By.XPATH, "//div[text() = '配送時間: ']/following-sibling::div")

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

    def click_checkout_btn(self):
        self.find_clickable_elem(self.get_ckeckout_btn_locator).click()

    def input_checkout_info(self, checkout_data):
        LOGGER.info(f"[DATA] Fill in checkout_data to the form :{checkout_data}")

        self.find_clickable_elem(self.get_checkout_form_name_input_locator).send_keys(checkout_data["Receiver"])
        self.find_clickable_elem(self.get_checkout_form_email_input_locator).send_keys(checkout_data["Email"])
        self.find_clickable_elem(self.get_checkout_form_phone_input_locator).send_keys(checkout_data["Mobile"])
        self.find_clickable_elem(self.get_checkout_form_address_input_locator).send_keys(checkout_data["Address"])
        
        if checkout_data["Deliver Time"] == "Anytime":
            self.find_clickable_elem(self.get_checkout_form_deliver_time_anytime_locator).click()
        elif checkout_data["Deliver Time"] == "Morning":
            self.find_clickable_elem(self.get_checkout_form_deliver_time_morning_locator).click()
        elif checkout_data["Deliver Time"] == "Afternoon":
            self.find_clickable_elem(self.get_checkout_form_deliver_time_afternoon_locator).click()
        
        self.switch_to_iframe(self.find_present_elem(self.get_card_number_iframe_locator))
        self.find_clickable_elem(self.get_card_number_input_locator).send_keys(checkout_data["Credit Card No"])
        self.switch_back_main_page()
        
        self.switch_to_iframe(self.find_present_elem(self.get_expiration_date_iframe_locator))
        self.find_clickable_elem(self.get_expiration_date_input_locator).send_keys(checkout_data["Expiry Date"])
        self.switch_back_main_page()
        
        self.switch_to_iframe(self.find_present_elem(self.get_ccv_iframe_locator))
        self.find_clickable_elem(self.get_ccv_input_locator).send_keys(checkout_data["Security Code"])
        self.switch_back_main_page()

    def get_order_product_info(self):
        item = {
            "id": self.find_present_elem(self.get_item_id_locator).text,
            "title": self.find_present_elem(self.get_item_name_locator).text,
            "color": self.find_present_elem(self.get_item_color_locator).text.split("｜")[1],
            "size": self.find_present_elem(self.get_item_size_locator).text.split("｜")[1],
            "quantity": int(self.find_present_elem(self.get_order_quantity_locator).text),
            "price": int(self.find_present_elem(self.get_item_price_locator).text.split(".")[1])
        }

        item["sub_total"] = item["quantity"] * item["price"]

        return item

    def get_order_recipient_info(self):
        info = {
            "amount_payable": int(self.find_present_elem(self.get_order_total_amount_locator).text),
            "Receiver": self.find_present_elem(self.get_order_reveiver_locator).text,
            "Email": self.find_present_elem(self.get_order_email_locator).text,
            "Mobile": self.find_present_elem(self.get_order_mobile_locator).text,
            "Address": self.find_present_elem(self.get_order_address_locator).text
        }
        
        if self.find_present_elem(self.get_order_deliver_locator).text == "不指定":
            info["Deliver Time"] = "Anytime"
        elif self.find_present_elem(self.get_order_deliver_locator).text == "08:00 - 12:00":
            info["Deliver Time"] = "Morning"
        else:
            info["Deliver Time"] = "Afternoon"

        return info