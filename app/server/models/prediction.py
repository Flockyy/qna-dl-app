from typing import Optional

from pydantic import BaseModel, Field

class PredictionSchema(BaseModel):
  text: str = Field(...)

  class Config:
    schema_extra = {
      "example": {
        "text": "Hello there",
      }
    }

class UpdatePredictionModel(BaseModel):
  text: Optional[str]

  class Config:
    schema_extra = {
      "example": {
        "text": "Hello there",
      }
    }

def ResponseModel(data, message):
  return {
    "data": [data],
    "code": 200,
    "message": message,
  }

def ErrorResponseModel(error, code, message):
  return {"error": error, "code": code, "message": message}