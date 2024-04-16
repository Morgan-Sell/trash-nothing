from dataclasses import dataclass

import pytest
from whiskey_auction.src.models import Auction


@dataclass
class MockAuction:
    name: str
    date: str
    bid: float

    def values(self):
        return (self.name, self.date, self.bid)


@pytest.fixture(scope="module")
def sample_auction():
    auction = Auction(
        name="Spartacus Whiskey",
        date="614-06-07",
        winning_bid_max=1000.47,
        winning_bid_min=3.99,
        winning_bid_mean=673.21,
        trading_volume=99999,
        lots_count=2345,
    )
    return auction


@pytest.fixture(scope="module")
def sample_whiskey_api_data():
    data = {
        "dt": "2024-03-01",
        "winning_bid_max": 5167.3,
        "winning_bid_min": 11.9,
        "winning_bid_mean": 204.82,
        "auction_trading_volume": 259096.9,
        "auction_lots_count": 1265,
        "all_auctions_lots_count": 47132,
        "auction_name": "Australian Whisky Auctions",
        "auction_slug": "australian-whisky-auctions"
    }
    return data
