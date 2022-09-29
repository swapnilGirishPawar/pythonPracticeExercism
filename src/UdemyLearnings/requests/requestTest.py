import requests


params = {"#q": "Pizza"}
r = requests.get("https://google.com", params=params)
print("Status:", r.status_code)
print(r.url)
# print(r.text)
