from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta


class Invoice(BaseModel):
    amount: int
    name: str
    tax_id: str
    
    due: Optional[str] = (datetime.utcnow() + timedelta(hours=48)).isoformat(),  # Campo opcional

    expiration: Optional[int] = 99999999  # Campo opcional
    fine: Optional[float] = 0.00  # Campo opcional
    interest: Optional[float] = 0.00  # Campo opcional

