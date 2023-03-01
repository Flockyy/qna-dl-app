from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.server.database import get_db

from app.server.database import (
    add_prediction,
    delete_prediction,
    retrieve_prediction,
    retrieve_predictions,
    update_prediction,
)
from app.server.models.prediction import (
    ErrorResponseModel,
    ResponseModel,
    PredictionSchema,
    PredictionOrm
)

router = APIRouter()

@router.post("/", response_description="Prediction data added into the database", status_code=status.HTTP_201_CREATED)
async def add_prediciton_data(predicton: PredictionSchema = Body(...), db: Session = Depends(get_db)):
    new_prediction = PredictionOrm(**predicton.dict())
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    return ResponseModel(new_prediction, "Prediciton added successfully.")
