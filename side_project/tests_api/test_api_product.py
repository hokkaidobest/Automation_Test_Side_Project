import logging, allure, pytest

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from api_objects.product_category import ProductCategory
from sql_objects.product import Product
from test_data.get_data_from_excel import GetTestData

base_url = env["UAT_URL"]

get_data = GetTestData()
success_login_data = get_data.get_success_login_data()
failed_login_data = get_data.get_failed_login_data()
failed_logout_data = get_data.get_failed_logout_data()

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