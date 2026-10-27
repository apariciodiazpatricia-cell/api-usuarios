from typing import List
from sqlalchemy.orm import Session

from app.schemas.test_schema import TestCreate, TestResponse
from app.services.test_service import TestService


class TestController:
    @staticmethod
    def create_test(test_data: TestCreate, db: Session) -> TestResponse:
        return TestService.create_test(db=db, test_data=test_data)

    @staticmethod
    def get_tests(db: Session) -> List[TestResponse]:
        return TestService.get_tests(db=db)
