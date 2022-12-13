import logging, allure, pytest

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from api_objects.product_category import ProductCategory
from api_objects.product_search import ProductSearch
from api_objects.product_detail import ProductDetail
from sql_objects.product import Product

base_url = env["UAT_URL"]

# Test case 1：get product by category successfully
# Test API: products/{category}?paging={paging}
@pytest.mark.parametrize('category', ["men", "women", "accessories"])
def test_get_product_by_category_successfully(session, category):

    with allure.step("[START] test_get_product_by_category_successfully"):
        paging = 0
        api_result = []

    while True:
        
        with allure.step("Send API request"):
            url = base_url + f"api/1.0/products/{category}?paging={paging}"
            product_api = ProductCategory(session)
            response = product_api.get_product_by_category(url)

        with allure.step("Verify API response status code"):
            assert response.status_code == 200
            LOGGER.info("[VERIFICATION] The http status code should be 200")

        with allure.step("Save API response"):
            api_result = api_result + response.json()["data"]

        with allure.step("Check whether to send the request again"):
            if not (response.json().get("next_paging") is None):
                paging = response.json()["next_paging"]
            else:
                api_result_count = len(api_result)
                break

    with allure.step("Get product data via category"):
        product_sql = Product()
        db_result = product_sql.get_product_by_category(category)
        db_result_count = len(db_result)

    with allure.step("Verify API and DB same category count"):
        assert api_result_count == db_result_count
        LOGGER.info(f"[DATA] Count of API response: {api_result_count}, count of DB response: {db_result_count}")
        LOGGER.info("[VERIFICATION] The product count of API and DB are same")

    with allure.step("Check the category of each product"):
        for product in api_result:
            assert product["category"] == category
            LOGGER.info(f"[VERIFICATION] The product: {product['title']} category is same to request")

    with allure.step("[END] test_get_product_by_category_successfully"):
        pass

# Test case 2：get all product successfully
# Test API: products/{category}?paging={paging}
@pytest.mark.parametrize('category', ["all"])
def test_get_all_product_by_successfully(session, category):
    
    with allure.step("[START] test_get_all_product_by_successfully"):
        paging = 0
        api_result = []

    while True:
        
        with allure.step("Send API request"):
            url = base_url + f"api/1.0/products/{category}?paging={paging}"
            product_api = ProductCategory(session)
            response = product_api.get_product_by_category(url)

        with allure.step("Verify API response status code"):
            assert response.status_code == 200
            LOGGER.info("[VERIFICATION] The http status code should be 200")

        with allure.step("Save API response"):
            api_result = api_result + response.json()["data"]

        with allure.step("Check whether to send the request again"):
            if not (response.json().get("next_paging") is None):
                paging = response.json()["next_paging"]
            else:
                api_result_count = len(api_result)
                break

    with allure.step("Get product data via category"):
        product_sql = Product()
        db_result = product_sql.get_product_by_category(category)
        db_result_count = len(db_result)

    with allure.step("Verify API and DB same category count"):
        assert api_result_count == db_result_count
        LOGGER.info(f"[DATA] Count of API response: {api_result_count}, count of DB response: {db_result_count}")
        LOGGER.info("[VERIFICATION] The product count of API and DB are same")

    with allure.step("[END] test_get_all_product_by_successfully"):
        pass

# Test case 3：get product by category failed
# Test API: products/{category}?paging={paging}
@pytest.mark.parametrize('category', ["fasion"])
def test_get_product_by_category_failed(session, category):
    
    with allure.step("[START] test_get_product_by_category_failed"):
        paging = 0

    with allure.step("Send API request"):
        url = base_url + f"api/1.0/products/{category}?paging={paging}"
        product_api = ProductCategory(session)
        response = product_api.get_product_by_category(url)

    with allure.step("Verify API response status code"):
        assert response.status_code == 400
        LOGGER.info("[VERIFICATION] The http status code should be 200")

    with allure.step("Verify API error message"):
        assert response.json()["errorMsg"] == "Invalid Category"
        LOGGER.info("[VERIFICATION] The error message should be shown")

    with allure.step("[END] test_get_product_by_category_failed"):
        pass

