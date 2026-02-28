from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.dtos.menu_dto import FastFood
from app.Entities.food_model import FastFood_model
router = APIRouter(prefix="/Food", tags=["Food Master"])

@router.post("/add-food")
async def AddFood(
    food:FastFood,
    db: AsyncSession = Depends(get_db)
):
    ab=FastFood_model(
id=food.burger
    )
    db.add(ab)
    db.commit()
    return "working"