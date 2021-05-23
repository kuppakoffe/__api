import requests

BASEURL = "http://localhost:8000"


response = requests.put(
    "{}/{}".format(BASEURL, "/video/123"),
    json={"name": "Random", "likes": 10, "views": 100},
)

print(response.status_code)

# Fetching the same from response
response = requests.get("{}/{}".format(BASEURL, "/video/1234"))
print(response.text)


