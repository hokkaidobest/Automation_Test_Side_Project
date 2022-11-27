import logging
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

from os import environ as env
from dotenv import load_dotenv
load_dotenv()

from sql_objects.user import User
from page_objects.member_page import MemberPage

# Test case 1 : Login and Logout Success
# When member login with correct email and password
# Then login success and there is jwt token in local storage
# When member logout
# Then logout success
def test_login_and_logout_success(member_broswer):
    
    LOGGER.info("[START] test_login_and_logout_success")
    
    user_token = member_broswer.get_user_jwt_token()
    LOGGER.info(f"[UI] Get user cookie from broswer: {user_token}")

    email = env["UAT_ACCOUNT"]
    user_sql = User()
    db_token = user_sql.get_user_token_by_email(email)
    LOGGER.info(f"[DATA] Get user cookie from database: {db_token}")

    assert db_token == user_token
    LOGGER.info("[VERIFICATION] Compare token pass")

    member_broswer.log_out()
    LOGGER.info("[ACTION] Log out successfully")

    assert member_broswer.alert_is_present().text == "Logout Success"
    LOGGER.info("[VERIFICATION] Log out successfully")

    member_broswer.alert_is_present().accept()
    LOGGER.info("[ACTION] Click confirm btn")
    LOGGER.info("[PAGE] Switch to login page")
    LOGGER.info("[END] test_login_and_logout_success")

# Test case 2 : Login Failed with incorrect email or password
# When member login with incorrect email / password
# Then login failed with error message
def test_login_failed(main_broswer):
    LOGGER.info("[START] test_login_and_logout_success")
    
    email = env["UAT_INCORRECT_ACCOUNT"]
    password = env["UAT_INCORRECT_PASSWORD"]

    member_page = MemberPage(main_broswer)
    member_page.click_profile_btn()
    LOGGER.info("[PAGE] Switch to login page")

    member_page.log_in(email, password)
    LOGGER.info(f"[ACTION] Log in as {email}")

    assert member_page.alert_is_present().text == "Login Failed"
    LOGGER.info("[VERIFICATION] Log in failed")

    member_page.alert_is_present().accept()
    LOGGER.info("[ACTION] Click confirm btn")
    LOGGER.info("[END] test_login_and_logout_success")

# Test case 3 : Login with invalid access token
# Given member login with correct email and password
# And login success and copy the jwt token
# And member logout
# And logout success
# When using the jwt token to access member page
# Then error message "Invalid Token"
def test_login_with_invalid_access_token(member_broswer):
    
    LOGGER.info("[START] test_login_with_invalid_access_token")
    
    user_token = member_broswer.get_user_jwt_token()
    LOGGER.info(f"[UI] Get user cookie from broswer: {user_token}")

    email = env["UAT_ACCOUNT"]
    user_sql = User()
    db_token = user_sql.get_user_token_by_email(email)
    LOGGER.info(f"[DATA] Get user cookie from database: {db_token}")

    assert db_token == user_token
    LOGGER.info("[VERIFICATION] Compare token pass")

    member_broswer.log_out()
    LOGGER.info("[ACTION] Log out successfully")

    assert member_broswer.alert_is_present().text == "Logout Success"
    LOGGER.info("[VERIFICATION] Log out successfully")

    member_broswer.alert_is_present().accept()
    LOGGER.info("[ACTION] Click confirm btn")
    LOGGER.info("[PAGE] Switch to login page")

    member_broswer.set_user_jwt_token(user_token)
    LOGGER.info("[ACTION] Set user jwt token")

    member_broswer.load_page("profile.html")
    assert member_broswer.alert_is_present().text == "Invalid Access Token"
    LOGGER.info("[VERIFICATION] Token invalid")

    LOGGER.info("[END] test_login_with_invalid_access_token")