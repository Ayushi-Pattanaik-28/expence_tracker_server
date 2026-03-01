from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://ayushidb:AyushiAtlas96@cluster0.emep0.mongodb.net/ExpenseTracker"
)

db = client["user_db"]
user_collection = db["users"]


def create_indexes():
    user_collection.create_index("email", unique=True)
