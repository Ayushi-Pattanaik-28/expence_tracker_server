from app.db.expenseDb import expense_collection
from bson import ObjectId
from fastapi import HTTPException


def create_expense(data: dict, current_user: dict):

    data["user_id"] = current_user["user_id"]

    result = expense_collection.insert_one(data)

    return {
        "message": "Expense created successfully",
        "id": str(result.inserted_id),
    }


def get_all_expenses(current_user: dict):

    expenses = expense_collection.find({"user_id": current_user["user_id"]})

    expense_list = []

    for exp in expenses:
        exp["_id"] = str(exp["_id"])
        expense_list.append(exp)

    return expense_list


def update_expense(data: dict, expense_id: str, current_user: dict):

    result = expense_collection.update_one(
        {
            "_id": ObjectId(expense_id),
            "user_id": current_user["user_id"],
        },
        {"$set": data},
    )

    if result.modified_count == 0:
        raise HTTPException(
            status_code=404, detail="Expense not found or not owned by you"
        )

    return {"message": "Expense updated successfully"}


def delete_expense(expense_id: str, current_user: dict):

    result = expense_collection.delete_one(
        {
            "_id": ObjectId(expense_id),
            "user_id": current_user["user_id"],
        }
    )

    if result.deleted_count == 0:
        raise HTTPException(
            status_code=404, detail="Expense not found or not owned by you"
        )

    return {"message": "Expense deleted successfully"}
