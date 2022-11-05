from Index_Page import *
from Checkout_Page import *

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

# Step 1 : Open the Chrome browser.
# Step 2 : Go to Demo Store (http://demostore.supersqa.com)
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"
driver = webdriver.Chrome(options = options)
driver.maximize_window()
driver.get("http://demostore.supersqa.com/")

try:
    
    # INDEX PAGE
    index_page = IndexPage(driver)

    # Step 3 : Add “Album” to cart and view cart
    product_name = "Album"
    index_page.get_add_to_cart_btn_locator(product_name)
    index_page.click_add_to_cart_btn()
    index_page.click_view_cart_btn()
    
    # Step 4 : Change the quantity to 2 and update cart in Cart Page
    qty_text_field_elem = index_page.click_item_qty_btn()
    qty_text_field_elem.clear()
    qty_text_field_elem.send_keys(2)

    index_page.click_update_cart_btn()
    index_page.get_update_alert_message_locator()

    # Step 5 : Verify that Subtotal is $30.00
    subtotal_text_elem = index_page.get_subtotal_text_locator()
    assert subtotal_text_elem.text == "$30.00", "The subtotal price shoud be $30.00!"

    # Step 6 : Click “Checkout” and Fill in the form as below
    index_page.click_checkout_btn()

    # CHECKOUT PAGE
    checkout_page = CheckoutPage(driver)

    billing_first_name = checkout_page.get_ckeckout_form_column_locator("billing_first_name")
    billing_first_name = checkout_page.fill_in_ckeckout_form_column("First")

    billing_last_name = checkout_page.get_ckeckout_form_column_locator("billing_last_name")
    billing_last_name = checkout_page.fill_in_ckeckout_form_column("Last")

    billing_company = checkout_page.get_ckeckout_form_column_locator("billing_company")
    billing_company = checkout_page.fill_in_ckeckout_form_column("ABC Company")

    set_country = Select(driver.find_element(By.NAME, 'billing_country'))
    set_country.select_by_value('TW')

    billing_address_1 = checkout_page.get_ckeckout_form_column_locator("billing_address_1")
    billing_address_1 = checkout_page.fill_in_ckeckout_form_column("Address Line 1")

    billing_address_2 = checkout_page.get_ckeckout_form_column_locator("billing_address_2")
    billing_address_1 = checkout_page.fill_in_ckeckout_form_column("Address Line 2")

    billing_city = checkout_page.get_ckeckout_form_column_locator("billing_city")
    billing_city = checkout_page.fill_in_ckeckout_form_column("Taipei")

    billing_state = checkout_page.get_ckeckout_form_column_locator("billing_state")
    billing_state = checkout_page.fill_in_ckeckout_form_column("Taipei")

    billing_postcode = checkout_page.get_ckeckout_form_column_locator("billing_postcode")
    billing_postcode = checkout_page.fill_in_ckeckout_form_column("101")

    billing_phone = checkout_page.get_ckeckout_form_column_locator("billing_phone")
    billing_phone = checkout_page.fill_in_ckeckout_form_column("0123456789")

    billing_email = checkout_page.get_ckeckout_form_column_locator("billing_email")
    billing_email = checkout_page.fill_in_ckeckout_form_column("abc@abc.com")

    # Step 7 : Create an account with password “1234QWERasdf!@#$” in Checkout Page
    checkout_page.click_create_account_btn()

    account_password = checkout_page.get_ckeckout_form_column_locator("account_password")
    account_password = checkout_page.fill_in_ckeckout_form_column("1234QWERasdf!@#$")

    # Step 8 : Fill in Additional Information with “Thank you!” in Checkout Page
    order_comments = checkout_page.get_ckeckout_form_column_locator("order_comments")
    order_comments = checkout_page.fill_in_ckeckout_form_column("Thank you!")

    # Step 9 : Click Place Order
    checkout_page.click_place_order_btn()

    # Step 10 : Verify that “Invalid payment method” is displayed.
    alert_elem = checkout_page.get_checkout_alert_message()
    assert alert_elem.text == "Invalid payment method.", "Something went wrong"

finally:
    # Step 11 : Finally, Close the Browser
    driver.quit()