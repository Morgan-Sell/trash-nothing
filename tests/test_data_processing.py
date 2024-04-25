import csv
import os
from pprint import pprint
from tempfile import NamedTemporaryFile, TemporaryDirectory
import pytest

from trash_nothing.src.data_processing import (
    append_data_to_csv,
    initialize_csv_with_headers,
    convert_json_to_trash_nothing_post,
)
from trash_nothing.src.models import TrashNothingPost

from .conftest import MockTrashPost


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
        post1 = MockTrashPost(
            post_id=2,
            title="Half-empty Oaxacan Mezcal",
            description="Imported from the Oaxacan mountains. Drank half of it with my dad.", 
            post_date="2003-10-14T09:03:15",
        )
        post2 = MockTrashPost(
            post_id=68,
            title="Dog-chewed baseball glove",
            description="Wore the glove when making the winning catch for the little league world series.", 
            post_date="1999-12-25T18:37:25",
        )

        # append data to temporary csv file
        append_data_to_csv(tmp.name, post1)
        append_data_to_csv(tmp.name, post2)

        # read data
        tmp.seek(0)
        lines = tmp.readlines()
        pprint(lines)
        # check expected results
        assert lines[0].strip() == (
            "2,Half-empty Oaxacan Mezcal," \
            "Imported from the Oaxacan mountains. Drank half of it with my dad.," \
            "2003-10-14T09:03:15"
        )
        assert lines[1].strip() == (
            "68,Dog-chewed baseball glove," \
            "Wore the glove when making the winning catch for the little league world series.," \
            "1999-12-25T18:37:25"
        )


def test_convert_json_to_trash_nothing_post(sample_trash_nothing_api_data):
    # call the function
    post = convert_json_to_trash_nothing_post(sample_trash_nothing_api_data)

    expected_results = TrashNothingPost(
        post_id=43065400,
        title="Verticals blind replacement slats (West Riverside off 91 freeway)",
        description="31/2 inches wide by 82 inches long. Pecan colored vertical blind "
            "replacement slats. Perfect condition. They don’t get along with "
            "my cats!😂there are 27 of them.\n"
            "\n"
            "\n"
            "https://trashnothing.com/pics/9FtxWkT",
        collection_days_times="",
        post_date="2024-04-14T21:53:15",
        expiry_date="2024-07-13T21:53:15",
        outcome=None,
        reply_measure="low",
        latitude=33.92209325780915,
        longitude=-117.42453890783474,
        user_id=9190382
    )

    # check expected results
    assert post == expected_results
