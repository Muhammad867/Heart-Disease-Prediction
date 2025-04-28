import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("heart_disease_model.pkl")

# Streamlit UI
st.title("💓 Heart Disease Prediction App")
st.write("Enter the patient details below to predict heart disease risk.")

# Numeric Inputs
age = st.number_input("Age", min_value=1, max_value=120, value=50)
resting_blood_pressure = st.number_input("Resting Blood Pressure", min_value=50, max_value=200, value=120)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=600, value=200)
max_heart_rate = st.number_input("Max Heart Rate Achieved", min_value=50, max_value=250, value=150)
oldpeak = st.slider("ST Depression Induced by Exercise", min_value=0.0, max_value=6.0, step=0.1, value=1.0)

# Categorical Inputs as Dropdowns
sex = st.selectbox("Sex", options=[0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
chest_pain_type = st.selectbox("Chest Pain Type", options=[0, 1, 2, 3], 
                               format_func=lambda x: ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"][x])
fasting_blood_sugar = st.selectbox("Fasting Blood Sugar", options=[0, 1], format_func=lambda x: "< 120 mg/ml" if x == 0 else "> 120 mg/ml")
rest_ecg = st.selectbox("Resting ECG", options=[0, 1, 2], 
                         format_func=lambda x: ["ST-T wave abnormality", "Normal", "Left ventricular hypertrophy"][x])
exercise_induced_angina = st.selectbox("Exercise-Induced Angina", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
slope = st.selectbox("Slope of Peak Exercise ST Segment", options=[0, 1, 2], 
                      format_func=lambda x: ["Downsloping", "Upsloping", "Flat"][x])
vessels_colored_by_fluoroscopy = st.selectbox("Number of Major Vessels", options=[0, 1, 2, 3, 4])
thalassemia = st.selectbox("Thalassemia Type", options=[0, 1, 2, 3], 
                            format_func=lambda x: ["Reversible Defect", "Fixed Defect", "Normal", "No"][x])

# Predict Button
if st.button("Predict"):
    # Prepare features for prediction
    features = np.array([[age, resting_blood_pressure, cholesterol, max_heart_rate, oldpeak,
                          sex, chest_pain_type, fasting_blood_sugar, rest_ecg, exercise_induced_angina,
                          slope, vessels_colored_by_fluoroscopy, thalassemia]])

    prediction = model.predict(features)
    result = "🚨 High Risk of Heart Disease" if prediction[0] == 1 else "✅ Low Risk of Heart Disease"
    st.subheader(result)