from api_objects.api_utils import *

class Logout(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def logout(self, url, header):
        response = self.post_request(url, headers = header)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response