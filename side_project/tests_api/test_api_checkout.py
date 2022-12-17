import logging, pytest
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from tests_web.conftest import *
from api_objects.order import Order
from sql_objects.product import Product
from sql_objects.order import Order as SqlOrder

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
def test_failed_checkout_with_invalid_checkout_data(session, user_token, checkout_prime, receiver):

    with allure.step("[START] test_failed_checkout_with_invalid_checkout_data"):
        LOGGER.info("[START] test_failed_checkout_with_invalid_checkout_data")

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
        LOGGER.info("[VALIDATION] Create order API should responsed status code 400")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == receiver["Alert Msg"]
        LOGGER.info(f"[VALIDATION] Create order API should responsed {receiver['Alert Msg']}")

    with allure.step("[END] test_failed_checkout_with_invalid_checkout_data"):
        LOGGER.info("[END] test_failed_checkout_with_invalid_checkout_data")

@allure.title("Test case 3: checkout failed with invalid user_token")
@allure.description("API: /order")
@pytest.mark.parametrize(
        "user_token, error_code, error_message", 
        [("", 401, "Unauthorized"), 
        ({"authorization": "Bearer test"}, 403, "Forbidden")]
    )
def test_failed_checkout_with_invalied_token(session, user_token, error_code, error_message, checkout_prime):

    with allure.step("[START] test_failed_checkout_with_invalied_token"):
        LOGGER.info("[START] test_failed_checkout_with_invalied_token")

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
        assert api_order_res.status_code == error_code
        LOGGER.info(f"[VALIDATION] Create order API should responsed status code {error_code}")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == error_message
        LOGGER.info(f"[VALIDATION] Create order API should responsed: {error_message}")

    with allure.step("[END] test_failed_checkout_with_invalied_token"):
        LOGGER.info("[END] test_failed_checkout_with_invalied_token")

@allure.title("Test case 4: checkout failed with invalid prime")
@allure.description("API: /order")
@pytest.mark.parametrize(
        "checkout_prime, error_code, error_message", 
        [("test_pirme", 400, "Invalid prime")]
    )
def test_failed_checkout_with_invalied_prime(session, user_token, checkout_prime, error_code, error_message):

    with allure.step("[START] test_failed_checkout_with_invalied_prime"):
        LOGGER.info("[START] test_failed_checkout_with_invalied_prime")

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
        assert api_order_res.status_code == error_code
        LOGGER.info(f"[VALIDATION] Create order API should responsed status code {error_code}")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == error_message
        LOGGER.info(f"[VALIDATION] Create order API should responsed: {error_message}")

    with allure.step("[END] test_failed_checkout_with_invalied_prime"):
        LOGGER.info("[END] test_failed_checkout_with_invalied_prime")

@allure.title("Test case 5: get order successfully")
@allure.description("API: /order/order_id")
@pytest.mark.parametrize('order_number', ["1117614863313"])
def test_get_order_successfully(session, user_token, order_number):

    with allure.step("[START] test_get_order_successfully"):
        LOGGER.info("[START] test_get_order_successfully")

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Get order detail"):
        api_order_res = order_api.get_order(order_number, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == 200
        LOGGER.info("[VALIDATION] Get order API should responsed status code 200")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["data"] is not None
        LOGGER.info("[VALIDATION] Get order API should responsed order id")

    with allure.step("[ACTION] Get order info from Database"):
        order_sql = SqlOrder()
        order = order_sql.get_order_by_number(order_number)

    with allure.step("[VALIDATION] Compare number between API response and DB"):
        assert api_order_res.json()["data"]["number"] == order["number"]
        LOGGER.info("[VALIDATION] Compare number between API response and DB")

    with allure.step("[END] test_get_order_successfully"):
        LOGGER.info("[END] test_get_order_successfully")

@allure.title("Test case 6: get order failed")
@allure.description("API: /order/order_id")
@pytest.mark.parametrize(
        "order_number, error_code, error_message", 
        [("123456", 400, "Order Not Found."), 
        ("test", 500, "Internal Server Error")]
    )
def test_get_order_failed(session, user_token, order_number, error_code, error_message):

    with allure.step("[START] test_get_order_failed"):
        LOGGER.info("[START] test_get_order_failed")

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Get order detail"):
        api_order_res = order_api.get_order(order_number, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == error_code
        LOGGER.info(f"[VALIDATION] Get order API should responsed status code {error_code}")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == error_message
        LOGGER.info(f"[VALIDATION] Get order API should responsed error message {error_message}")

    with allure.step("[END] test_get_order_failed"):
        LOGGER.info("[END] test_get_order_failed")

@allure.title("Test case 7: get order failed with invalid token")
@allure.description("API: /order/order_id")
@pytest.mark.parametrize(
        "order_number, user_token, error_code, error_message", 
        [("1117614863313", "", 401, "Unauthorized"), 
        ("1117614863313", {"authorization": "Bearer test"}, 403, "Forbidden")]
    )
def test_get_order_failed_with_invalid_token(session, user_token, order_number, error_code, error_message):

    with allure.step("[START] test_get_order_failed_with_invalid_token"):
        LOGGER.info("[START] test_get_order_failed_with_invalid_token")

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Get order detail"):
        api_order_res = order_api.get_order(order_number, user_token)

    with allure.step("[VALIDATION] validate the API response code"):
        assert api_order_res.status_code == error_code
        LOGGER.info(f"[VALIDATION] Get order API should responsed status code {error_code}")

    with allure.step("[VALIDATION] validate the API response data"):
        assert api_order_res.json()["errorMsg"] == error_message
        LOGGER.info(f"[VALIDATION] Get order API should responsed error message {error_message}")

    with allure.step("[END] test_get_order_failed_with_invalid_token"):
        LOGGER.info("[END] test_get_order_failed_with_invalid_token")