from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from beanie import init_beanie
from pymongo.asynchronous.database import AsyncDatabase

from collection.product import Product
from collection.recomendation import Recommendation
from collection.user import User


async def init_db() -> AsyncDatabase:
    client: AsyncIOMotorClient = AsyncIOMotorClient("mongodb://mongo:27017")
    db: AsyncDatabase| AsyncIOMotorDatabase = client["tienda"]
    await init_beanie(database=db, document_models=[User, Product, Recommendation])
    return db
