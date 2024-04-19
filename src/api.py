import requests
from requests.exceptions import HTTPError
from config import JSONType
import aiohttp
import asyncio



async def fetch_data(endpoint: str, params: dict, headers: dict = {}) -> JSONType:
    """
    Sends a GET request to a specified URL endpoint with optional parameters and headers,
    returns the response data as a JSON object.

    Parameters:
    - endpoint (str): The URL to which the GET request is sent.
    - params (dict): Parameters to be sent with the request.
    - headers (dict, optional): HTTP headers to send with the request. Default is an empty dictionary.

    Returns:
    - JSONType: A JSON object containing the response data.

    Raises:
    - HTTPError: If the response status is not 200, indicating the fetch was unsuccessful.
    """
    # response = requests.get(url=endpoint, params=params, headers=headers)
    # if response.status_code == 200:
    #     return response.json()
    # else:
    #     raise HTTPError(
    #         f"Error fetching data: {response.status_code} - {response.reason}"
    #     )
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint, params=params, headers=headers) as response:
            if response.status == 200:
                return await response.json()
            else:
                response.raise_for_status()