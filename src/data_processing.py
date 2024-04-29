import csv
import os
from datetime import datetime

import pandas as pd

from config import JSONType
from models import TrashNothingPost


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
    # create the directory it is does not exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    
    if not os.path.exists(file_path):
        # create and open the file for writing
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


def load_and_process_data(
    data: pd.DataFrame, start_date_var: str, end_date_var: str
) -> pd.DataFrame:
    """
    Loads a dataset from a CSV file and processes the date columns.

    Parameters:
    - data (pd.DataFrame): The path to the CSV file to be loaded as a DataFrame.
    - start_date_var (str): The name of the column in `data` that contains the start dates.
    - end_date_var (str): The name of the column in `data` that contains the end dates.

    Returns:
    - df (pd.DataFrame): A DataFrame with the original data, where the `start_date_var` and `end_date_var`
      have been converted to datetime objects and a new column `days_available_for_pickup` has been added,
      which contains the number of days between `start_date_var` and `end_date_var`.
    """
    df = pd.read_csv(data)

    # transform to datetime objects
    df[start_date_var] = pd.to_datetime(df[start_date_var])
    df[end_date_var] = pd.to_datetime(df[end_date_var])

    # calculate number of days that item can be picked up
    df["days_available_for_pickup"] = (df[end_date_var] - df[start_date_var]).dt.days

    return df


def combine_text(data: pd.DataFrame, variable: str) -> str:
    """
    Concatenate all text elements from a specified column in a DataFrame into a single string.

    Parameters:
    - data (pd.DataFrame): The DataFrame containing the text data to combine.
    - variable (str): The name of the column in `data` from which to aggregate the text.

    Returns:
    - str: A single string consisting of all text elements from the specified column
      in the DataFrame concatenated together, separated by spaces.
    """

    return " ".join(words for words in data[variable])