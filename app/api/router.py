from fastapi import APIRouter

from app.api.endpoints import user_router, table_router, reservation_router


main_router = APIRouter(prefix='/api')

main_router.include_router(user_router)
main_router.include_router(table_router)
main_router.include_router(reservation_router)
