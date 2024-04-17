import csv
import os

from .config import JSONType
from .models import Auction


def initialize_csv_with_headers(file_path: str, headers: list) -> None:
    if not os.path.exists(file_path):
        with open(file_path, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)


def append_data_to_csv(file_path: str, data_class: Auction) -> None:
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data_class.values())



def convert_json_to_auction(data: JSONType) -> Auction:
    auction = Auction(
        name=data["auction_name"],
        date=data["dt"],
        winning_bid_max=data["winning_bid_max"],
        winning_bid_min=data["winning_bid_min"],
        winning_bid_mean=data["winning_bid_mean"],
        trading_volume=data["auction_trading_volume"],
        lots_count=data["auction_lots_count"],
    )
    return auction
