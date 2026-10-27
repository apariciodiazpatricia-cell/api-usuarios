from typing import Optional
from pydantic import BaseModel, ConfigDict


class TestBase(BaseModel):
    name: str
    description: Optional[str] = None


class TestCreate(TestBase):
    pass


class TestResponse(TestBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
