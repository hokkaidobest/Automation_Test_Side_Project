import requests

class Get:
    def __init__(self):
        self.basic_url = "http://54.201.140.239/api/1.0/"
        self.paging = 0

    def get_search_with_keyword(self, keyword):
        self.url = f"{self.basic_url}products/search?keyword={keyword}&paging={self.paging}"

        result = requests.get(self.url)

        return len(result.json()["data"])

    def get_products_count_without_keyword(self):
        i = 0
        count = 0

        for i in range(3):
            self.url = f"{self.basic_url}products/all?paging={i}"
            result = requests.get(self.url)
            count = count + len(result.json()["data"])
            i + 1

        return count