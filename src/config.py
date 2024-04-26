import os
from pathlib import Path
from typing import Any, Dict, List, Union

from dotenv import load_dotenv

# obtain API key from .env file
load_dotenv()
api_key = os.getenv("API_KEY")

# type aliases
JSONType = Union[Dict[str, Any], List[Any]]

# directory configuration
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
IMG_DIR = BASE_DIR / "img"

# file configuration
CSV_OUTPUT_PATH = DATA_DIR / "trash_posts.csv"


# API configuraiton
API_URL = "https://trashnothing.com/api/v1.4/posts"
API_PARAMS = {
    "api_key": api_key,
    "sort_by": "date",
    "types": "offer",
    "sources": "groups",
    "group_ids": 4673,  # DC ReUseIt group
    "per_page": 20,
    "page": 1,
}
NUM_CALLS = 3

# Output file configuration

