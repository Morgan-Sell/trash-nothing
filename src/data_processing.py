import csv
import os

from .models import Auction


def initialize_csv_with_headers(file_path: str, headers: list) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def append_data_to_csv(file_path: str, data_class: Auction) -> None:
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_class.__init__.values())
