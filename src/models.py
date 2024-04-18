from dataclasses import dataclass, fields


@dataclass
class TrashPost:
    post_id: int
    title: str
    description: str
    collection_days_times: str
    post_date: str
    expiry_date: str
    outcome: str
    reply_measure: str
    latitude: float
    longitude: float
    user_id: int


    def keys(self):
        return [field.name for field in fields(self)]
