from dataclasses import dataclass


@dataclass
class Auction:
    name: str
    date: str
    winning_bid_max: float
    winning_bid_min: float
    winning_bid_mean: float
    trading_volume: float
    lots_count: float
