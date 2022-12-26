import requests
from datetime import datetime

USERNAME = 'jasonlim9'
TOKEN = 'abc123abc123abc123'
GRAPH_ID = 'graph1'

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}

## POST
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": GRAPH_ID,
  "name": "Jogging Graph",
  "unit": "Km",
  "type": "float",
  "color": "ajisai"
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixela_data = {
  "date": today.strftime("%Y%m%d"),
  "quantity": input("How many kilometers did you joggnig today? "),
}

response = requests.post(url=pixela_creation_endpoint,
                         json=pixela_data,
                         headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {"quantity": "7"}

## PUT
# response = requests.put(url=update_endpoint, json=pixela_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

## DELETE
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

# https://pixe.la/v1/users/jasonlim9/graphs/graph1.html
