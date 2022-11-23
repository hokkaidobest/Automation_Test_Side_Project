import requests

from api_objects.api_utils import *

class GetAllProduct(ApiUtils):
    def __init__(self):
        super().__init__(self.basic_url)

    def get_all_product(self):
        i = 0
        count = 0

        for i in range(3):
            self.url = f"{self.basic_url}products/all?paging={i}"
            result = requests.get(self.url)
            count = count + len(result.json()["data"])
            i + 1

        return count