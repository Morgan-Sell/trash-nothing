from dataclasses import dataclass, fields

import pandas as pd
import pytest
from aiohttp import web

from trash_nothing.src import TrashNothingPost


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
    trash_post = TrashNothingPost(
        post_id=1,
        title="Flying skateboard",
        description="Max speed is 90 mph. Has built in solar panel \
            for charging.",
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
        "content": "31/2 inches wide by 82 inches long. Pecan colored \
            vertical blind replacement slats. Perfect condition. They \
            don’t get along with my cats!😂there are 27 of them.\n\n\n \
            https://trashnothing.com/pics/9FtxWkT",
        "date": "2024-04-14T21:53:15",
        "expiration": "2024-07-13T21:53:15",
        "footer": "",
        "group_id": "",
        "latitude": 33.92209325780915,
        "longitude": -117.42453890783474,
        "outcome": "",
        "outcome_date": "",
        "photos": None,
        "post_id": 43065400,
        "reply_measure": "low",
        "repost_count": 0,
        "reselling": None,
        "source": "trashnothing",
        "title": "Verticals blind replacement slats (West Riverside \
            off 91 freeway)",
        "type": "offer",
        "url": "https://trashnothing.com/post/43065400/verticals-blind- \
            replacement-slats-west-riverside-off-91-freeway",
        "user_id": 9190382,
    }
    return data


@pytest.fixture(scope="function")
async def mock_server(aiohttp_server):
    """Fixture to create a mock response helper function"""

    async def hello(request):
        page = request.rel_url.query.get("page")
        if request.path == "/error":
            raise web.HTTPNotFound(text="Not found")
        return web.json_response(
            data={"message": "Hello", "page": page}, status=200
        )

    app = web.Application()
    app.router.add_get("/", hello)
    app.router.add_get("/server", hello)
    return await aiohttp_server(app)


@pytest.fixture(scope="module")
def sample_dataset():
    data = {
        "post_id": [1, 2, 3, 4, 5],
        "title": [
            "skateboard", "baseball", "kitchen sink", "guitar", "surfboard"
        ],
        "description": [
            "wood with 4 wheels",
            "white canvas and red stitch",
            "commercial size",
            "Played by BB King",
            "Float on water",
        ],
        "collection_days_times": [
            "week nights",
            "weekdays during lunch",
            "Weekends between 1 and 5pm",
            "Sundays only",
            "First Friday of the month",
        ],
        "post_date": [
            "2024-04-25 17:15:02",
            "2024-01-31 15:15:02",
            "2024-02-14 10:15:01",
            "2024-01-01 18:15:03",
            "2024-03-02 08:16:44",
        ],
        "expiry_date": [
            "2024-05-25 01:16:05",
            "2024-03-02 20:44:05",
            "2024-02-28 11:22:09",
            "2024-04-25 14:51:05",
            "2024-07-25 08:33:06",
        ],
        "outcome": ["taken", "promised", "promised", "taken", ""],
        "reply_measure": ["high", "low", "medium", "low", "high"],
        "latitude": [34.4, 39.0, 37.4, 38.7, 39.1],
        "longitude": [-84.2, -34.3, -100.1, -101.3, 50.1],
        "user_id": [3456, 1234, 6523, 33, 1983],
    }

    df = pd.DataFrame(data)

    # transform to datetime objects
    df["post_date"] = pd.to_datetime(df["post_date"])
    df["expiry_date"] = pd.to_datetime(df["expiry_date"])

    return df
