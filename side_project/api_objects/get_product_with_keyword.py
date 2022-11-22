import requests

from api_objects.api_utils import *

class GetProductWithKeyword(ApiUtils):
    def __init__(self):
        super().__init__(self.basic_url)
        self.paging = 0

    def get_product_with_keyword(self, keyword):
        self.url = f"{self.basic_url}products/search?keyword={keyword}&paging={self.paging}"

        result = requests.get(self.url)

        return len(result.json()["data"])