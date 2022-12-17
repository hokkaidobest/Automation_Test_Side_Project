from api_objects.api_utils import *

class Order(ApiUtils):
    def __init__(self, session):
        super().__init__(session)

    def create_order(self, prime, receiver, product, header):
        url = self.basic_url + "api/1.0/order"
        data = self.get_checkout_data(prime, receiver, product)
        response = self.send_request("POST", url, body = data, headers = header)
        LOGGER.info(f"[TEST] API response: {response.json()}, code: {response.status_code}")

        return response

    def get_checkout_data(self, prime, receiver, product):
        data = {
            "prime": prime,
            "order": {
                "shipping": "delivery",
                "payment": "credit_card",
                "subtotal": product["qty"] * product["price"],
                "freight": 30,
                "total": product["qty"] * product["price"] + 30,
                "recipient": {
                    "name": receiver["name"],
                    "phone": receiver["phone"],
                    "email": receiver["email"],
                    "address": receiver["address"],
                    "time": receiver["time"]
                },
                "list": [{
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
            }
        }
        LOGGER.info(f"[DATA] Checkout data: {data}")

        return data


    def get_receiver_data(self):
        receiver = {
            "name": "Chan Tai Man",
            "phone": "0912345678",
            "email": "abc@abc.com",
            "address": "台北市中山區 xxxxx",
            "time": "anytime"
        }
        LOGGER.info(f"[DATA] Receiver data: {receiver}")

        return receiver