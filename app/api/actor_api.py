from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.core.database import get_db
from app.Entities.actor import Actor
from app.dtos.actor_dto import ActorCreate,ActorResponse,ActorUpdate
router = APIRouter(prefix="/actors",tags=["Actors"])

@router.post("/",response_model=ActorResponse)
async def create_actor(actor:ActorCreate,db: AsyncSession=Depends(get_db)):
    new_actor=Actor(name=actor.name)
    db.add(new_actor)
    await db.commit()
    await db.refresh(new_actor)
    return new_actor

@router.get("/",response_model=list[ActorResponse])
async def get_actor(db:AsyncSession=Depends(get_db)):
 result=await db.execute(select(Actor))
 actors=result.scalars().all()
 
 return actors

@router.patch("/{actor_id}",response_model=ActorResponse)
async def update_actor(actor_id:int,actor:ActorUpdate,db:AsyncSession=Depends(get_db)):
 result=  await db.execute(select(Actor).where(Actor.id==actor_id))
 actor_obj=result.scalar_one_or_none()
 if not actor_obj:
    raise 
 HTTPException(status_code=404,detail="Actor not found")
 for key, value in actor.dict(exclude_unset=True).items():  
   setattr(actor_obj,key,value)

 await db.commit()
 await db.refresh(actor_obj)
 return actor_obj
   
@router.delete("/{actor_id}")
async def delete_actor(actor_id:int,db:AsyncSession=Depends(get_db)):
  result = await db.execute(select(Actor).where(Actor.id==actor_id))
  actor=result.scalar_one_or_none()
  if not actor:
    raise 
  HTTPException(status_code=404,detail="actor not found")
  await db.delete(actor)
  await db.commit()
  return{"message":"deleted sucessful"}