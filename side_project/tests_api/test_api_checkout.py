import logging, pytest
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from tests_web.conftest import *
from api_objects.order import Order
from sql_objects.product import Product
from sql_objects.order import Order

# from test_data.get_data_from_excel import GetTestData
# get_data = GetTestData()
# success_login_data = get_data.get_success_login_data()
# failed_login_data = get_data.get_failed_login_data()
# failed_logout_data = get_data.get_failed_logout_data()

@allure.title("Test case 1: checkout successfully")
@allure.description("API: /order")
@pytest.mark.usefixtures("get_prime")
def test_success_checkout(session, get_prime):

    with allure.step("[START] test_success_checkout"):
        LOGGER.info("[START] test_success_checkout")

    with allure.step("[ACTION] Get prime from web from page"):
        LOGGER.info(f"[DATA] prime: {get_prime}")

    with allure.step("[ACTION] Get product info from Database"):
        product_sql = Product()
        product = product_sql.get_checkout_product() # 這邊要組的準備要送出的 list 內一樣
        LOGGER.info(f"[DATA] product: {product}")

    with allure.step("[ACTION] Init the Order API object"):
        order_api = Order(session)

    with allure.step("[ACTION] Call order API to create an order"):
        api_order_res = order_api.create_order(get_prime, product) # 組 request 打 post 出去
        assert api_order_res.status_code == 200
        LOGGER.info("[VALIDATION] Create order API should responsed status code 200")

    with allure.step("[ACTION] Verify order data via database"):
        order_sql = Order() 
        sql_order_res = order_sql.get_order_info(api_order_res.json()["id"]) # 根據 API response id 去 DB 撈
        assert api_order_res == sql_order_res # 嘿嘿，看這邊要怎麼比對了... 理想上應該是全部比對，因為這邊不會關聯太多
        LOGGER.info("[VALIDATION] The order data from API response and databse should be same")

    with allure.step("[END] test_success_checkout"):
        LOGGER.info("[END] test_success_checkout")

# Test case 2 : login failed
# Test API: user/login
# @pytest.mark.parametrize('failed_login_data', failed_login_data)
# def test_failed_login(session, failed_login_data):

#     LOGGER.info("[START] test_failed_login")

#     login_api = Login(session)
#     response = login_api.login(failed_login_data)

#     assert response.status_code == int(failed_login_data["Http Status Code"])
#     LOGGER.info("[VERIFICATION] The http status code should be 400")

#     assert response.json()["errorMsg"] == failed_login_data["Error Msg"]
#     LOGGER.info("[VERIFICATION] The error message should be responded")

#     LOGGER.info("[END] test_failed_login")