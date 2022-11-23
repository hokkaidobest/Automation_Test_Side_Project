import requests

from api_objects.api_utils import *

class GetProductWithCatrgory(ApiUtils):
    def __init__(self):
        super().__init__(self.basic_url)
        self.paging = 0

    def get_products_with_category(self, category):
        self.url = f"{self.basic_url}products/{category}?paging={self.paging}"

        result = []
        response = requests.get(self.url)
        for data in response.json()["data"]:
            result.append(data["title"])
        # count = len(result.json()["data"])

        if "next_paging" in response.json():
            self.url = f"{self.basic_url}products/{category}?paging={response.json()['next_paging']}"
            for data in response.json()["data"]:
                result.append(data["title"])

        return result