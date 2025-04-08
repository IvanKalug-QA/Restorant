from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_pagination import Page
from fastapi_pagination.iterables import paginate

from app.core.db import get_async_session
from app.database.table import table_crud
from app.core.user import current_user
from app.schemas.table import TableDB, TableCreate
from app.validators.table import (
    check_exists_table,
    check_exists_table_and_get_obj)

router = APIRouter(prefix='/tables', tags=['table'])


@router.get(
    '/', response_model=Page[TableDB], dependencies=[Depends(current_user)])
async def get_tables(session: AsyncSession = Depends(get_async_session)):
    tables = await table_crud.get_all_tables(session)
    return paginate(tables)


@router.post(
    '/', response_model=TableDB, dependencies=[Depends(current_user)])
async def create_tabel(
    table_schema: TableCreate,
    session: AsyncSession = Depends(get_async_session)
):
    await check_exists_table(table_crud, table_schema.name, session)
    return await table_crud.create_table(table_schema, session)


@router.delete(
    '/{id}', response_model=TableDB, dependencies=[Depends(current_user)])
async def delete_table(
    id: int, session: AsyncSession = Depends(get_async_session)
):
    table_obj = await check_exists_table_and_get_obj(
        table_crud,
        id, session
    )
    return await table_crud.delete_table(session, table_obj)
