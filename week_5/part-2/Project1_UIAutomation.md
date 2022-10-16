# Week 5 Part 2 (Deadline: 2022/11/20 23:59)

## Assignment
Create a new test file "test_web_product_page.py", and write automation script for the below scenario.

### Feature: Product Page Related Feature
#### Scenario: Color Selection
- **Given** entered a product page
- **When** select a color of the product
- **Then** selected color is highlighted

#### Scenario: Size Selection
- **Given** entered a product page
- **When** select a size of the product
- **Then** selected size is highlighted
 
#### Scenario: Quantity Editor Disabled
- **Given** entered a product page
- **When** edit quantity without size selection
- **Then** quantity editor is disabled

#### Scenario: Quantity Editor - Increase Quantity
- **Given** entered a product page
- **And** select a size of the product
- **When** add 8 more quantity
- **Then** quantity should be 9
- **When** add 2 more quantity
- **Then** quantity still be 9

#### Scenario: Quantity Editor - Decrease Quantity
- **Given** entered a product page
- **And** select a size of the product
- **And** add 8 more quantity

- **When** decrease 8 quantity
- **Then** quantity should be 1

#### Scenario: Add To Cart - Success
- **Given** entered a product page
- **And** select a size of the product
- **When** click add to cart button
- **Then** success message should be shown
- **And** cart icon number should be 1


#### Scenario: Add To Cart - Failed
- **Given** entered a product page without size selection
- **When** click add to cart button
- **Then** alert message should be shown

---
### Requirements:
- Generate **Allure Report** when testing complete.
- Attach the Testing Final Screenshot in Testing Report.
- Add Testing log.
- Write a Shell script which called **exec_test.sh** to execute test and generate allure report.