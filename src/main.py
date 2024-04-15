from config import API_URL, API_PARAMS, API_HEADERS
from src.api import fetch_data
 


if __name__ == "__main__":
    print(fetch_data(API_URL, API_PARAMS, API_HEADERS))