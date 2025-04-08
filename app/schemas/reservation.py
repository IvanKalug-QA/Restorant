from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ReservationCreate(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int


class ReservationDB(ReservationCreate):
    id: int
    model_config = ConfigDict(from_attributes=True)
