import requests

url = "http://127.0.0.1:8000/tasks"
headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3RfdXNlciIsImV4cCI6MTczMjc5OTA5MX0._PQmllx82cUiwJUiesxx3wfs22KPGV8-zKFG6hvvpeU"
}

response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.json())
