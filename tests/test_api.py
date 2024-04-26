from unittest.mock import patch

import aiohttp
import pytest
import requests
from aiohttp.test_utils import make_mocked_coro

from trash_nothing.src.api import fetch_data


@pytest.mark.asyncio
async def test_fetch_data_success(mock_server):
    # simulate server
    server = await mock_server

    # assumed params for fetch_data
    endpoint = str(server.make_url("/"))
    params = {"param": "value"}
    page = 3

    # call function with the mock server
    response = await fetch_data(endpoint, params, page)

    # check results
    assert response == {"message": "Hello", "page": "3"}


@pytest.mark.asyncio
async def test_fetch_data_error(mock_server):
    # simulate server
    server = await mock_server

    # assumed params for fetch_data
    endpoint = str(server.make_url("/error"))
    params = {"param": "value"}
    page = 3

    # check for error
    with pytest.raises(aiohttp.ClientResponseError):
        await fetch_data(endpoint, params, page)
