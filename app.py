import streamlit as st
import numpy as np
import pickle

st.title("Taxi Demand Prediction App")

model = pickle.load(open("taxi_model.pkl", "rb"))

st.write("Enter previous 3 hours of demand values")

lag_1 = st.number_input("Demand 1 hour ago", min_value=0)
lag_2 = st.number_input("Demand 2 hours ago", min_value=0)
lag_3 = st.number_input("Demand 3 hours ago", min_value=0)

if st.button("Predict"):
    x = np.array([[lag_1, lag_2, lag_3]])
    pred = model.predict(x)[0]
    st.success(f"Predicted next hour demand: {int(pred)}")
