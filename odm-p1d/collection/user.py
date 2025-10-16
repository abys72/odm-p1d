from odmantic import Model, Field, Index
from datetime import datetime


class User(Model):
    name: str
    password: str
    email: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
