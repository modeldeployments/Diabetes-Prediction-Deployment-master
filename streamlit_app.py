import streamlit as st
import pickle
import numpy as np

st.set_page_config(
    page_title="Diabetes Predictor",
    page_icon="🩺"
)

# Load the Random Forest model
with open("diabetes-prediction-rfc-model.pkl", "rb") as file:
    classifier = pickle.load(file)

st.title("Diabetes Predictor")

st.write("This app uses a trained Random Forest model to predict diabetes.")

st.write("Please enter the following details:")

# Initialize prediction
if "prediction" not in st.session_state:
    st.session_state.prediction = None

# Reset function
def reset_form():
    st.session_state.pregnancies = None
    st.session_state.glucose = None
    st.session_state.bloodpressure = None
    st.session_state.skinthickness = None
    st.session_state.insulin = None
    st.session_state.bmi = None
    st.session_state.dpf = None
    st.session_state.age = None
    st.session_state.prediction = None

# Input fields
pregnancies = st.number_input(
    "Number of Pregnancies",
    min_value=0,
    max_value=20,
    step=1,
    value=None,
    placeholder="Number of Pregnancies eg. 0",
    key="pregnancies"
)

glucose = st.number_input(
    "Glucose (mg/dL)",
    min_value=0,
    max_value=300,
    step=1,
    value=None,
    placeholder="Glucose (mg/dL) eg. 80",
    key="glucose"
)

bloodpressure = st.number_input(
    "Blood Pressure (mmHg)",
    min_value=0,
    max_value=200,
    step=1,
    value=None,
    placeholder="Blood Pressure (mmHg) eg. 80",
    key="bloodpressure"
)

skinthickness = st.number_input(
    "Skin Thickness (mm)",
    min_value=0,
    max_value=100,
    step=1,
    value=None,
    placeholder="Skin Thickness (mm) eg. 20",
    key="skinthickness"
)

insulin = st.number_input(
    "Insulin Level (IU/mL)",
    min_value=0,
    max_value=900,
    step=1,
    value=None,
    placeholder="Insulin Level (IU/mL) eg. 80",
    key="insulin"
)

bmi = st.number_input(
    "Body Mass Index (kg/m²)",
    min_value=0.0,
    max_value=70.0,
    step=0.1,
    value=None,
    placeholder="Body Mass Index (kg/m²) eg. 23.1",
    key="bmi"
)

dpf = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    step=0.01,
    value=None,
    placeholder="Diabetes Pedigree Function eg. 0.52",
    key="dpf"
)

age = st.number_input(
    "Age (years)",
    min_value=1,
    max_value=120,
    step=1,
    value=None,
    placeholder="Age (years) eg. 34",
    key="age"
)

# Predict button
if st.button("Predict"):

    values = [
        pregnancies,
        glucose,
        bloodpressure,
        skinthickness,
        insulin,
        bmi,
        dpf,
        age
    ]

    if any(value is None for value in values):

        st.warning("Please enter all the values before making a prediction.")

    else:

        data = np.array([[
            pregnancies,
            glucose,
            bloodpressure,
            skinthickness,
            insulin,
            bmi,
            dpf,
            age
        ]])

        prediction = classifier.predict(data)

        st.session_state.prediction = prediction[0]

# Display prediction
if st.session_state.prediction is not None:

    if st.session_state.prediction == 1:
        st.error("Oops! You have DIABETES.")
    else:
        st.success("Great! You DON'T have diabetes.")

    st.button(
        "🔄 Try Another",
        on_click=reset_form
    )