from http import HTTPStatus

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException


async def check_exists_table(
    table_crud, table_name: str, session: AsyncSession
):
    table_db = await table_crud.get_table_by_name(table_name, session)
    if table_db is not None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такой столик уже есть!'
        )


async def check_exists_table_and_get_obj(
        table_crud, table_id: int, session: AsyncSession):
    table_obj = await table_crud.get_table_by_id(session, table_id)
    if table_obj is None:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Такого столика нет!'
        )
    return table_obj
