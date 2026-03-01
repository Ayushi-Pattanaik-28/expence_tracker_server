from fastapi import APIRouter, Depends
from app.controllers import expenseController
from app.schemas.expenseSchema import Expenses
from app.middlewares.authMiddleware import get_current_user
router = APIRouter(prefix="/expense", tags=["Expenses"])

@router.post("/")
def add_expense(
    expenses: Expenses,
    current_user: dict = Depends(get_current_user),
):
    return expenseController.create_expense(expenses.model_dump(), current_user)

@router.get("/")
def read_all(
    current_user: dict = Depends(get_current_user),
):
    return expenseController.get_all_expenses(current_user)

@router.put("/{expense_id}")
def modify_expense(
    expense: Expenses,
    expense_id: str,
    current_user: dict = Depends(get_current_user),
):
    return expenseController.update_expense(
        expense.model_dump(), expense_id, current_user
    )

@router.delete("/{expense_id}")
def remove_expense(
    expense_id: str,
    current_user: dict = Depends(get_current_user),
):
    return expenseController.delete_expense(expense_id, current_user)