from api_objects.api_utils import *

class Login(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def login(self, data):
        url = self.basic_url + "api/1.0/user/login"
        response = self.send_request("POST", url, body = data)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response