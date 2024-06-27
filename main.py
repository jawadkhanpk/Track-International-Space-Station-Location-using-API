import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)
response.raise_for_status()

data = response.json()
print(data)

latitude = str(data["iss_position"]["latitude"])
longitude = str(data["iss_position"]["longitude"])

iss_position = latitude +","+ longitude

url = "https://maps.google.com/maps?&daddr="

google_map_link = url + iss_position
print(google_map_link)