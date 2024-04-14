import requests
from config import API_ROOT_URL, API_PARAMS

response = requests.get(url=API_ROOT_URL, params=API_PARAMS)
print(response.status_code)