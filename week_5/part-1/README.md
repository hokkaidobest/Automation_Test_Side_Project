# Week 5 Part 1

## Assignment
You are working on an e-commerce development project - Stylish.

Project Manager (PM) provided a [system requirement](https://docs.google.com/document/d/1TBzeYw5d7_tCm2sOBFECJRcBPvrPXgTrOVaCms6o3AM/edit?usp=sharing).

E-commerce development project - [Stylish](http://54.201.140.239/) is ready for testing now.

As a SDET (Software Development Engineer in Test), you should write automation script for Testing.
Let start to write automation script to execute Web UI Automation Testing.

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
