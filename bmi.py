# -----------------------------
# BMI Calculator using Streamlit
# -----------------------------

import streamlit as st

# App Title
st.title("BMI Calculator Application")
st.write(
    "This application calculates **Body Mass Index (BMI)** "
    "and provides a health category based on standard BMI ranges."
)

# User Inputs
st.subheader("Enter Your Details")

height = st.number_input(
    "Height (in meters)",
    min_value=0.5,
    max_value=2.5,
    value=1.65
)

weight = st.number_input(
    "Weight (in kilograms)",
    min_value=10.0,
    max_value=300.0,
    value=60.0
)

# Calculate BMI
if st.button("Calculate BMI"):

    bmi = weight / (height ** 2)

    st.write(f"### Your BMI is: **{bmi:.2f}**")

    # BMI Categories
    if bmi < 18.5:
        st.warning(" Category: Underweight")
    elif 18.5 <= bmi < 25:
        st.success(" Category: Normal weight")
    elif 25 <= bmi < 30:
        st.info(" Category: Overweight")
    else:
        st.error(" Category: Obese")

# Footer Note
st.write(
    "---\n"
    " *BMI is a screening tool and does not replace professional medical advice.*"
)
