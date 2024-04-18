import csv
import os

from .config import JSONType
from .models import TrashPost


def initialize_csv_with_headers(file_path: str, headers: list) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def append_data_to_csv(file_path: str, data_class: TrashPost) -> None:
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_class.values())



def convert_json_to_trash_post(data: JSONType) -> TrashPost:
    post = TrashPost(
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
