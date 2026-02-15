from pydantic import BaseModel, Field
from typing import Optional, Dict, Any


class PredictRequest(BaseModel):
    # Все фичи German Credit (кроме target credit_risk)
    checking_status: str
    duration_months: int
    credit_history: str
    purpose: str
    credit_amount: int
    savings_status: str
    employment: str
    installment_rate: int
    personal_status: str
    other_debtors: str
    residence_since: int
    property_magnitude: str
    age: int
    other_payment_plans: str
    housing: str
    existing_credits: int
    job: str
    num_dependents: int
    own_telephone: str
    foreign_worker: str

    # опционально: request_id, чтобы удобно дебажить
    request_id: Optional[str] = Field(default=None)


class PredictResponse(BaseModel):
    probability: float
    predicted_label: int
    threshold: float = 0.5
    request_id: Optional[str] = None