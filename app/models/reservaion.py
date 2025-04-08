from datetime import datetime

from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class Reservation(Base):
    customer_name: Mapped[str] = mapped_column(String(100), nullable=False)
    reservation_time: Mapped[datetime] = mapped_column(
        DateTime, nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False)
    table_id: Mapped[int] = mapped_column(ForeignKey('table.id'))

    def __repr__(self):
        return (
            f'Забранированно в {
                self.reservation_time} на {self.duration_minutes} минут.'
        )
