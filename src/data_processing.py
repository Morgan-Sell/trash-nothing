import csv
import os
import re

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


def remove_emojis(text: str) -> str:
    # Regular expression pattern to match all emojis
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        "\U0001FA00-\U0001FA6F"  # Chess Symbols
        "\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        "\U00002702-\U000027B0"  # Dingbats
        "\U000024C2-\U0001F251" 
        "]+",
        flags=re.UNICODE
    )

    clean_text = emoji_pattern.sub(r"", text)

    return clean_text


def remove_newline_characters(text):
    return text.replace("\n", "")