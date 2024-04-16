import csv
import os
from tempfile import NamedTemporaryFile, TemporaryDirectory
import pytest

from whiskey_auction.src.data_processing import (
    append_data_to_csv,
    initialize_csv_with_headers,
    # convert_json_to_auction,
)

from .conftest import MockAuction


def test_initialize_csv_with_headers_crates_file():
    with TemporaryDirectory() as tmp_directory:
        # define the path and headers
        file_path = os.path.join(tmp_directory, "test.csv")
        headers = ["var_A", "var_B", "var_C"]

        # call the function
        initialize_csv_with_headers(file_path, headers)

        # confirm the file has ben created
        assert os.path.exists(file_path)

        # confirm that file has the correct headers
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            read_headers = next(reader)
            assert read_headers == headers


def test_initialize_csv_does_not_overwrite_existing_file():
    with TemporaryDirectory() as tmp_directory:
        # define the path and headers
        file_path = os.path.join(tmp_directory, "test.csv")
        headers = ["var_A", "var_B", "var_C"]
        initial_data = ["xx", "yy", "zz"]

        # create an initial file with different content
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(initial_data)
        
        # call the function
        initialize_csv_with_headers(file_path, headers)

        # confirm that initial_data is still there
        with open(file_path, mode="r", newline="") as file:
            reader = csv.reader(file)
            data = next(reader)
            assert data == initial_data


def test_append_data_csv():
    with NamedTemporaryFile(mode="w+", delete=False) as tmp:
        # initialize auction data
        auction1 = MockAuction("Oaxacan Mezcal", "2024-01-01", 345.67)
        auction2 = MockAuction("Argentine Malbec", "2010-10-31", 3890.12)

        # append data to temporary csv file
        append_data_to_csv(tmp.name, auction1)
        append_data_to_csv(tmp.name, auction2)

        # read data
        tmp.seek(0)
        lines = tmp.readlines()
        
        # check expected results
        assert lines[0].strip() == "Oaxacan Mezcal,2024-01-01,345.67"
        assert lines[1].strip() == "Argentine Malbec,2010-10-31,3890.12"


def test_convert_json_to_auction(sample_whiskey_api_data):
    # call the function
    auction = convert_json_to_auction(sample_whiskey_api_data)

    expected_results = Action(
        name="Australian Whisky Auctions",
        date="2024-03-01",
        winning_bid_max=5167.3,
        winning_bid_min=11.9,
        winning_bid_mean=204.82,
        trading_volume=259096.9,
        lots_count=1265,
    )

    # check expected results
    assert auction == expected_results