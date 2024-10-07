import requests
url = "http://127.0.0.1:8080/api/deleteCode/AB01"
res = requests.delete(url)
print(f"status:{res.status_code}")
print(f"text:{res.text}")