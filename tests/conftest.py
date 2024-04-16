from dataclasses import dataclass

import pytest


@dataclass
class MockAuction:
    name: str
    date: str
    bid: float

    def values(self):
        return (self.name, self.date, self.bid)
