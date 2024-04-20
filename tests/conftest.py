from dataclasses import dataclass, fields

import pytest
from trash_nothing.src.models import TrashPost


@dataclass
class MockTrashPost:
    post_id: int
    title: str
    description: float
    post_date: str

    def values(self):
        return [getattr(self, field.name) for field in fields(self)]


@pytest.fixture(scope="module")
def sample_trash_post():
    trash_post = TrashPost(
        post_id=1,
        title="Flying skateboard",
        description="Max speed is 90 mph. Has built in solar panel for charging.",
        collection_days_times="Weekends between 1 and 5pm",
        post_date="2024-04-14T21:38:25",
        expiry_date="2024-07-13T21:38:25",
        outcome="taken",
        reply_measure="high",
        latitude=34.41,
        longitude=84.2,
        user_id=3456,
    )

    return trash_post

@pytest.fixture(scope="module")
def sample_trash_nothing_api_data():
    data = {
        "collection_days_times": "",
        "content": "31/2 inches wide by 82 inches long. Pecan colored vertical blind "
        "replacement slats. Perfect condition. They don’t get along with "
        "my cats!😂there are 27 of them.\n"
        "\n"
        "\n"
        "https://trashnothing.com/pics/9FtxWkT",
        "date": "2024-04-14T21:53:15",
        "expiration": "2024-07-13T21:53:15",
        "footer": None,
        "group_id": None,
        "latitude": 33.92209325780915,
        "longitude": -117.42453890783474,
        "outcome": None,
        "outcome_date": None,
        "photos": None,
        'post_id': 43065400,
        "reply_measure": "low",
        "repost_count": 0,
        "reselling": None,
        "source": "trashnothing",
        "title": "Verticals blind replacement slats (West Riverside off 91 freeway)",
        "type": "offer",
        "url": "https://trashnothing.com/post/43065400/verticals-blind-replacement-slats-west-riverside-off-91-freeway",
        "user_id": 9190382
    }
    return data
