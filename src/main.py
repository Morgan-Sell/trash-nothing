from config import (
    API_URL, API_PARAMS, API_HEADERS, CSV_OUTPUT_PATH
)
from api import fetch_data
from data_processing import (
    convert_json_to_trash_nothing_post,
    initialize_csv_with_headers,
    append_data_to_csv,
)

from pprint import pprint

def main():
    # pull data from API
    data = fetch_data(API_URL, API_PARAMS, API_HEADERS)

    # for i in range(3):
    pprint(data["posts"][0])

    # transform JSON to dataclas
    auction = convert_json_to_trash_nothing_post(data["posts"][0])

    # create csv w/ headers if csv does not exist
    initialize_csv_with_headers(CSV_OUTPUT_PATH, auction.keys())

    # append new data to CSV
    append_data_to_csv(CSV_OUTPUT_PATH, auction)
    

if __name__ == "__main__":
    main()
