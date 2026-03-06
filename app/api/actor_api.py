from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.core.database import get_db
from app.Entities.actor_model import Actor
from app.dtos.actor_create_dto import ActorCreateDTO
from app.dtos.actor_update_dto import ActorUpdateDTO

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.post("/")
async def create_actor(actor: ActorCreateDTO, db: AsyncSession = Depends(get_db)):

    new_actor = Actor(name=actor.name)

    db.add(new_actor)
    await db.commit()
    await db.refresh(new_actor)

    return new_actor


@router.get("/")
async def get_actors(db: AsyncSession = Depends(get_db)):

    result = await db.execute(select(Actor))
    actors = result.scalars().all()

    return actors