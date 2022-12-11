from api_objects.api_utils import *

class ProductCategory(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def get_product_by_category(self, url):
        response = self.get_resuest(url)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response