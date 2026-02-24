import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Raisin Prediction Apps")

Area = int(st.number_input("Enter area(int) : "))
MajorAxisLength = st.number_input("Enter Major Axis Length (float) : ")
MinorAxisLength = st.number_input("Enter Minor Axis Length (float) : ")
Eccentricity = st.number_input("Enter Eccentricity (float) : ")
ConvexArea = st.number_input("Enter Convex Area (float) : ")
Extent = st.number_input("Enter Extent (float) : ")
Perimeter = st.number_input("Enter Perimeter (float) : ")


if st.button("predict"):

  user_input = {
    "Area" : Area,
    "MajorAxisLength" : MajorAxisLength,
    "MinorAxisLength" : MinorAxisLength,
    "Eccentricity" : Eccentricity,
    "ConvexArea" : ConvexArea,
    "Extent" : Extent,
    "Perimeter" : Perimeter
  }

  try:
    response = requests.post(API_URL, json=user_input)
    result = response.json()

    if response.status_code == 200 and "prediction_value" in result:
      st.success(f"prediction : {result['prediction_value']}")
    
    else:
      st.error(f"API error : {response.status_code}")
  except requests.exceptions.ConnectionError:
    st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")