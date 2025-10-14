from beanie import Document, Indexed
from pydantic import Field
from datetime import datetime

class User(Document):
    name: str
    email: Indexed(str, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "user"