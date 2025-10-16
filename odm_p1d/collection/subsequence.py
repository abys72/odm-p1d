from odmantic import Model, Field

from typing import List
from datetime import datetime


class Subsequence(Model):
    subsequence: List[List[int]]
    created_at: datetime = Field(default_factory=datetime.utcnow, index=True)

    model_config = {
        "collection": "subsequence"
    }
