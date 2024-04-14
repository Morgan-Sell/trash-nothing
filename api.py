import requests
from requests.exceptions import HTTPError
from config import JSONType


def fetch_data(endpoint: str, params: dict) -> JSONType:
    response = requests.get(url=endpoint, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPError(
            f"Error fetching data: {response.status_code} - {response.reason}"
        )
