from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.models import UserCreate, User
from app.security import pwd_context
from app.authentication import authenticate_user
from app.database import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(username=user.username, email=user.email, password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user.__dict__

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    # Placeholder authentication logic
    # Replace with your actual authentication logic
    pass
