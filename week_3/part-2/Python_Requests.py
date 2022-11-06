import requests

url = "https://fakerestapi.azurewebsites.net/api/v1/Activities"

res = requests.get(url)

#  Verify the response status code is 200
response_code = res.status_code
assert response_code == 200, "The API HTTPS code is not equal to 200."


# List out all the activity ids which are not completed.
datas = res.json()
result = []

for data in datas:
    if data['completed'] != True:
        result.append(data['id'])
    
print(f"The list of activity ids are not completed {result}.")