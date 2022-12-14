from api_objects.api_utils import *

class Logout(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def logout(self, header):
        url = self.basic_url + "api/1.0/user/logout"
        response = self.send_request("POST", url, headers = header)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response