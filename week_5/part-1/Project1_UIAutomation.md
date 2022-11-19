# Week 5 Part 1 (Deadline: 2022/11/16 23:59)

## Online Learning Material
* [PyTest Documents](https://docs.pytest.org/en/7.1.x/) 
* [HeadSpin University 課程](https://ui.headspin.io/university/learn/appium-selenium-fundamentals-2020/units)
  * Section 10: Test Suite Design

## Assignment

---
### Feature: Product Search
Create a test file "test_web_search.py" and write automation script for below scenarios

#### Scenario: Search Product By Keyword
- **When** search with keyword "洋裝"
- **Then** all searched product title should be included "洋裝"

#### Scenario: Search Product Without Keyword
- **When** search with empty keyword
- **Then** all product should be displayed 

#### Scenario: Search Product - No Product Found
- **When** search with keyword "Hello"
- **Then** no products should be displayed

---
### Feature: Category
Create a test file "test_web_category.py" and write automation script for below scenario

#### Scenario: Category Selection (3 Test Cases)
- **When** select a category (Women / Men / Accessories)
- **Then** correct products in category should be displayed.

---
### Requirements:
- Using **[PyTest](https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm)** Framework and **Selenium**.
- Using PyTest **Fixture** to launch chrome webdriver.
- Should use **Page Object Model**.
- Create a **requirement.rf** to list out all python plugin needed.

### Expected Project Structure
```
    ├── tests_web
          ├── __init__.py
          ├── conftest.py
          └── test_xxxx.py
    ├── page_objects
          ├── xxxx_page.py
          └── action_utils.py (optional)
    ├── pytest.ini
    └── requirement.rf
```