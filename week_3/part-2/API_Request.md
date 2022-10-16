# Week 3 Part 2 (Deadline: 2022/11/06 23:59)

## Online Learning Material
* [RESTful API Testing with Postman](https://www.udemy.com/course/restful-api-testing-with-postman/learn/lecture/6075726#overview)
* [Python Dictionary and JSON](https://medium.com/analytics-vidhya/python-dictionary-and-json-a-comprehensive-guide-ceed58a3e2ed)
* [Python Requests](https://www.youtube.com/playlist?list=PLJ1odve0o6dX5ndJ5lwiCOR58ycB1rcrV)
* [curl](https://blog.techbridge.cc/2019/02/01/linux-curl-command-tutorial/)

## Assignment 1: Python Requests

According to the [API Documents](https://fakerestapi.azurewebsites.net/index.html), please write a python script to make the API call to get all the activities, and 
Using Assertion to verify that the response status code is 200

List out all the activity ids which are not completed.

## Assignment 2: Python Requests - Cookies, Sessions

Write a python script to book a room on the website (https://automationintesting.online/). Please follow the below instructions:

1. Login to get a token by doing a POST call against the auth API at https://automationintesting.online/auth/login. The request body should be like that:
```json
{
  "username": "admin",
  "password": "password"
}
```
2. Get a list of rooms by doing a GET call against the getting rooms API at https://automationintesting.online/room/. 
Extract the room ID of the first room.
3. Make a booking for the room by doing a POST call against the booking API at https://automationintesting.online/booking. It also requested to send your token as a cookie. The request body should be like that: (Change the data as you like)
```json
{
  "bookingdates": {
    "checkin": string with datetime format (YYYY-MM-HHThh:mm:ss.fZ),
    "checkout": string with datetime format (YYYY-MM-HHThh:mm:ss.fZ),
  },
  "depositpaid": boolean,
  "firstname": string
  "lastname": string
  "roomid": string
  "totalprice": integer
}
```
4. Verify that your booking is successful by checking the response status code.
5. Assert the response booking information is correct.

## Assignment 4: Algorithm Practice
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

```python
def single_number(nums):
    # your code here

print(single_number([2, 2, 1])) # Should be 1
print(single_number([4, 1, 2, 1, 2])) # Should be 4
print(single_number([1])) # Should be 1
```
