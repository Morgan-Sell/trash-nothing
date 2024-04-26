from datetime import datetime

import pytest

from trash_nothing.src.models import TrashNothingPost


def test_trash_nothing_post_post_init(sample_trash_nothing_api_data):
    data = sample_trash_nothing_api_data()

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

    # test removal of commas
    assert "," not in post.title
    assert "," not in post.description

    # test rounding of latitude and longitude
    assert post.latitude == 33.9
    assert post.longitude == -117.4

    # test dates are datetime objects
    assert isinstance(post.post_date, datetime)
    assert isinstance(post.expiry_date, datetime)

    # test newline characters are removed
    assert "\n" not in post.description

    # test url are removed
    assert "https://trashnothing.com/pics/9FtxWkT" not in post.description

    # test emojis are removed
    assert "😂" not in post.description
