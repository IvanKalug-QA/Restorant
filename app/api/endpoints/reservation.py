from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page
from fastapi_pagination.iterables import paginate

from app.core.db import get_async_session
from app.database.reservation import reservation_crud
from app.core.user import current_user
from app.database.table import table_crud
from app.schemas.reservation import ReservationCreate, ReservationDB
from app.validators.reservation import (
    check_exists_reservation_by_id, check_reservation_on_same_time)
from app.validators.table import check_exists_table_and_get_obj


router = APIRouter(prefix='/reservations', tags=['reservations'])


@router.get(
    '/', response_model=Page[ReservationDB],
    dependencies=[Depends(current_user)])
async def get_all_reservations(
    session: AsyncSession = Depends(get_async_session)
):
    reservations_db = await reservation_crud.get_all_reservations(
        session
    )
    return paginate(reservations_db)


@router.post(
    '/', response_model=ReservationDB, dependencies=[Depends(current_user)])
async def create_reservarion(
    reservation_schema: ReservationCreate,
    session: AsyncSession = Depends(get_async_session),
):
    await check_exists_table_and_get_obj(
        table_crud, reservation_schema.table_id, session
    )
    await check_reservation_on_same_time(
        reservation_schema, session, reservation_crud)
    return await reservation_crud.create_reservation(
        reservation_schema,
        session)


@router.delete(
    '/{id}', response_model=ReservationDB,
    dependencies=[Depends(current_user)])
async def delete_reservation(
    id: int, session: AsyncSession = Depends(get_async_session)
):
    reservation_obj = await check_exists_reservation_by_id(
        reservation_crud, id, session
    )
    return await reservation_crud.delete_reservation(
        reservation_obj, session
    )
