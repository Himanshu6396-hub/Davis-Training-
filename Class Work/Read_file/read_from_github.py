import requests

url = "https://raw.githubusercontent.com/Himanshu6396-hub/Davis-Training-/main/Class%20Work/Numpy/operation.py"

response = requests.get(url)
data = response.text

print(data)
