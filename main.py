import requests
from datetime import datetime

Pixela_endpoint = "https://pixe.la/v1/users"

token = "vdv235e6e654v5e"
username = "lolahell22"
id = "jjddjjdjbe"

user_params = {
    "token": token,
    "username": username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

user = requests.post(url=Pixela_endpoint, json=user_params)
# print(user.text)

graph = f"{Pixela_endpoint}/{username}/graphs"

graph_params = {
    "id": id,
    "name": "codingtracker",
    "unit": "hours",
    "type": "float",
    "color": "momiji"
}

header = {
    "X-USER-TOKEN": token
}

# response = requests.post(url=graph, json=graph_params, headers=header)
# print(response.text)

post_pixel = f"{Pixela_endpoint}/{username}/graphs/{id}"

today = datetime.now()

pixel_params = {
    "date": today.strftime("20231024"),
    "quantity": "1"
}

# pixel_response = requests.post(url=post_pixel, json=pixel_params, headers=header)

pixel_update = f"{Pixela_endpoint}/{username}/graphs/{id}/{today.strftime('%Y%m%d')}"

update_pixel_params = {
    "quantity": "2",

}

# update_response = requests.put(url=pixel_update, json=update_pixel_params, headers=header)

delete_pixel = f"{Pixela_endpoint}/{username}/graphs/{id}/{today.strftime('%Y%m%d')}"

delete_response = requests.delete(url=delete_pixel, headers=header)
print(delete_response.text)