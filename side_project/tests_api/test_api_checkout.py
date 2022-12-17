import logging, pytest
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from tests_web.conftest import *
from api_objects.order import Order
from sql_objects.product import Product
# from sql_objects.order import Order

from test_data.get_data_from_excel import GetTestData
get_data = GetTestData()
receiver = get_data.get_invalid_api_checkout_data()

@allure.title("Test case 1: checkout successfully")
@allure.description("API: /order")
def test_success_checkout(session, user_token, checkout_prime):

    with allure.step("[START] test_success_checkout"):
        LOGGER.info("[START] test_success_checkout")

    with allure.step("[ACTION] Get prime from web from page"):
        LOGGER.info(f"[DATA] prime: {checkout_prime}")

    with allure.step("[ACTION] Get product info from Database"):
        product_sql = Product()
        product = product_sql.get_product_for_checkout()
        product_count = len(product)

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Get receiver data"):
        receiver = order_api.get_receiver_data()

    with allure.step("[ACTION] Call order API to create an order"):
        api_order_res = order_api.create_order(checkout_prime, receiver, product, product_count, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == 200
        LOGGER.info("[VALIDATION] Create order API should responsed status code 200")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["data"]["number"] is not None
        LOGGER.info("[VALIDATION] Create order API should responsed order id")

    with allure.step("[END] test_success_checkout"):
        LOGGER.info("[END] test_success_checkout")

@allure.title("Test case 2: checkout with invalid value")
@allure.description("API: /order")
@pytest.mark.parametrize("receiver", receiver)
def test_failed_checkout(session, user_token, checkout_prime, receiver):

    with allure.step("[START] test_failed_checkout"):
        LOGGER.info("[START] test_failed_checkout")

    with allure.step("[ACTION] Get prime from web from page"):
        LOGGER.info(f"[DATA] prime: {checkout_prime}")

    with allure.step("[VERIFICATION] Check product number"):
        if receiver["list"] == "1 item":
            with allure.step("[ACTION] Get product info from Database"):
                product_sql = Product()
                product = product_sql.get_product_for_checkout()
                product_count = len(product)
        else:
            with allure.step("[ACTION] Get empty product list"):
                product = {}
                product_count = len(product)

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Call order API to create an order"):
        api_order_res = order_api.create_order(checkout_prime, receiver, product, product_count, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == 400
        LOGGER.info("[VALIDATION] Create order API should responsed status code 200")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == receiver["Alert Msg"]
        LOGGER.info("[VALIDATION] Create order API should responsed order id")

    with allure.step("[END] test_failed_checkout"):
        LOGGER.info("[END] test_failed_checkout")

@allure.title("Test case 3: checkout failed with invalid user_token")
@allure.description("API: /order")
def test_success_checkout(session, user_token, checkout_prime):

    with allure.step("[START] test_success_checkout"):
        LOGGER.info("[START] test_success_checkout")

    with allure.step("[ACTION] Get prime from web from page"):
        LOGGER.info(f"[DATA] prime: {checkout_prime}")

    with allure.step("[ACTION] Get product info from Database"):
        product_sql = Product()
        product = product_sql.get_product_for_checkout()
        product_count = len(product)

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Get receiver data"):
        receiver = order_api.get_receiver_data()

    with allure.step("[ACTION] Call order API to create an order"):
        api_order_res = order_api.create_order(checkout_prime, receiver, product, product_count, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == 200
        LOGGER.info("[VALIDATION] Create order API should responsed status code 200")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["data"]["number"] is not None
        LOGGER.info("[VALIDATION] Create order API should responsed order id")

    with allure.step("[END] test_success_checkout"):
        LOGGER.info("[END] test_success_checkout")