import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model.pkl")

st.set_page_config(page_title="Lung Cancer Prediction", page_icon="🫁")

st.title("🫁 Lung Cancer Prediction System")

gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 1, 100, 30)

gender = 1 if gender == "Male" else 0

smoking = st.selectbox("Smoking", [1, 2])
yellow_fingers = st.selectbox("Yellow Fingers", [1, 2])
anxiety = st.selectbox("Anxiety", [1, 2])
peer_pressure = st.selectbox("Peer Pressure", [1, 2])
chronic_disease = st.selectbox("Chronic Disease", [1, 2])
fatigue = st.selectbox("Fatigue", [1, 2])
allergy = st.selectbox("Allergy", [1, 2])
wheezing = st.selectbox("Wheezing", [1, 2])
alcohol = st.selectbox("Alcohol Consuming", [1, 2])
coughing = st.selectbox("Coughing", [1, 2])
shortness_breath = st.selectbox("Shortness of Breath", [1, 2])
swallowing_difficulty = st.selectbox("Swallowing Difficulty", [1, 2])
chest_pain = st.selectbox("Chest Pain", [1, 2])

if st.button("Predict"):

    data = pd.DataFrame({
        "GENDER":[gender],
        "AGE":[age],
        "SMOKING":[smoking],
        "YELLOW_FINGERS":[yellow_fingers],
        "ANXIETY":[anxiety],
        "PEER_PRESSURE":[peer_pressure],
        "CHRONIC_DISEASE":[chronic_disease],
        "FATIGUE":[fatigue],
        "ALLERGY":[allergy],
        "WHEEZING":[wheezing],
        "ALCOHOL_CONSUMING":[alcohol],
        "COUGHING":[coughing],
        "SHORTNESS_OF_BREATH":[shortness_breath],
        "SWALLOWING_DIFFICULTY":[swallowing_difficulty],
        "CHEST_PAIN":[chest_pain]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Lung Cancer")
    else:
        st.success("✅ Low Risk of Lung Cancer")