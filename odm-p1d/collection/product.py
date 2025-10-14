from beanie import Document, Indexed

class Product(Document):
    id: Indexed(int, unique=True)
    name: str
    category: str
    price: float

    class Settings:
        name = "product"