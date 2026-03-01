from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime, timezone


class Expenses(BaseModel):

    type: Literal["income", "expense"]
    amount: float
    currency: str = "INR"
    category: str

    description: Optional[str] = None

    date: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))