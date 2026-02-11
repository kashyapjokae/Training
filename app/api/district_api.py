from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.dtos.district_create_dto import district_dto
from app.Entities.district_model import District_model
router = APIRouter(prefix="/district", tags=["District Master"])

@router.post("/Create-District")
async def CreateDistrict(
    district: district_dto,
    db: AsyncSession = Depends(get_db)
):
    mmapped_data = District_model(
        district_name=district.district_name,
        district_code=district.district_code,
        is_active=True
    )
    db.add(mmapped_data)
    await db.commit()
    await db.refresh(mmapped_data)
    return {
        "message":"Successfully Created"
    }
