from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.table import Table
from app.schemas.table import TableCreate


class TableCRUD:
    async def get_all_tables(
        self, session: AsyncSession
    ) -> list[Table]:
        tables_db = await session.execute(
            select(Table)
        )
        return tables_db.scalars().all()

    async def get_table_by_name(
        self, table_name: str, session: AsyncSession
    ) -> Table | None:
        table_db = await session.execute(
            select(Table).where(Table.name == table_name)
        )
        return table_db.scalar_one_or_none()

    async def get_table_by_id(
        self, session: AsyncSession,
        table_id: int
    ) -> Table | None:
        table_db = await session.execute(
            select(Table).where(Table.id == table_id)
        )
        return table_db.scalar_one_or_none()

    async def create_table(
            self, table_schema: TableCreate,
            session: AsyncSession
    ) -> Table:
        new_table = Table(**table_schema.model_dump())
        session.add(new_table)
        await session.commit()
        await session.refresh(new_table)
        return new_table

    async def delete_table(
        self, session: AsyncSession,
        table_obj: Table
    ) -> Table:
        await session.delete(table_obj)
        await session.commit()
        return table_obj


table_crud = TableCRUD()
