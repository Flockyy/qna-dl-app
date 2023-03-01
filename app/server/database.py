

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