from sqlalchemy.orm import Session

from app.schemas import UserCreate, UserResponse
from app.services import UserService


class UserController:
    @staticmethod
    def create_user(user: UserCreate, db: Session) -> UserResponse:
        return UserService.create_user(db=db, user=user)
