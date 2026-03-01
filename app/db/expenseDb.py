from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://ayushidb:AyushiAtlas96@cluster0.emep0.mongodb.net/ExpenseTracker"
)

db = client["expense_db"]

expense_collection = db["expenses"]
logger_user_collection = db["logged_user"]


def create_indexes():
    logger_user_collection.create_index("email", unique=True)

    # For transactions
    expense_collection.create_index("user_id")
    expense_collection.create_index("date")
    expense_collection.create_index("category")
