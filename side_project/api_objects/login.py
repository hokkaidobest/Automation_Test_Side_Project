from api_objects.api_utils import *

class Login(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def login(self, url, data):
        response = self.post_request(url, body = data)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response