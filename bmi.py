import streamlit as st

st.title('BMI Calculator')

# Input for height and weight
weight = st.number_input('Enter your weight in kilograms (kg):', min_value=0.1, max_value=500.0, value=70.0, step=0.1)
height = st.number_input('Enter your height in meters (m):', min_value=0.1, max_value=3.0, value=1.75, step=0.01)

# Calculate BMI
if st.button('Calculate BMI'):
    if height > 0:
        bmi = weight / (height ** 2)
        st.write(f'Your BMI is: {bmi:.2f}')

        # Interpret BMI
        if bmi < 18.5:
            st.write('Category: Underweight')
        elif 18.5 <= bmi < 24.9:
            st.write('Category: Normal weight')
        elif 25 <= bmi < 29.9:
            st.write('Category: Overweight')
        else:
            st.write('Category: Obesity')
    else:
        st.write('Height cannot be zero.')