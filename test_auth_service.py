import requests

url = "http://localhost:8000/api/register/"  # ⚠️ Check spelling!
data = {
    "username": "dhanashree",
    "password": "pass123"
}

res = requests.post(url, json=data)

print("Status Code:", res.status_code)
print("Raw Response Text:")
print(res.text)  # ← Show raw HTML/text response
