import requests

class Booking:
    def __init__(self):
        self.basic_url = "https://automationintesting.online/"
        self.request = requests.Session()

    def get_user_token(self, username, password):
        self.login_url = f"{self.basic_url}auth/login"
        self.login_data = {
            "username": username,
            "password": password
        }

        return self.post(self.login_url, self.login_data)

    def get_avaliable_room(self):
        self.room_url = f"{self.basic_url}room/"

        return self.get(self.room_url)

    def add_a_new_booking(self, booking_data):
        self.booking_url = f"{self.basic_url}booking/"
        self.booking_data = booking_data

        return self.post(self.booking_url, self.booking_data)

    def compare_request_and_response_data(self, request, response):
        return request == response

    def post(self, url, data = None):
        return self.request.post(url, json = data)

    def get(self, url, data = None):
        return self.request.get(url, json = data)

init = Booking()

# Step 1 : Login to get a token
account = "admin"
password = "password"

token = init.get_user_token(account, password)
assert token.status_code == 200, "Get user info faild."

# Step 2 : Get a list of rooms
room = init.get_avaliable_room()
assert room.status_code == 200, "Get room info faild."

# Step 3 : Make a booking
booking_data = {
    "bookingdates": {
        "checkin": "2022-12-31",
        "checkout": "2023-01-01"
    },
    "depositpaid": True,
    "firstname": "Nathan",
    "lastname": "Tung",
    "roomid": 1111,
    "totalprice": 1000
}
booking_result = init.add_a_new_booking(booking_data)

# Step 4 : Verify that your booking
assert booking_result.status_code == 201, "Make a new booking faild."

# Step : Assert the response 
del booking_data['totalprice'] # This data does not respond via API.
result = booking_result.json()["booking"]
del result["bookingid"] # This data does not exist in the request.

comparation_result = init.compare_request_and_response_data(booking_data, result)

assert comparation_result == True, "Request and response are not the same; please confirm with customer service."