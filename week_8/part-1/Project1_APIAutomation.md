# Week 8 Part 1 (Deadline: 2022/12/07 23:59)

## Assignment
According to [Stylish API Document](https://app.swaggerhub.com/apis-docs/YINGNTY/Stylish/1.0.0). You should to write API Automation Test for following APIs:  


### User APIs 
1.  /user/login
2.  /user/logout
3.  /user/profile

---
### Requirements:
- You are required to connect with database for verifying if the information is correct.

### Expected Project Structure
```
    ├── tests_web
          ├── __init__.py
          ├── conftest.py
          └── test_xxxx.py
    ├── tests_api
          ├── __init__.py
          ├── conftest.py
          └── test_xxxx.py
    ├── page_objects
          ├── xxxx_page.py
          └── action_utils.py (optional)
    ├── api_objects
          ├── xxxx_api.py
          └── api_utils.py (optional)
    ├── test_data
          ├── xxxx.xlxs (New)
          └── get_data_from_excel.py (New)
    ├── .env
    ├── pytest.ini
    └── requirement.rf
```