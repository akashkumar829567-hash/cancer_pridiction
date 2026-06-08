import streamlit as st
import pandas as pd
import joblib

# Load Model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# Page Configuration
st.set_page_config(
    page_title="Lung Cancer Prediction",
    page_icon="🫁",
    layout="centered"
)

st.title("🫁 Lung Cancer Prediction System")
st.write("Enter the patient's details and click Predict.")

# User Inputs
gender = st.selectbox("Gender", ["Male", "Female"])
age = st.slider("Age", 1, 100, 30)

gender = 1 if gender == "Male" else 0

# Dataset uses 1 = No, 2 = Yes
smoking = st.selectbox("Smoking", ["No", "Yes"])
yellow_fingers = st.selectbox("Yellow Fingers", ["No", "Yes"])
anxiety = st.selectbox("Anxiety", ["No", "Yes"])
peer_pressure = st.selectbox("Peer Pressure", ["No", "Yes"])
chronic_disease = st.selectbox("Chronic Disease", ["No", "Yes"])
fatigue = st.selectbox("Fatigue", ["No", "Yes"])
allergy = st.selectbox("Allergy", ["No", "Yes"])
wheezing = st.selectbox("Wheezing", ["No", "Yes"])
alcohol = st.selectbox("Alcohol Consuming", ["No", "Yes"])
coughing = st.selectbox("Coughing", ["No", "Yes"])
shortness_breath = st.selectbox("Shortness of Breath", ["No", "Yes"])
swallowing_difficulty = st.selectbox("Swallowing Difficulty", ["No", "Yes"])
chest_pain = st.selectbox("Chest Pain", ["No", "Yes"])

# Convert Yes/No to Dataset Format (1/2)
def convert(value):
    return 2 if value == "Yes" else 1

if st.button("Predict"):

    data = pd.DataFrame({
        "GENDER": [gender],
        "AGE": [age],
        "SMOKING": [convert(smoking)],
        "YELLOW_FINGERS": [convert(yellow_fingers)],
        "ANXIETY": [convert(anxiety)],
        "PEER_PRESSURE": [convert(peer_pressure)],
        "CHRONIC_DISEASE": [convert(chronic_disease)],
        "FATIGUE": [convert(fatigue)],
        "ALLERGY": [convert(allergy)],
        "WHEEZING": [convert(wheezing)],
        "ALCOHOL_CONSUMING": [convert(alcohol)],
        "COUGHING": [convert(coughing)],
        "SHORTNESS_OF_BREATH": [convert(shortness_breath)],
        "SWALLOWING_DIFFICULTY": [convert(swallowing_difficulty)],
        "CHEST_PAIN": [convert(chest_pain)]
    })

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Lung Cancer")
    else:
        st.success("✅ Low Risk of Lung Cancer")

    # Probability (KNN supports predict_proba)
    try:
        probability = model.predict_proba(data)
        st.write(f"Prediction Confidence: **{max(probability[0])*100:.2f}%**")
    except:
        pass
