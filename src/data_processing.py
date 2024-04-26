import csv
import os
import re
from datetime import datetime

from .config import JSONType
from .models import TrashNothingPost


def initialize_csv_with_headers(file_path: str, headers: list) -> None:
    """
    Creates a new CSV file at the specified file path and writes the given headers
    as the first row of the file. If the file already exists, it does nothing.

    Parameters:
    - file_path (str): The path where the CSV file will be created.
    - headers (list): A list of strings representing the header row of the CSV.

    Returns:
    - None

    Raises:
    - IOError: An error occurred when attempting to write to the file.
    """
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def append_data_to_csv(file_path: str, data_class: TrashNothingPost) -> None:
    """
    Appends a row of data to an existing CSV file from an instance of TrashPost.
    The row is composed of the values from the data_class instance.

    Parameters:
    - file_path (str): The path to the CSV file where the data will be appended.

    - data_class (TrashPost): An instance of the TrashPost data class containing
      the data to be written to the CSV.

    Returns:
    - None:
    """
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_class.values())


def convert_json_to_trash_nothing_post(data: JSONType) -> TrashNothingPost:
    """
    Converts a JSON object to a TrashPost instance.

    Parameters:
    - data (JSONType): A dictionary-like object containing keys and values that map directly
      to the TrashPost data class attributes.

    Returns:
    - post (TrashNothingPost): An instance of the TrashPost data class populated with data from the JSON object.
    """

    post = TrashNothingPost(
        post_id=data["post_id"],
        title=data["title"],
        description=data["content"],
        collection_days_times=data["collection_days_times"],
        post_date=data["date"],
        expiry_date=data["expiration"],
        outcome=data["outcome"],
        reply_measure=data["reply_measure"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        user_id=data["user_id"],
    )
    return post


def calc_days_between_dates(start_date: datetime, end_date: datetime) -> int:
    difference = end_date - start_date
    total_seconds = difference.total_seconds()
    days_diff = total_seconds // (24 * 60 * 60)
    return days_diff
