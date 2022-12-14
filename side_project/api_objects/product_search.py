from api_objects.api_utils import *

class ProductSearch(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def get_product_by_keyword(self, keyword, paging):
        url = self.basic_url + f"api/1.0/products/search?keyword={keyword}&paging={paging}"
        response = self.get_request(url)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response