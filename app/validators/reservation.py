from http import HTTPStatus
from datetime import timedelta, datetime

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from app.schemas.reservation import ReservationCreate


async def check_exists_reservation_by_id(
    reservation_crud, reservarion_id: int,
    session: AsyncSession
):
    reservation = await reservation_crud.get_reservation_by_id(
        reservarion_id, session
    )
    if reservation is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой резервации нет!'
        )
    return reservation


async def check_reservation_on_same_time(
    reservation_schema: ReservationCreate,
    session: AsyncSession, reservation_crud
):
    reservations = await reservation_crud.get_reservations_with_that_table(
        reservation_schema.table_id, session
    )
    if reservations is None:
        return
    new_start_time: datetime = reservation_schema.reservation_time
    new_end_time: timedelta = reservation_schema.reservation_time + timedelta(
        minutes=reservation_schema.duration_minutes)
    for reservation in reservations:
        existing_start_time: datetime = reservation.reservation_time
        existing_end_time: timedelta = (
            reservation.reservation_time + timedelta(
                minutes=reservation.duration_minutes))
        if not (
            new_end_time <= existing_start_time or
            new_start_time >= existing_end_time
        ):
            raise HTTPException(
                status_code=HTTPStatus.BAD_REQUEST,
                detail=str(reservation)
            )
