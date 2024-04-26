from unittest.mock import patch
import pytest
import requests
import aiohttp
from aiohttp.test_utils import make_mocked_coro

from trash_nothing.src.api import fetch_data


@pytest.mark.asyncio
async def test_fetch_data_success(mock_server):
    server = await mock_server
    endpoint = str(server.make_url("/"))
    params = {"param": "value"}
    page = 3

    # call function with the mock server
    response = await fetch_data(endpoint, params, page)

    # check results
    assert response == {"message": "Hello", "page": "3"}


# @pytest.mark.asyncio
# async def test_fetch_data_http_error(mock_response):
#     # given params
#     endpoint = "http://example.com/api"
#     params = {"query": "error"}
#     page = 33
#     error_status = 404

#     # mock session and response setup
#     response = mock_response(status=error_status, json_body={"error": "not found"})
#     with patch("aiohttp.ClientSession.get", return_value=response), pytest.raises(aiohttp.ClientResponseError) as excinfo:
#         await fetch_data(endpoint, params, page)

        # test results
        # assert excinfo.value.status == 404