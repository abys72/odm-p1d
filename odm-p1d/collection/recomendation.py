from beanie import Document
from typing import List


class Recommendation(Document):
    user_id: int
    subsequence: List[int]

    class Settings:
        name = "recommendation"
