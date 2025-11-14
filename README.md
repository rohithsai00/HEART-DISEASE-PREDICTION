# Heart Disease Predictor

A machine learning application that predicts the risk of heart disease using the **Framingham Heart Study dataset**. The project includes an interactive **Streamlit UI** for easy input and prediction.

---

## Table of Contents

- [Overview](#overview)  
- [Features](#features)  
- [Dataset](#dataset)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Technologies Used](#technologies-used)  
- [Model Details](#model-details)  
- [Contributing](#contributing)  
- [License](#license)  

---

## Overview

Heart disease is a leading cause of death globally. Early prediction can help prevent complications. This project uses machine learning to estimate the risk of heart disease based on patient health parameters.

---

## Features

- Predicts the likelihood of heart disease (`High Risk` or `Low Risk`).  
- User-friendly **Streamlit interface** for entering health data.  
- Outputs a prediction along with the probability score.  

---

## Dataset

- Dataset: **Framingham Heart Study dataset**  
- Features include:  
  - Age  
  - Sex  
  - Total cholesterol  
  - Systolic blood pressure  
  - Smoking status  
  - Diabetes  
  - Body Mass Index (BMI)  
  - Other cardiovascular risk factors  

Source: [Framingham Heart Study Dataset](https://www.kaggle.com/datasets/amanajmera1/framingham-heart-study-dataset)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/heart-disease-predictor.git
Navigate to the project folder:

bash
Copy code
cd heart-disease-predictor
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
Run the Streamlit app:

bash
Copy code
streamlit run app.py
Enter patient health details in the input fields.

Click Predict to see the risk of heart disease.

Technologies Used
Python

Pandas & NumPy for data handling

Scikit-learn for machine learning models

Streamlit for interactive UI

Matplotlib/Seaborn for visualizations
