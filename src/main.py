import asyncio

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

async def main():
    # pull data from API
    posts = []

    for _ in range(3):
        await asyncio.sleep(1)
        task = fetch_data(API_URL, API_PARAMS, API_HEADERS)
        posts.append(task)
        API_PARAMS["page"] += 1
    print()
    results = await asyncio.gather(*posts, return_exceptions=True)
    pprint(results)
    print(len(results[0]["posts"]))
    for result in results[0]["posts"]:
        if isinstance(result, Exception):
            print(result)
        
        else:        
            # transform JSON to dataclas
            auction = convert_json_to_trash_nothing_post(result)

            # create csv w/ headers if csv does not exist
            initialize_csv_with_headers(CSV_OUTPUT_PATH, auction.keys())

            # append new data to CSV
            append_data_to_csv(CSV_OUTPUT_PATH, auction)
        

if __name__ == "__main__":
    asyncio.run(main())
