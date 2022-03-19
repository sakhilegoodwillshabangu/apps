import requests
params = {"email":"goodwillsakhileshabangu@gmail.com", "password":"maria2468"}
response = requests.get("http://localhost:8080/gateway/logon/", params = params)
print(response.text)