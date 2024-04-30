import re
from dataclasses import dataclass, fields
from datetime import datetime


@dataclass
class TrashNothingPost:
    """
    Represents a post made on the TrashNothing website. A website where
    people list used goods, so the products can find a second home.

    Attributes:
    - post_id (int): Unique identifier for the post.
    - title (str): Title of the TrashNothing post, describing what is
      being offered.
    - description (str): Detailed description of the offer.
    - collection_days_times (str): Information about when the used good
      can be collected.
    - post_date (str): The date when the post was made.
    - expiry_date (str): The date when the offer expires.
    - outcome (str): Outcome of the post, e.g., 'Collected', 'Available'.
    - reply_measure (str): Level of interest, e.g., 'low', 'high'.
    - latitude (float): Geographic latitude of where to pick up the
      used good.
    - longitude (float): Geographic longitude of where to pick up the
      used good.
    - user_id (int): Identifier of the user who made the post.

    """

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

    def __post_init__(self):
        # remove commas from title because saving to CSV
        self.title = re.sub(",", "", self.title)

        # clean description attribute
        self.description = self._remove_emojis(self.description)
        self.description = self._remove_newline_characters(self.description)
        self.description = self._remove_urls(self.description)
        self.description = re.sub(
            ",", "", self.description
        )  # remoma comma because saving to CSV

        # round latitude and longitude
        self.latitude = round(self.latitude, 1)
        self.longitude = round(self.longitude, 1)

        # transform post_date and expiry_date to datetime objects
        date_format = "%Y-%m-%dT%H:%M:%S"
        self.post_date = datetime.strptime(self.post_date, date_format)
        self.expiry_date = datetime.strptime(self.expiry_date, date_format)

        # if 'outcome' is blank change value to 'No Pickup'
        self.outcome = self._modify_outcome(self.outcome)

    def keys(self):
        return [field.name for field in fields(self)]

    def values(self):
        return [getattr(self, field.name) for field in fields(self)]

    def _remove_emojis(self, text: str) -> str:
        """
        Removes emojis from the specified string using a regular expression.

        Parameters:
        - text (str): The string from which emojis will be removed.

        Returns:
        - cleaned_text (str): The modified string with all emojis removed.
        """

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
            flags=re.UNICODE,
        )

        cleaned_text = emoji_pattern.sub(r"", text)

        return cleaned_text

    def _remove_newline_characters(self, text: str) -> str:
        """
        Removes all newline characters, "\n" from a given string.

        Parameters:
        - text (str): The string from which newline characters
          are to be removed.

        Returns:
        - str: The modified string with all newline characters removed.
        """
        return text.replace("\n", "")

    def _remove_urls(self, text: str) -> str:
        """
        Removes URLs from a given text string using a regular expression.

        This method compiles a regex pattern that matches URLs
        beginning with 'http://', 'https://', or 'www', and replaces
        them with an empty string.

        Parameters:
        - text (str): The string from which URLs will be removed.

        Returns:
        - cleaned_text (str): The string with all URLs removed.
        """
        # This pattern matches most URLs that start with
        # http://, https://, or www and include typical URL characters
        url_pattern = r"https?://\S+|www\.\S+"

        # replace URLs with an empty string
        cleaned_text = re.sub(url_pattern, "", text)

        return cleaned_text

    def _modify_outcome(self, text: str) -> str:
        if text is None or text.strip() == "":
            return "available"
        else:
            return text
