from typing import Optional
from app.server.database import Base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel, Field

class PredictionOrm(Base):
    __tablename__ = 'predictions'
    id = Column(Integer, primary_key=True, nullable=False)
    text = Column(String(500), unique=True)

class PredictionSchema(BaseModel):
  text: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "text": "Hello there",
      }
    }
    orm_mode = True

def ResponseModel(data, message):
  return {
    "data": [data],
    "code": 200,
    "message": message,
  }

def ErrorResponseModel(error, code, message):
  return {"error": error, "code": code, "message": message}