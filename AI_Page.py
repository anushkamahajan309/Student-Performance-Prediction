import streamlit as st
import joblib

myAI = joblib.load("student_model.pkl")

st.title("🎓 Student Performance Prediction")

st.write(
    "Enter the student's details below to predict their final score."
)

study_hours = st.number_input(
    "Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)
attendance = st.number_input(
    "Attendance (%)",
    min_value=0,
    max_value=100,
    value=75
)
assignments = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=5
)
previous_score = st.number_input(
    "Previous Score",
    min_value=0,
    max_value=100,
    value=70
)

if st.button("Predict"):
    result = myAI.predict([[study_hours,attendance,assignments,previous_score]])
    st.write(result)