import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.title("Insurance Prediction Apps")

Age = int(st.number_input("Enter Age : ", min_value=0, max_value=120))
Weight = st.number_input("Enter Weight (kg) : ", min_value=0.0)
Height = st.number_input("Enter Height (cm) : ", min_value=0.0)
Sex = st.selectbox("Enter Sex : ", ['male', 'female'])
Children = int(st.number_input("Enter no. of Children : ", min_value=0, max_value=20))
Smoker = st.selectbox("Enter Smoker (yes/no) : ", ['yes', 'no'])
Region = st.selectbox("Enter Region : ", ['southeast', 'southwest', 'northwest', 'northeast'])

if st.button("Predict Insurance"):
  user_input = {
  "Age" : Age,
  "Weight" : Weight,
  "Height" : Height,
  "Sex" : Sex,
  "Children" : Children,
  "Smoker" : Smoker,
  "Region" : Region
  }

  try:

    response = requests.post(API_URL, json=user_input)

    result = response.json()

    if response.status_code == 200 and 'Predicted_Value' in result:
      st.success(f"Charges : {result['Predicted_Value']}")
    else:
      st.error("Api Error : ", response.status_code)

  except requests.exceptions.ConnectionError:
    st.error("❌ Could not connect to the FastAPI server. Make sure it's running.")
  