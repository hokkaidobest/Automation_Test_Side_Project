# Week 5 Part 1 (Deadline: 2022/11/17 00:00)

## Assignment
Let start to write automation script to execute Web UI Automation Testing for Stylish.

---
### Feature: Product Search
Create a test file "test_web_search.py" and write automation script for below scenarios

#### Scenario: Search Product By Keyword
- **When** search with keyword "洋裝"
- **Then** all searched product title should be included "洋裝"

#### Scenario: Search Product Without Keyword
- **When** search with empty keyword
- **Then** no product should be displayed 

#### Scenario: Search Product - No Product Found
- **When** search with keyword "Hello"
- **Then** all products should be displayed

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
          ├── test_xxxx.py
    ├── page_objects
          └── xxxx_page.py
    ├── pytest.ini
    └── requirement.rf
```