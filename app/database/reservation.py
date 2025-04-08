from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.reservaion import Reservation
from app.schemas.reservation import ReservationCreate


class ReservationCRUD:
    async def get_all_reservations(
        self,
        session: AsyncSession
    ) -> list[Reservation]:
        reservations_db = await session.execute(
            select(Reservation)
        )
        return reservations_db.scalars().all()

    async def get_reservation_by_id(
        self,
        reservation_id: int, session: AsyncSession
    ) -> Reservation | None:
        reservation_db = await session.execute(
            select(Reservation).where(Reservation.id == reservation_id)
        )
        return reservation_db.scalar_one_or_none()

    async def get_reservations_with_that_table(
        self,
        table_id: int,
        session: AsyncSession
    ) -> list[Reservation] | None:
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.table_id == table_id))
        return reservations.scalars().all()

    async def create_reservation(
        self,
        reservation_shema: ReservationCreate,
        session: AsyncSession
    ) -> Reservation:
        new_reservation = Reservation(**reservation_shema.model_dump())
        session.add(new_reservation)
        await session.commit()
        await session.refresh(new_reservation)
        return new_reservation

    async def delete_reservation(
        self,
        obj_db: Reservation, session: AsyncSession
    ) -> Reservation:
        await session.delete(obj_db)
        return obj_db


reservation_crud = ReservationCRUD()
