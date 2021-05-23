import requests

BASEURL = "http://localhost:8000"


response = requests.post(
    "{}/{}".format(BASEURL, "/api/videos"),
    json={"name": "Random", "likes": 10, "views": 100},
)

print(response.status_code)

# Fetching the same from response
# response = requests.get("{}/{}".format(BASEURL, "/api/video/1"))
# print(response.text)

# Listing all resources
# response = requests.get("{}/{}".format(BASEURL, "/api/videos"))
# print(response.json())
