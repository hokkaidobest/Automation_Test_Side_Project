import pytest, requests, allure

from api_objects.login import Login

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

@pytest.fixture()
def session():
    session = requests.Session()
    
    yield session
    
    session.close()

@pytest.fixture()
def user_token(session):
    
    with allure.step("[START] user login"):
        login_data = {
            "provider": "native",
            "email": env["UAT_ACCOUNT"],
            "password": env["UAT_PASSWORD"]
        }
        LOGGER.info(f"[DATA] User login data: {login_data}")

    with allure.step("[ACTION] Init the Login API object"):
        login_api = Login(session)
    
    with allure.step("[ACTION] Do user login"):
        response = login_api.login(login_data)
        LOGGER.info(f"[DATA] User login API response: {response.json()}")

    with allure.step("[ACTION] Verify login API response code"):
        assert response.status_code == 200
        LOGGER.info("[VERIFICATION] The http status code should be 200")

    with allure.step("[ACTION] Organize user token"):
        header = {"authorization": f"Bearer {response.json()['data']['access_token']}"}
        LOGGER.info(f"[DATA] User token is: {header}")
    
    return header