from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.controllers import TestController
from app.database import get_db
from app.schemas import TestCreate, TestResponse

router = APIRouter(prefix="/test", tags=["Test"])


@router.post("/", response_model=TestResponse, status_code=status.HTTP_201_CREATED)
def create_test(test_data: TestCreate, db: Session = Depends(get_db)):
    return TestController.create_test(test_data=test_data, db=db)


@router.get("/", response_model=List[TestResponse])
def get_tests(db: Session = Depends(get_db)):
    return TestController.get_tests(db=db)
