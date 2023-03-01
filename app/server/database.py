from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOSTNAME}:{settings.DATABASE_PORT}/{settings.POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# helpers

def prediction_helper(prediction) -> dict:
  return {
    "id": str(prediction["_id"]),
    "text": prediction["fullname"],
  }
    
# Retrieve all predictions present in the database
async def retrieve_predictions():
  pass


# Add a new prediction into to the database
async def add_prediction(prediction_data: dict) -> dict:
  pass


# Retrieve a prediction with a matching ID
async def retrieve_prediction(id: str) -> dict:
  pass


# Update a prediction with a matching ID
async def update_prediction(id: str, data: dict):
  pass


# Delete a prediction from the database
async def delete_prediction(id: str):
  pass