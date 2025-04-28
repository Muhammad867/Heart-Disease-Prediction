💓 Heart Disease Prediction App
This project is a Machine Learning-powered Streamlit web application that predicts a patient's risk of heart disease based on several health-related features.

📂 Project Structure
Heart Disease Prediction.ipynb — Jupyter notebook used to train and evaluate the heart disease prediction model.

HeartDiseaseTrain-Test.csv — Dataset containing patient information used for training and testing the model.

app.py — Streamlit web application to interactively predict heart disease risk based on user input.

heart_disease_model.pkl — Pre-trained machine learning model saved via joblib (must be present in the same directory).

🛠️ Features
Collects user input (age, blood pressure, cholesterol, etc.) through an interactive web interface.

Predicts whether a patient has a high risk or low risk of heart disease.

Simple, clean UI built with Streamlit.

📊 Input Fields
Age

Resting Blood Pressure

Cholesterol Level

Max Heart Rate Achieved

ST Depression (Oldpeak)

Sex

Chest Pain Type

Fasting Blood Sugar

Resting ECG Results

Exercise-Induced Angina

Slope of Peak Exercise ST Segment

Number of Major Vessels Colored by Fluoroscopy

Thalassemia Type

🚀 How to Run the App
Clone the repository or download the project files.

Make sure you have the required Python packages installed:
pip install streamlit joblib numpy scikit-learn pandas

Ensure that the model file heart_disease_model.pkl is present in the same directory as app.py. If not, run the training notebook Heart Disease Prediction.ipynb to generate it.

Run the Streamlit app:
streamlit run app.py

Open the provided local URL in your browser to use the app.

📈 Model Training
The model is trained using a dataset (HeartDiseaseTrain-Test.csv) containing patient records with various clinical attributes. Key steps:

Data preprocessing

Feature selection

Model training (likely a classification algorithm — exact model type can be verified in the notebook)

Saving the model with joblib

📋 Requirements
Python 3.7+

Streamlit

scikit-learn

pandas

numpy

joblib

⚠️ Important
The app uses categorical encoding via dropdowns to match the model's expectations (e.g., sex encoded as 0 or 1).

Some field descriptions (like thalassemia types) are mapped manually in the UI for user-friendly selection.

✨ Future Improvements
Improve model accuracy using hyperparameter tuning.

Add model explainability (e.g., SHAP plots).

Deploy the app to platforms like Streamlit Cloud, AWS, or Heroku.
