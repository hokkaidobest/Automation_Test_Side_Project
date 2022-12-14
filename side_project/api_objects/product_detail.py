from api_objects.api_utils import *

class ProductDetail(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def get_product_detail_by_id(self, id):
        url = self.basic_url + f"api/1.0/products/details?id={id}"
        response = self.get_request(url)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response