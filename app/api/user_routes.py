from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers import UserController
from app.database import get_db
from app.schemas import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return UserController.create_user(user=user, db=db)
