import pytest

from page_objects.main_page import MainPage
from sql_objects.product import Product

# Test case 1
# When select a category (Women / Men / Accessories)
# Then correct products in category should be displayed.
categories = [
    {
        "type": "women"
    },
    {
        "type": "men"
    },
    {
        "type": "accessories"
    }
]

@pytest.mark.parametrize('categories', categories)
def test_category(driver, categories):
    
    # Get UI procucts id list
    main_page = MainPage(driver)
    main_page.click_category_button(categories["type"])
    ui_product_list = main_page.get_products_id_list_by_category()

    # Get SQL products id list
    sql = Product()
    sql_product_list = sql.get_products_id_list_by_category(categories["type"])

    # Compare UI and SQL product id
    assert ui_product_list not in sql_product_list, "The data between UI and API are not the same."