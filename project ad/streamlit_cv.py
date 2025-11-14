import streamlit as st
import joblib
import pandas as pd

# Custom CSS to add a background image
st.markdown(
    """
        <style>
        .stApp {
            background-image: url("D:\\ET1 AD\\et1\\project ad\\wall.py");
            background-size: cover;
            background-position: center;
        }
        </style>
        """
    ,
    unsafe_allow_html=True
)

# Title and description
st.title("Heart Disease Prediction")
st.write("Please fill out the following form to predict your 10-year risk of developing heart disease.")

# Create a form for user input
with st.form("heart_disease_form"):
    col1, col2, col3 = st.columns(3)

    # Input fields
    gender = col1.selectbox("Enter your gender", ["Male", "Female"])
    male = col1.selectbox("Are you male?", ["Yes", "No"])
    age = col2.number_input("Enter your age", min_value=1, max_value=120, step=1)
    education = col3.selectbox("Highest academic qualification",
                               ["High school diploma", "Undergraduate degree", "Postgraduate degree", "PhD"])

    isSmoker = col1.selectbox("Are you currently a smoker?", ["Yes", "No"])
    yearsSmoking = col2.number_input("Number of cigarettes per week ", min_value=0, max_value=100, step=1)
    BPMeds = col3.selectbox("Are you currently on BP medication?", ["Yes", "No"])

    stroke = col1.selectbox("Have you ever experienced a stroke?", ["Yes", "No"])
    hyp = col2.selectbox("Do you have hypertension?", ["Yes", "No"])
    diabetes = col3.selectbox("Do you have diabetes?", ["Yes", "No"])

    chol = col1.number_input("Enter your cholesterol level", min_value=50, max_value=500, step=1)
    sys_bp = col2.number_input("Enter your systolic blood pressure", min_value=50, max_value=250, step=1)
    dia_bp = col3.number_input("Enter your diastolic blood pressure", min_value=30, max_value=150, step=1)

    bmi = col1.number_input("Enter your BMI", min_value=10.0, max_value=60.0, step=0.1)
    heart_rate = col2.number_input("Enter your resting heart rate", min_value=30, max_value=200, step=1)
    glucose = col3.number_input("Enter your glucose level", min_value=50, max_value=500, step=1)

    # Submit button for the form
    submit_button = st.form_submit_button(label='Predict')

# Convert the user input into a DataFrame for prediction
if submit_button:
    df_pred = pd.DataFrame([[male, age, education, isSmoker, yearsSmoking, BPMeds, stroke, hyp, diabetes, chol, sys_bp,
                             dia_bp, bmi, heart_rate, glucose]],
                           columns=['male', 'age', 'education', 'currentSmoker', 'cigsPerDay', 'BPMeds',
                                    'prevalentStroke', 'prevalentHyp', 'diabetes', 'totChol', 'sysBP', 'diaBP', 'BMI',
                                    'heartRate', 'glucose'])

    # Process input data
    df_pred['male'] = df_pred['male'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['prevalentHyp'] = df_pred['prevalentHyp'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['prevalentStroke'] = df_pred['prevalentStroke'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['diabetes'] = df_pred['diabetes'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['BPMeds'] = df_pred['BPMeds'].apply(lambda x: 1 if x == 'Yes' else 0)
    df_pred['currentSmoker'] = df_pred['currentSmoker'].apply(lambda x: 1 if x == 'Yes' else 0)


    # Transform education to numeric
    def transform_education(data):
        if data == 'High school diploma':
            return 0
        elif data == 'Undergraduate degree':
            return 1
        elif data == 'Postgraduate degree':
            return 2
        elif data == 'PhD':
            return 3
        return 3


    df_pred['education'] = df_pred['education'].apply(transform_education)

    # Load the model and make a prediction
    model = joblib.load('fhs_rf_model.pkl')
    prediction = model.predict(df_pred)

    # Display prediction result
    if prediction[0] == 0:
        st.success('You likely will not develop heart disease in 10 years.')
    else:
        st.warning('You are likely to develop heart disease in 10 years.')
