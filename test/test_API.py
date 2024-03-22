import requests
import json
localhost = "http://127.0.0.1:8000"
response = requests.get(localhost+"/api/user/profile/")


print(response.status_code)
print(response.content)
t1=json.loads(response.content)
print(t1)