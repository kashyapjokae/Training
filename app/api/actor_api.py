from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.entities.actor_model import Actor
from app.dtos.actor_dto import ActorResponse

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.get("/{actor_id}", response_model=ActorResponse)
def get_actor(actor_id: int, db: Session = Depends(get_db)):

    actor = db.query(Actor).filter(Actor.id == actor_id).first()

    return actor