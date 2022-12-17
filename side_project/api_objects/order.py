from api_objects.api_utils import *

class Order(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def create_order(self, prime, receiver, product, product_count, header):
        url = self.basic_url + "api/1.0/order"
        data = self.get_checkout_data(prime, receiver, product, product_count)
        response = self.send_request("POST", url, body = data, headers = header)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response

    def get_checkout_data(self, prime, receiver, product, product_count):
        if product_count is not 0:
            list = [{
                  "id": product["id"],
                  "name": product["name"],
                  "qty": product["qty"],
                  "price": product["price"],
                  "size": product["size"],
                  "image": product["image"],
                    "color": {
                        "code": product["color"]["code"],
                        "name": product["color"]["name"]
                  }
                }]
        else:
            list = []

        data = {
            "prime": prime,
            "order": {
                "payment": "credit_card",
                "shipping": "delivery",
                "freight": 30,
                "subtotal": receiver["Subtotal"],
                "total": receiver["Total"],
                "recipient": {
                    "name": receiver["Receiver"],
                    "phone": receiver["Mobile"],
                    "email": receiver["Email"],
                    "address": receiver["Address"],
                    "time": receiver["Deliver Time"]
                },
                "list": list
            }
        }
        LOGGER.info(f"[DATA] Checkout data: {data}")

        return data


    def get_receiver_data(self):
        receiver = {
            "Receiver": "Chan Tai Man",
            "Mobile": "0912345678",
            "Email": "abc@abc.com",
            "Address": "台北市中山區 xxxxx",
            "Deliver Time": "anytime",
            "Subtotal": 799,
            "Total": 829
        }
        LOGGER.info(f"[DATA] Receiver data: {receiver}")

        return receiver