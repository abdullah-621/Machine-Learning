from pydantic import BaseModel, Field,computed_field
from typing import Annotated
import pickle
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

# model load

with open('Model/model.pkl', 'rb') as f:
  model = pickle.load(f)

class UserInput(BaseModel):
  Age : Annotated[int, Field(..., gt=0)]
  Weight : Annotated[float, Field(..., gt=0)]
  Height : Annotated[float, Field(..., gt=0)]
  Sex : Annotated[str, Field(...)]
  Children : Annotated[int, Field()]
  Smoker : Annotated[str, Field(...)]
  Region : Annotated[str, Field(...)]

  @computed_field
  @property
  def bmi(self) -> float:
        return self.Weight / ((self.Height / 100) ** 2)


app = FastAPI()

@app.get("/")
def hello():
  return {"message" : "This is Insurance calculate API"}

@app.post("/predict")
def predict(data : UserInput):

  Region_convert = 0

  if data.Region == 'southeast':
    Region_convert = 0
  elif data.Region == 'southwest':
    Region_convert = 1
  elif data.Region == 'northwest':
    Region_convert = 2
  else:
    Region_convert = 3

  input_df = pd.DataFrame([{
  "Age" : data.Age,
  "Sex" : 0 if data.Sex == 'female' else 1,
  "bmi" : data.bmi,
  "Children" : data.Children,
  "Smoker" : 0 if data.Smoker == 'no' else 1,
  "Region" : Region_convert
  }])

  prediction = float(round(model.predict(input_df)[0], 2))

  return JSONResponse(status_code=200, content={"Predicted_Value":prediction})

