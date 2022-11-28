from page_objects.main_page import MainPage
from sql_objects.product import Product

# Test case 1
# When search with keyword "洋裝"
# Then all searched product title should be included "洋裝"
def test_search_product_with_keyword(main_browser):
    keyword = "洋裝"
    main_page = MainPage(main_browser)
    
    # Send keyword to search
    main_page.input_search_text(keyword)
    
    # Get element's text to verify
    products = main_page.get_search_result()
    for product in products:
        assert keyword in product.text, f"The product {product.text}'s title does not include {keyword}."

# Test case 2
# When search with empty keyword
# Then all products should be displayed
def test_search_product_with_empty_keyword(main_browser):
    keyword = ""
    main_page = MainPage(main_browser)

    # Send keyword to search
    main_page.input_search_text(keyword)
    
    # Get Selenium's saerch result
    products = main_page.get_products_count_with_empty_keyword()

    # Get SQL's select result
    sql = Product()
    sql_products = sql.get_products_count_with_empty_keyword()

    # Compare number of Selenium's result and DB's result
    assert products == sql_products, "The search value dose not same between Web UI and Sql."

# Test case 3
# When search with keyword "Hello"
# Then no product should be displayed
def test_search_product_with_keyword_but_empty_result(main_browser):
    keyword = "Hello"
    main_page = MainPage(main_browser)

    # Send keyword to search
    main_page.input_search_text(keyword)

    # Get saerch result
    products = main_page.check_element_exists_by_xpath()

    # The product was not found
    assert products == False, "Wrong result, please check later."

    # Get SQL's select result
    sql = Product()
    sql_products = sql.get_product_count_with_keyword(keyword)

    # Compare number of Selenium's result and DB's result
    assert products == sql_products, "Wrong result, DB data and UI elements does not match."