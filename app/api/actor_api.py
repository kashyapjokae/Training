from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.core.database import get_db
from app.entities.actor_model import Actor
from app.entities.movie_model import Movie
from app.dtos.actor_dto import ActorResponse

router = APIRouter(prefix="/actors", tags=["Actors"])


# CREATE Actor
@router.post("/", response_model=ActorResponse)
async def create_actor(actor: ActorResponse, db: AsyncSession = Depends(get_db)):

    new_actor = Actor(name=actor.name)

    db.add(new_actor)
    await db.commit()
    await db.refresh(new_actor)

    return new_actor


# GET ALL Actors with Movies and Awards
@router.get("/", response_model=list[ActorResponse])
async def get_all_actors(db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Actor).options(
            selectinload(Actor.movies).selectinload(Movie.awards)
        )
    )

    actors = result.scalars().all()

    return actors


# GET Actor by ID with Movies and Awards
@router.get("/{actor_id}", response_model=ActorResponse)
async def get_actor(actor_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Actor)
        .where(Actor.id == actor_id)
        .options(
            selectinload(Actor.movies).selectinload(Movie.awards)
        )
    )

    actor = result.scalar_one_or_none()

    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    return actor


# UPDATE Actor
@router.put("/{actor_id}", response_model=ActorResponse)
async def update_actor(actor_id: int, actor: ActorResponse, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Actor).where(Actor.id == actor_id)
    )

    db_actor = result.scalar_one_or_none()

    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    db_actor.name = actor.name

    await db.commit()
    await db.refresh(db_actor)

    return db_actor


# DELETE Actor
@router.delete("/{actor_id}")
async def delete_actor(actor_id: int, db: AsyncSession = Depends(get_db)):

    result = await db.execute(
        select(Actor).where(Actor.id == actor_id)
    )

    actor = result.scalar_one_or_none()

    if actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")

    await db.delete(actor)
    await db.commit()

    return {"message": "Actor deleted successfully"}