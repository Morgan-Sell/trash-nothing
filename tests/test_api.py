import pytest
import requests

from api import fetch_data


def test_fetch_data_success(requests_mock):
    # mock a successful API response
    test_url = "https://fake.url.api.com/data"
    expected_response_data = {"key": "value"}
    requests_mock.get(test_url, json=expected_response_data, status_code=200)

    # call fetch_data function
    test_params = {"param1": "value1"}
    response = fetch_data(test_url, test_params)

    # test
    assert response == expected_response_data


def test_fetch_data_error(requests_mock):
    # mock an API response with an error
    test_url = "https://fake.url.api.com/data"
    requests_mock.get(test_url, status_code=500)

    with pytest.raises(requests.HTTPError):
        fetch_data(test_url, {})