# Test case 4 : get search result by keyword successfully
# Test API: products/search?keyword={keyword}&paging={paging}
@pytest.mark.parametrize('keyword', ["洋裝", "牛仔褲", "襯衫", "西裝", "包"])
def test_get_product_by_keyword_successfully(session, keyword):

    with allure.step("[START] test_get_product_by_keyword_successfully"):
        paging = 0

    with allure.step("Send API request"):
        url = base_url + f"api/1.0/products/search?keyword={keyword}&paging={paging}"
        product_api = ProductSearch(session)
        response = product_api.get_product_by_keyword(url)
        api_result_count = len(response.json()["data"])

    with allure.step("Verify API response status code"):
        assert response.status_code == 200
        LOGGER.info("[VERIFICATION] The http status code should be 200")

    with allure.step("Get DB product data via keyword"):
        product_sql = Product()
        db_result_count = product_sql.get_product_count_with_keyword(keyword)

    with allure.step("Verify API and DB same keyword count"):
        assert api_result_count == db_result_count["COUNT(*)"]
        LOGGER.info(f"[DATA] Count of API response: {api_result_count}, count of DB response: {db_result_count}")
        LOGGER.info("[VERIFICATION] The product count of API and DB are same")

    with allure.step("[END] test_get_product_by_keyword_successfully"):
        pass

# Test case 5 : get search result by keyword failed
# Test API: products/search?keyword={keyword}&paging={paging}
@pytest.mark.parametrize('keyword', ["軍裝"])
def test_get_product_by_keyword_failed(session, keyword):

    with allure.step("[START] test_get_product_by_keyword_failed"):
        paging = 0

    with allure.step("Send API request"):
        url = base_url + f"api/1.0/products/search?keyword={keyword}&paging={paging}"
        product_api = ProductSearch(session)
        response = product_api.get_product_by_keyword(url)
        api_result_count = len(response.json()["data"])

    with allure.step("Verify API response status code"):
        assert response.status_code == 200
        LOGGER.info("[VERIFICATION] The http status code should be 200")

    with allure.step("Verify API response is an empty list"):
        assert api_result_count == 0
        LOGGER.info("[VERIFICATION] The API response should be an empty list")

    with allure.step("[END] test_get_product_by_keyword_failed"):
        pass

# Test case 6 : get product detail by id successfully
# Test API: products/details?id={product_id}
@pytest.mark.parametrize('id', ["201807201824"])
def test_get_product_detail_by_id_successfully(session, id):

    with allure.step("[START] test_get_product_detail_by_id_successfully"):

        with allure.step("Send API request"):
            url = base_url + f"api/1.0/products/details?id={id}"
            product_api = ProductDetail(session)
            api_response = product_api.get_product_detail_by_id(url)

    with allure.step("Verify API response status code"):
        assert api_response.status_code == 200
        LOGGER.info("[VERIFICATION] The http status code should be 200")

    with allure.step("Verify API response is only one product"):
        assert len(api_response.json()) == 1
        LOGGER.info("[VERIFICATION] API response is only one product")

    with allure.step("Get DB product data via id"):
        product_sql = Product()
        db_result = product_sql.get_product_by_id(id)

    with allure.step("Verify API and DB data should has same id"):
        assert api_response.json()["data"]["id"] == db_result["id"]
        LOGGER.info(f"[DATA] API response product id is: {api_response.json()['data']['id']}, DB selected product id is: {db_result['id']}")
        LOGGER.info("[VERIFICATION] The product id of API and DB are same")

    with allure.step("[END] test_get_product_detail_by_id_successfully"):
        pass

# Test case 7 : get product detail by id failed
# Test API: products/details?id={product_id}
@pytest.mark.parametrize("id, errorMessage", [("", "Invalid Category"), ("123456", "Invalid Product ID")])
def test_get_product_detail_by_id_failed(session, id, errorMessage):

    with allure.step("[START] test_get_product_detail_by_id_failed"):

        with allure.step("Send API request"):
            url = base_url + f"api/1.0/products/details?id={id}"
            product_api = ProductDetail(session)
            api_response = product_api.get_product_detail_by_id(url)

    with allure.step("Verify API response status code"):
        assert api_response.status_code == 400
        LOGGER.info("[VERIFICATION] The http status code should be 400")

    with allure.step("Verify API response error message"):
        assert api_response.json()["errorMsg"] == errorMessage
        LOGGER.info("[VERIFICATION] API resonse message")

    with allure.step("[END] test_get_product_detail_by_id_failed"):
        pass