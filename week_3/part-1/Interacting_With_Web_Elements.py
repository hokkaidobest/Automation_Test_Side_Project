import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select


# Step 1 : Open the Chrome browser.
options = Options()
options.chrome_executable_path = "/usr/local/bin/chromedriver"

driver = webdriver.Chrome(options = options)
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Step 2 : Go to Demo Store (http://demostore.supersqa.com)
driver.get("http://demostore.supersqa.com")

# Step 3 : Add “Album” to cart and view cart
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "?add-to-cart=24")]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "added_to_cart wc-forward")]'))).click()

# Step 4 : Change the quantity to 2 and update cart in Cart Page
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@title, "Qty")]')))
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@title, "Qty")]'))).clear()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@title, "Qty")]'))).send_keys("2")
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@name, "update_cart")]'))).click()

time.sleep(3)

# Step 5 : Verify that Subtotal is $30.00
subtotal = wait.until(EC.presence_of_element_located((By.XPATH, '//td[contains(@data-title, "Subtotal")]'))).text
assert subtotal == "$30.00", "The subtotal price shoud be $30.00!"

# Step 6 : Click “Checkout” and Fill in the form as 
wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "checkout-button button alt wc-forward")]'))).click()
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_first_name")]'))).send_keys("First")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_last_name")]'))).send_keys("Last")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_company")]'))).send_keys("ABC Company")
Select(wait.until(EC.element_to_be_clickable((By.NAME, 'billing_country')))).select_by_value('TW')
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_address_1")]'))).send_keys("Address Line 1")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_address_2")]'))).send_keys("Address Line 2")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_city")]'))).send_keys("Taipei")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_state")]'))).send_keys("Taipei")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_postcode")]'))).send_keys("101")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_phone")]'))).send_keys("0123456789")
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "billing_email")]'))).send_keys("abc@abc.com")

# Step 7 : Create an account with password “1234QWERasdf!@#$” in Checkout Page
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[contains(@id, "createaccount")]'))).click()
time.sleep(3)
wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@id, "account_password")]'))).send_keys("1234QWERasdf!@#$")

# Step 8 : Fill in Additional Information with “Thank you!” in Checkout Page
wait.until(EC.presence_of_element_located((By.XPATH, '//textarea[contains(@id, "order_comments")]'))).send_keys("Thank you!")

# Step 9 : Click Place Order
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@id, "place_order")]'))).click()

# Step 10 : Verify that “Invalid payment method” is displayed.
alert_message = wait.until(EC.presence_of_element_located((By.XPATH, '//ul[contains(@class, "woocommerce-error")]'))).text
assert alert_message == "Invalid payment method.", "Something went wrong"

# Step 11 : Finally, Close the Browser
driver.quit()