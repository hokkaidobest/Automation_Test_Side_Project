import pytest

from page_objects.main_page import MainPage
from api_objects.get_method import Get
from sql_objects.main_page_sql import MainPageSql

# Test case 1
# When select a category (Women / Men / Accessories)
# Then correct products in category should be displayed.
categories = [
    {
        "type": "women",
        "link": "女裝"
    },
    {
        "type": "men",
        "link": "男裝"
    },
    {
        "type": "accessories",
        "link": "配件"
    }
]

@pytest.mark.parametrize('categories', categories)
def test_products_displayed_by_category(main_broswer, categories):
    
    # Get UI procucts id list
    main_page = MainPage(main_broswer)
    main_page.click_category_button(categories["type"])
    ui_product_count = main_page.get_products_id_list_by_category()
    
    # Get API products id list
    search_api = Get()
    api_product_count = search_api.get_products_id_list_by_category(categories["type"])
    
    # Compare UI and API product id
    assert ui_product_count not in api_product_count, "The data between UI and API are not the same."

    # # Get SQL products id list
    search_sql = MainPageSql()
    sql_product_count = search_sql.get_products_id_list_by_category(categories["type"])

    # # Compare UI and SQL product id
    assert ui_product_count not in sql_product_count, "The data between UI and API are not the same."