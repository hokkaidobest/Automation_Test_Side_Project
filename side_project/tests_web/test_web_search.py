from page_objects.main_page import MainPage
from api_objects.get_method import Get
from sql_objects.main_page_sql import MainPageSql

from selenium.webdriver.common.keys import Keys

# Test case 1
# When search with keyword "洋裝"
# Then all searched product title should be included "洋裝"
def test_search_product_by_key(main_broswer):
    keyword = "洋裝"
    main_page = MainPage(main_broswer)
    
    # Send keyword to search
    main_page.click_search_btn().send_keys(keyword)
    main_page.click_search_btn().send_keys(Keys.ENTER)
    
    # Get element's text to varify
    products = main_page.get_search_result()
    for product in products:
        assert keyword in product.text, f"The product {product.text}'s title does not include {keyword}."

    # Get API response
    search_keyword_api = Get()
    result_count = search_keyword_api.get_search_with_keyword(keyword)

    # Compare number of Selenium's result and API's result
    assert result_count == len(products), "The search result dose not match."

# Test case 2
# When search with empty keyword
# Then all products should be displayed
def test_search_product_without_key(main_broswer):
    main_page = MainPage(main_broswer)

    # Send keyword to search
    main_page.click_search_btn().send_keys("")
    main_page.click_search_btn().send_keys(Keys.ENTER)
    
    # Get saerch result
    products = main_page.get_products_count_without_keyword()

    # Get API response
    search_keyword_api = Get()
    result_count = search_keyword_api.get_products_count_without_keyword()

    # Compare number of Selenium's result and API's result
    assert result_count == products, "The search value dose not same between Web UI and API."

    # Get SQL's select result
    search_sql = MainPageSql()
    result_count = search_sql.get_products_count_without_keyword()

    # Compare number of Selenium's result and DB's result
    assert result_count == products, "The search value dose not same between Web UI and API."

# Test case 3
# When search with keyword "Hello"
# Then no product should be displayed
def test_search_product_by_keyword_with_empty_result(main_broswer):
    keyword = "Hello"
    main_page = MainPage(main_broswer)

    # Send keyword to search
    main_page.click_search_btn().send_keys(keyword)
    main_page.click_search_btn().send_keys(Keys.ENTER)

    # Get saerch result
    search_result = main_page.check_element_exists_by_xpath()

    assert search_result == False, "Wrong result, please check later."

    search_keyword_api = Get()
    result_count = search_keyword_api.get_search_with_keyword(keyword)

    assert search_result == result_count, "Wrong result, please check later."

    search_sql = MainPageSql()
    sql_result_count = search_sql.get_product_count_with_keyword(keyword)

    assert search_result == sql_result_count, "Wrong result, please check later."