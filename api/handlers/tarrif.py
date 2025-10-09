from fastapi import APIRouter
from service.database import add_tariff_service, get_tariffs_service

router = APIRouter(prefix="/tarrif", tags=['tarrif'])

@router.get("/all_tarrifs")
async def get_all_tarrifs():
    result = await get_tariffs_service()
    return {"tariffs": result}

@router.post("/add_tariff")
async def add_tariff(name: str, price: int):
    result = await add_tariff_service(name, price)
    return {"status": result}