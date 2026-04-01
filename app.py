import streamlit as st
import pandas as pd
import pickle
import os

# Title (ALWAYS OUTSIDE any condition)
st.title("Heart Disease Risk Predictor")

st.write("App is running...")

# Load model
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

# Inputs
col1, col2, col3 = st.columns(3)

with col1:
    age = st.slider("Age", 20, 80, 40)
    cholesterol = st.slider("Cholesterol", 100, 400, 200)
    fasting_bs = st.selectbox("Fasting BS (>120)", [0, 1])
    
with col2:
    resting_bp = st.slider("Resting BP", 80, 200, 120)
    max_hr = st.slider("Max HR", 50, 220, 150)
    oldpeak = st.slider("Oldpeak (ST depression)", 0.0, 6.0, 1.0)
    
with col3:
    sex_m = st.selectbox("Sex", ["Female", "Male"])
    sex_m = 1 if sex_m == "Male" else 0
    chest_pain = st.selectbox("Chest Pain Type", ["ASY", "ATA", "NAP", "TA"])
    exercise_angina = st.selectbox("Exercise Angina", ["No", "Yes"])
    exercise_angina = 1 if exercise_angina == "Yes" else 0

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    resting_ecg = st.selectbox("Resting ECG", ["Normal", "LVH", "ST"])
    
with col2:
    st_slope = st.selectbox("ST Slope", ["Down", "Flat", "Up"])

# Encode categorical variables
chest_pain_ata = 1 if chest_pain == "ATA" else 0
chest_pain_nap = 1 if chest_pain == "NAP" else 0
chest_pain_ta = 1 if chest_pain == "TA" else 0

resting_ecg_normal = 1 if resting_ecg == "Normal" else 0
resting_ecg_st = 1 if resting_ecg == "ST" else 0

st_slope_flat = 1 if st_slope == "Flat" else 0
st_slope_up = 1 if st_slope == "Up" else 0

# Prepare input with the same feature names used during model training.
input_data = pd.DataFrame(
    [
        {
            "Age": age,
            "RestingBP": resting_bp,
            "Cholesterol": cholesterol,
            "FastingBS": fasting_bs,
            "MaxHR": max_hr,
            "Oldpeak": oldpeak,
            "Sex_M": sex_m,
            "ChestPainType_ATA": chest_pain_ata,
            "ChestPainType_NAP": chest_pain_nap,
            "ChestPainType_TA": chest_pain_ta,
            "RestingECG_Normal": resting_ecg_normal,
            "RestingECG_ST": resting_ecg_st,
            "ExerciseAngina_Y": exercise_angina,
            "ST_Slope_Flat": st_slope_flat,
            "ST_Slope_Up": st_slope_up,
        }
    ]
)

# Predict
if st.button("Predict Risk"):
    prob = model.predict_proba(input_data)[0][1]

    threshold = 0.4
    prediction = 1 if prob >= threshold else 0

    if prediction == 1:
        st.error(f"High Risk ({prob:.2f})")
    else:
        st.success(f"Low Risk ({prob:.2f})")

    st.write("Probability:", round(prob, 3))
