from page_objects.action_utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pathlib import Path

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

class AdminProductPage(ActionUtils):
    def __init__(self, driver):
        super().__init__(driver)

    get_create_new_product_btn_locator = (By.XPATH, "//button[text() = 'Create New Product']")
    get_category_locator = (By.NAME, "category")
    get_title_locator = (By.NAME, "title")
    get_description_locator = (By.NAME, "description")
    get_price_locator = (By.NAME, "price")
    get_texture_locator = (By.NAME, "texture")
    get_wash_locator = (By.NAME, "wash")
    get_place_of_production_locator = (By.NAME, "place")
    get_note_locator = (By.NAME, "note")
    get_color_locator = (By.ID, "color_ids")
    get_size_locator = (By.NAME, "sizes")
    get_story_locator = (By.NAME, "story")
    get_main_image_locator = (By.NAME, "main_image")
    get_other_images_locator = (By.NAME, "other_images")
    get_create_procudt_btn_locator = (By.XPATH, "//input[@value = 'Create']")
    get_product_title_locator = (By.ID, "product_title")

    def click_create_new_product_btn(self):
        self.find_clickable_elem(self.get_create_new_product_btn_locator).click()
        
    def switch_to_the_page(self, window):
        if window == "product creation page":
            self.driver.switch_to.window(self.driver.window_handles[1])
        elif window == "product list page":
            self.driver.switch_to.window(self.driver.window_handles[0])

    def select_product_category(self, data):
        category = Select(self.find_present_elem(self.get_category_locator))
        category.select_by_visible_text(data)

    def select_product_color(self, data):
        colors = self.find_present_elems(self.get_color_locator)
        colors_options = {
            "白色": 0,
            "亮綠": 1,
            "淺灰": 2,
            "淺棕": 3,
            "淺藍": 4,
            "深藍": 5,
            "粉紅": 6
        }

        if data == "全選":
            for i in range(len(colors)):
                colors[i].click()
        elif data != "":
            select_color = data.split(", ")
            for color in select_color:
                colors[colors_options[color]].click()

    def select_product_size(self, data):
        sizes = self.find_present_elems(self.get_size_locator)
        sizes_options = {
            "S": 0,
            "M": 1,
            "L": 2,
            "XL": 3,
            "F": 4
        }
        if data == "全選":
            for i in range(len(sizes)):
                sizes[i].click()
        elif data != "":
            select_size = data.split(", ")
            for size in select_size:
                sizes[sizes_options[size]].click()

    def update_product_image(self, type, is_upload):
        image_path = Path(__file__).parents[1]
        LOGGER.info(f"[DATA] image_path is :{image_path}")
        
        main_image= f"{image_path}/test_data/mainImage.jpg"
        LOGGER.info(f"[DATA] main_image path is :{main_image}")

        other_image_0= f"{image_path}/test_data/otherImage0.jpg"
        other_image_1= f"{image_path}/test_data/otherImage1.jpg"

        if type == "Main Image" and is_upload == "sample image":
            self.find_clickable_elem(self.get_main_image_locator).send_keys(main_image)
        elif type == "Other Image 1" and is_upload == "sample image":
            self.find_present_elems(self.get_other_images_locator)[0].send_keys(other_image_0)
        elif type == "Other Image 2" and is_upload == "sample image":
            self.find_present_elems(self.get_other_images_locator)[1].send_keys(other_image_1)

    def input_product_data(self, data):
        LOGGER.info(f"[DATA] Fill in product_data to the form :{data}")

        self.select_product_category(data["Category"])
        self.find_clickable_elem(self.get_title_locator).send_keys(data["Title"])
        self.find_clickable_elem(self.get_description_locator).send_keys(data["Description"])
        self.find_clickable_elem(self.get_price_locator).send_keys(data["Price"])
        self.find_clickable_elem(self.get_texture_locator).send_keys(data["Texture"])
        self.find_clickable_elem(self.get_wash_locator).send_keys(data["Wash"])   
        self.find_clickable_elem(self.get_place_of_production_locator).send_keys(data["Place of Product"])
        self.find_clickable_elem(self.get_note_locator).send_keys(data["Note"])
        self.select_product_color(data["Colors"])
        self.select_product_size(data["Sizes"])
        self.find_clickable_elem(self.get_story_locator).send_keys(data["Story"])
        self.update_product_image("Main Image", data["Main Image"])
        self.update_product_image("Other Image 1", data["Other Image 1"])
        self.update_product_image("Other Image 2", data["Other Image 2"])
        
    def click_create_product_btn(self):
        self.find_clickable_elem(self.get_create_procudt_btn_locator).click()

    def check_product_creation(self):
        result = self.get_product_title_list()
        return result

    def get_product_title_list(self):
        product_title_list = []
        title = self.find_present_elems(self.get_product_title_locator)

        for i in title:
            product_title_list.append(i.text)
        
        return product_title_list

    def delete_product(self, title):
        delete_btn = (By.XPATH, f"//td[text() = '{title}']/following-sibling::td/child::button")
        self.find_clickable_elem(delete_btn).click()  