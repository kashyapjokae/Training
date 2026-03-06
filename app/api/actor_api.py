from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.entities.actor_model import Actor
from app.dtos.actor_dto import ActorCreate, ActorUpdate

router = APIRouter(prefix="/actors", tags=["Actors"])


@router.post("/")
def create_actor(actor: ActorCreate, db: Session = Depends(get_db)):
    new_actor = Actor(name=actor.name)

    db.add(new_actor)
    db.commit()
    db.refresh(new_actor)

    return new_actor


@router.get("/")
def get_actors(db: Session = Depends(get_db)):
    return db.query(Actor).all()


@router.put("/{actor_id}")
def update_actor(actor_id: int, actor: ActorUpdate, db: Session = Depends(get_db)):
    db_actor = db.query(Actor).filter(Actor.id == actor_id).first()

    db_actor.name = actor.name

    db.commit()
    db.refresh(db_actor)

    return db_actor