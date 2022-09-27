# Week 7 Part 1

## Assignment: Testing for Create Product Feature
It is required to launch new products to website. We developed an [admin page](http://54.201.140.239/admin/products.html ) to create product.
You are requested to test **Create Product** feature.

### Feature: Create Product
Create a new test file "test_web_create_product.py", and write automation script for the below scenario.

#### Scenario: Create Product Success (3 Test Cases)
- **Given** login success 
- **When** create product with valid values (According to Stylish-Test Case.xlsx - "Create Product Success" sheet)
- **Then** alert message "Create Product Success" should be shown
- **And** new product should be displayed on product list

#### Scenario: Create Product with Invalid Value (20 Test Cases)
- **Given** login success 
- **When** create product with valid values (According to Stylish-Test Case.xlsx - "Create Product Failed" sheet)
- **Then** related alert message should be shown

#### Scenario: Create Product without login
- **Given** product added to shopping cart
- **When** create product with valid values
- **Then** alert message "Please Login first" should be shown
- **And** should be redirected to login page

---
### Requirements:
- Place image files to /test_data, should be used to upload and create product.
- In "Create Product Success" sheet, you should rename the product name with your name XXXX_Product.
- To reset the data in a database to its pre-test state. It is required to delete product if product create successfully. 
- Try to execute test in parallel. Run 2 or more tests simultaneously.

