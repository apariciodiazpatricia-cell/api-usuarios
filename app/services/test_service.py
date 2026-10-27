from typing import List
from sqlalchemy.orm import Session

from app.models.test_model import TestModel
from app.schemas.test_schema import TestCreate


class TestService:
    @staticmethod
    def create_test(db: Session, test_data: TestCreate) -> TestModel:
        db_item = TestModel(
            name=test_data.name,
            description=test_data.description,
        )
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def get_tests(db: Session) -> List[TestModel]:
        return db.query(TestModel).all()
