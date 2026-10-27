from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models import User
from app.schemas import UserCreate


class UserService:
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Este correo electrónico ya está registrado",
            )

        db_user = User(
            name=user.name,
            email=user.email,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
