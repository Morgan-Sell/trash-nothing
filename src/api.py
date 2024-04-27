import asyncio

import aiohttp
from requests.exceptions import HTTPError

from config import JSONType


async def fetch_data(endpoint: str, params: dict, page: int) -> JSONType:
    """
    Asynchronously fetches data from a specified endpoint with given parameters.

    This function initializes an asynchronous HTTP session and sends a GET request to
    the provided endpoint. It includes support for pagination through the 'page' parameter.
    It returns the JSON response if the HTTP status code is 200.

    Parameters:
    - endpoint (str): The URL of the API endpoint to send the request to.
    - params (dict): A dictionary of parameters to be passed with the request.
    - page (int): The page number to be requested, used for pagination.

    Returns:
    - JSONType: A JSON object containing the response data if the request is successful.

    Raises:
    - ClientResponseError: If the response status is not 200, the function will
      raise an exception with the response's error status and message.

    """
    params["page"] = page
    async with aiohttp.ClientSession() as session:
        async with session.get(endpoint, params=params) as response:
            if response.status == 200:
                return await response.json()
            else:
                response.raise_for_status()
