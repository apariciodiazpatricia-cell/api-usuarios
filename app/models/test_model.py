from sqlalchemy import Column, Integer, String
from app.database import Base


class TestModel(Base):
    __tablename__ = "tests"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
