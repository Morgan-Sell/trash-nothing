from typing import Any, Dict, List, Union


# type aliases
JSONType = Union[Dict[str, Any], List[Any]]


# API configuraiton
API_URL = "https://itunes.apple.com/search"
API_PARAMS = {
    "term": "jurrasic5",
    "country": "us",
    "limit": 1,
}

# This defines a type alias that can be a Dict or a List, which are the typical structures of JSON data
