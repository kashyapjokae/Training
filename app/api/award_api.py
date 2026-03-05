from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import SessionLocal
from app.entities.award_model import Award
from app.dtos.award_dto import AwardCreate, AwardUpdate

router = APIRouter(prefix="/awards", tags=["Awards"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_award(award: AwardCreate, db: Session = Depends(get_db)):
    new_award = Award(award_name=award.award_name, movie_id=award.movie_id)
    db.add(new_award)
    db.commit()
    db.refresh(new_award)
    return new_award

@router.get("/")
def get_awards(db: Session = Depends(get_db)):
    return db.query(Award).all()

@router.put("/{award_id}")
def update_award(award_id: int, award: AwardUpdate, db: Session = Depends(get_db)):
    db_award = db.query(Award).filter(Award.id == award_id).first()
    db_award.award_name = award.award_name
    db.commit()
    return db_award