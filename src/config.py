from typing import Any, Dict, List, Union
from dotenv import load_dotenv
import os

# obtain API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# type aliases
JSONType = Union[Dict[str, Any], List[Any]]


# API configuraiton
API_URL = "https://trashnothing.com/api/v1.4/posts"
API_HEADERS = {

}
API_PARAMS = {
    "api_key": api_key,
    "sort_by": "date",
    "types": "offer",
    "sources": "trashnothing",
    "per_page": 20,
    "page": 1,
    "latitude": 38.90,
    "longitude": 77.0,
    "radius": 160934, # in meters, equals 100 miles
}


# Output file configuration
CSV_OUTPUT_PATH = "whiskey_auction/data/auctions.csv"
