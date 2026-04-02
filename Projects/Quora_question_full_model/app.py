import streamlit as st
import helper
import pickle

# Load the model
model = pickle.load(open("models/xgb_with_test.pkl", "rb"))


# Streamlit app header
st.header("Quora Question Pair")

# Input fields for the questions
q1 = st.text_input("Enter question number 1")
q2 = st.text_input("Enter question number 2")

# Button to trigger the prediction
if st.button("Find"):
    # Create a query point for the model
    query = helper.query_point_creator(q1, q2)
    
    # Predict if the questions are duplicates
    result = model.predict(query)[0]
    
    # Display the result
    if result:
        st.header("Duplicate")
    else:
        st.header("Not Duplicate")
