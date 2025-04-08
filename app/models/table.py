from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


class Table(Base):
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    seats: Mapped[int] = mapped_column(Integer, nullable=False)
    location: Mapped[str] = mapped_column(String(256), nullable=False)
    reservations = relationship('Reservation')
