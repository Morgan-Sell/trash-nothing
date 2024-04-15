from typing import Any, Dict, List, Union
from dotenv import load_dotenv
import os

# obtain API key from .env file
load_dotenv()
username = os.getenv("AUTH_USERNAME")
password = os.getenv("AUTH_PASSWORD")

# type aliases
JSONType = Union[Dict[str, Any], List[Any]]


# API configuraiton
API_URL = "https://whiskyhunter.net/api/auctions_data"
API_HEADERS = {
    "username": username,
    "password": password,
}
API_PARAMS = {
    "limit": 1,
}


# Output file configuration
CSV_OUTPUT_PATH = "data/auctions.csv"