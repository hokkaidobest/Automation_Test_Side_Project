# Week 6 Part 2 (Deadline: 2022/11/27 23:59)

## Assignment
You are going to test **shopping cart** and **checkout** feature.

### Feature: Shopping Cart
Create a new test file "test_web_shopping_cart.py", and write automation script for the below scenario.

#### Scenario: Shopping Cart Info Correct
- **When** add product to shopping cart
- **Then** cart info is displayed correctly

#### Scenario: Remove product from cart
- **Given** add 2 products to shopping cart 
- **When** delete product from shopping cart
- **Then** alert message "已刪除商品" should be shown
- **And** new cart info should be updated correctly
- **And** cart icon number should be updated correctly

#### Scenario: Edit quantity in cart
- **Given** product added to shopping cart
- **When** edit the quantity of the product 
- **Then** alert message "已修改數量" should be shown
- **And** subtotal should be updated correctly.


### Feature: Checkout
Create a new test file "test_web_checkout.py", and write automation script for the below scenario.

#### Scenario: Checkout with empty cart
- **When** click checkout button without add product to shopping cart
- **Then** alert message "尚未選購商品" should be shown

#### Scenario: Checkout with invalid values (17 Test Cases)
- **Given** login success 
- **And** add product to shopping cart
- **When** checkout with invalid value (According to Stylish-Test Case.xlsx - "Checkout with Invalid Value" sheet)
- **Then** related alert message should be shown

#### Scenario: Checkout with valid values (3 Test Cases)
- **Given** login success 
- **And** add product to shopping cart
- **When** checkout with valid value (According to Stylish-Test Case.xlsx - "Checkout with Valid Value" sheet)
- **Then** alert message "付款成功" should be shown
- **And** correct order info should be displayed in thankyou page
---
### Requirements:
- Create a folder with the name "test_data", and place the "Stylish-Test Case.xlsx" in the folder
- Create a file with the name "get_data_from_excel.py" to write a module for reading excel data from Stylish-Test Case.xlsx
- Using parametrizing fixtures to run the test against multiple sets of inputs.
- Try to execute test in headless browser mode. 