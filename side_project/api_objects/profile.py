from api_objects.api_utils import *

class Profile(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def get_profile(self,header):
        url = self.basic_url + "api/1.0/user/profile"
        response = self.get_request(url, headers = header)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response