from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


def create_connection(db_url: str, db_name: str) -> AIOEngine:
    client = AsyncIOMotorClient(db_url)
    engine = AIOEngine(client=client, database=db_name)
    return engine
