from pydantic import BaseModel, Field
from typing import Annotated
import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

# model load

with open("model.pkl", "rb") as f:
  model = pickle.load(f)

class UserInput(BaseModel):
  Area : Annotated[int, Field(..., gt=0)]
  MajorAxisLength :Annotated[float, Field(..., gt=0)]
  MinorAxisLength : Annotated[float, Field(..., gt=0)]
  Eccentricity : Annotated[float, Field(..., gt=0)]
  ConvexArea : Annotated[float, Field(..., gt=0)]
  Extent : Annotated[float, Field(..., gt=0)]
  Perimeter : Annotated[float, Field(..., gt=0)]


app = FastAPI()

@app.get("/hello")
def hello():
  return {"message": "Hello Everyone"}

@app.post("/predict")
def predict(data : UserInput):

  input_df = pd.DataFrame([{
    "Area" : data.Area,
    "MajorAxisLength" : data.MajorAxisLength,
    "MinorAxisLength" : data.MinorAxisLength,
    "Eccentricity" : data.Eccentricity,
    "ConvexArea" : data.ConvexArea,
    "Extent" : data.Extent,
    "Perimeter" : data.Perimeter
  }])

  prediction = int(model.predict(input_df)[0])

  prediction = "Kecimen" if prediction == 1 else "Besni"

  return JSONResponse(status_code = 200, content = {"prediction_value":prediction})

