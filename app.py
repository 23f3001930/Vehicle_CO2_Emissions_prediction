import streamlit as st               #to run the code python -m streamlit run app.py
import pandas as pd
import pickle

# Load model and encoders
with open("model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
encoders = model_data["encoders"]

# Streamlit App UI
st.title("🚗 Vehicle CO2 Emissions Predictor")

st.markdown("Enter vehicle details below to predict CO2 emissions (g/km).")

# Input fields
make = st.selectbox("Make", options=encoders["Make"].classes_)
model_name = st.selectbox("Model", options=encoders["Model"].classes_)
vehicle_class = st.selectbox("Vehicle Class", options=encoders["Vehicle Class"].classes_)
engine_size = st.number_input("Engine Size(L)", min_value=0.0, step=0.1)
cylinders = st.number_input("Cylinders", min_value=1, step=1)
transmission = st.selectbox("Transmission", options=encoders["Transmission"].classes_)
fuel_type = st.selectbox("Fuel Type", options=encoders["Fuel Type"].classes_)
fuel_city = st.number_input("Fuel Consumption City (L/100 km)", min_value=0.0, step=0.1)
fuel_hwy = st.number_input("Fuel Consumption Hwy (L/100 km)", min_value=0.0, step=0.1)
fuel_comb_l = st.number_input("Fuel Consumption Comb (L/100 km)", min_value=0.0, step=0.1)
fuel_comb_mpg = st.number_input("Fuel Consumption Comb (mpg)", min_value=0.0, step=0.1)

if st.button("Predict CO2 Emissions"):
    try:
        # Prepare input data
        input_data = pd.DataFrame({
            'Make': [make],
            'Model': [model_name],
            'Vehicle Class': [vehicle_class],
            'Engine Size(L)': [engine_size],
            'Cylinders': [cylinders],
            'Transmission': [transmission],
            'Fuel Type': [fuel_type],
            'Fuel Consumption City (L/100 km)': [fuel_city],
            'Fuel Consumption Hwy (L/100 km)': [fuel_hwy],
            'Fuel Consumption Comb (L/100 km)': [fuel_comb_l],
            'Fuel Consumption Comb (mpg)': [fuel_comb_mpg],
        })

        # Encode categorical columns
        for col in ['Make','Model', 'Vehicle Class', 'Transmission', 'Fuel Type']:
            encoder = encoders[col]
            input_data[col] = encoder.transform(input_data[col])

        # Predict
        prediction = model.predict(input_data)
        st.success(f" Estimated CO2 Emissions: {prediction[0]:.2f} g/km")

    except Exception as e:
        st.error(f" Error during prediction: {e}")
