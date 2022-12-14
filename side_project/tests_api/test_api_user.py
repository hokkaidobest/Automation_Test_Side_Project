import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

import pytest

from api_objects.login import Login
from api_objects.logout import Logout
from api_objects.profile import Profile
from sql_objects.user import User
from test_data.get_data_from_excel import GetTestData

base_url = env["UAT_URL"]

get_data = GetTestData()
success_login_data = get_data.get_success_login_data()
failed_login_data = get_data.get_failed_login_data()
failed_logout_data = get_data.get_failed_logout_data()

# Test case 1：login success
# Test API: user/login
@pytest.mark.parametrize('success_login_data', success_login_data)
def test_success_login(session, success_login_data):

    LOGGER.info("[START] test_success_login")

    url = base_url + "api/1.0/user/login"
    login_api = Login(session)
    response = login_api.login(url, success_login_data)

    assert response.status_code == int(success_login_data["Http Status Code"])
    LOGGER.info("[VERIFICATION] The http status code should be 200")

    user_sql = User()
    db_token = user_sql.get_user_token_by_email(success_login_data["email"])
    assert db_token["access_token"] == response.json()["data"]["access_token"]
    LOGGER.info("[VERIFICATION] The token from API response and DB.user.access_token suold be same")

    LOGGER.info("[END] test_success_login")

# Test case 2 : login failed
# Test API: user/login
@pytest.mark.parametrize('failed_login_data', failed_login_data)
def test_failed_login(session, failed_login_data):

    LOGGER.info("[START] test_failed_login")

    url = base_url + "api/1.0/user/login"
    login_api = Login(session)
    response = login_api.login(url, failed_login_data)

    assert response.status_code == int(failed_login_data["Http Status Code"])
    LOGGER.info("[VERIFICATION] The http status code should be 400")

    assert response.json()["errorMsg"] == failed_login_data["Error Msg"]
    LOGGER.info("[VERIFICATION] The error message should be responded")

    LOGGER.info("[END] test_failed_login")

# Test case 3 : logout success
# Test API: user/logout
@pytest.mark.parametrize('success_login_data', success_login_data)
def test_success_logout(session, success_login_data):
    
    LOGGER.info("[START] test_success_logout")

    login_url = base_url + "api/1.0/user/login"
    login_api = Login(session)
    response = login_api.login(login_url, success_login_data)

    logout_url = base_url + "api/1.0/user/logout"
    logout_api = Logout(session)
    header = {'authorization': f"Bearer {response.json()['data']['access_token']}"}
    response = logout_api.logout(logout_url, header)

    assert response.status_code == 200
    LOGGER.info("[VERIFICATION] The http status code should be 200")

    user_sql = User()
    db_token = user_sql.get_user_token_by_email(success_login_data["email"])
    assert db_token["access_token"] == ""
    LOGGER.info("[VERIFICATION] The token should be empty in the user table")

    LOGGER.info("[END] test_success_logout")

# Test case 4 : logout failed
# Test API: user/logout
@pytest.mark.parametrize('failed_logout_data', failed_logout_data)
def test_failed_logout(session, failed_logout_data):
    
    LOGGER.info("[START] test_failed_logout")

    logout_url = base_url + "api/1.0/user/logout"
    logout_api = Logout(session)
    header = {'authorization': f"{failed_logout_data['Token']}"}
    response = logout_api.logout(logout_url, header)

    assert response.status_code == int(failed_logout_data["Http Status Code"])
    LOGGER.info("[VERIFICATION] The http status code should be 401 or 403")

    assert response.json()["errorMsg"] == failed_logout_data["Error Msg"]
    LOGGER.info("[VERIFICATION] The error message should be responded")

    LOGGER.info("[END] test_failed_logout")

# Test case 5：Get profile success
# Test API: user/profile
@pytest.mark.parametrize('success_login_data', success_login_data)
def test_get_profile_success(session, success_login_data):
    
    LOGGER.info("[START] test_get_profile_success")

    login_url = base_url + "api/1.0/user/login"
    login_api = Login(session)
    login_response = login_api.login(login_url, success_login_data)

    profile_url = base_url + "api/1.0/user/profile"
    logout_api = Profile(session)
    header = {'authorization': f"Bearer {login_response.json()['data']['access_token']}"}
    profile_response = logout_api.get_profile(profile_url, header)

    assert profile_response.status_code == 200
    LOGGER.info("[VERIFICATION] The http status code should be 200")

    user_sql = User()
    db_data = user_sql.get_user_info_by_id(login_response.json()["data"]["user"]["id"])
    assert profile_response.json()["data"]["email"] == db_data["email"]
    assert profile_response.json()["data"]["name"] == db_data["name"]
    assert profile_response.json()["data"]["provider"] == db_data["provider"]
    assert profile_response.json()["data"]["picture"] == db_data["picture"]
    LOGGER.info("[VERIFICATION] The profile response data should be same to user table data")

    LOGGER.info("[END] test_get_profile_success")

# Test case 6：Get profile failed
# Test API: user/profile
@pytest.mark.parametrize('failed_logout_data', failed_logout_data)
def test_get_profile_failed(session, failed_logout_data):
    
    LOGGER.info("[START] test_get_profile_failed")

    logout_url = base_url + "api/1.0/user/profile"
    logout_api = Profile(session)
    header = {'authorization': f"{failed_logout_data['Token']}"}
    response = logout_api.get_profile(logout_url, header)

    assert response.status_code == int(failed_logout_data["Http Status Code"])
    LOGGER.info("[VERIFICATION] The http status code should be 401 or 403")

    assert response.json()["errorMsg"] == failed_logout_data["Error Msg"]
    LOGGER.info("[VERIFICATION] The error message should be responded")

    LOGGER.info("[END] test_get_profile_failed")