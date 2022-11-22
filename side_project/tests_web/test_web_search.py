from page_objects.main_page import MainPage
from sql_objects.product import Product

from selenium.webdriver.common.keys import Keys

# Test case 1
# When search with keyword "洋裝"
# Then all searched product title should be included "洋裝"
def test_search_product_with_keyword(main_broswer):
    keyword = "洋裝"
    main_page = MainPage(main_broswer)
    
    # Send keyword to search
    main_page.input_search_text().send_keys(keyword)
    main_page.input_search_text().send_keys(Keys.ENTER)
    
    # Get element's text to verify
    products = main_page.get_search_result()
    for product in products:
        assert keyword in product.text, f"The product {product.text}'s title does not include {keyword}."

# Test case 2
# When search with empty keyword
# Then all products should be displayed
def test_search_product_with_empty_keyword(main_broswer):
    main_page = MainPage(main_broswer)

    # Send keyword to search
    main_page.input_search_text().send_keys("")
    main_page.input_search_text().send_keys(Keys.ENTER)
    
    # Get Selenium's saerch result
    products = main_page.get_products_count_with_empty_keyword()

    # Get SQL's select result
    sql = Product()
    sql_products = sql.get_products_count_with_empty_keyword()

    # Compare number of Selenium's result and DB's result
    assert products == sql_products, "The search value dose not same between Web UI and API."

# Test case 3
# When search with keyword "Hello"
# Then no product should be displayed
def test_search_product_with_keyword_but_empty_result(main_broswer):
    keyword = "Hello"
    main_page = MainPage(main_broswer)

    # Send keyword to search
    main_page.input_search_text().send_keys(keyword)
    main_page.input_search_text().send_keys(Keys.ENTER)

    # Get saerch result
    products = main_page.check_element_exists_by_xpath()

    assert products == False, "Wrong result, please check later."

    # Get SQL's select result
    sql = Product()
    sql_products = sql.get_product_count_with_keyword(keyword)

    # Compare number of Selenium's result and DB's result
    assert products == sql_products, "Wrong result, DB data and UI elements does not match."