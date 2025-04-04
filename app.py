import streamlit as st
import pandas as pd  # ✅ Import pandas
import os
import pickle
# Import the functions or code from your downloaded Google Colab script
#file_path = pd.read_csv(r"C:\Users\mgm_c\Downloads\Vehicle_CO2_Emissions_prediction\vehicle_co2_emissions_prediction.csv")
#file_path = r"C:\Vehicle_CO2_Emissions_prediction"
#from (C:\Users\mgm_c\Downloads\Vehicle_CO2_Emissions_prediction.py import your_function()
# Set up Streamlit UI
#st.title("Streamlit and Colab Integration")
#st.write("This is a demo app")

# Call a function from your Colab code
#result = vehicle_co2_emissions_prediction # Example of calling a function from the Colab code
#st.write(df.head())  # Display the result
#if os.path.exists(file_path):
    ##st.title("Vehicle_CO2_Emissions_prediction")
    #st.write("### Data Preview:")
    #st.write(df.head())  # Display first 5 rows
#else:
   # st.error(f" File not found: {file_path}. Please check the file location.")

import streamlit as st
import pandas as pd
import os

# Specify the path to your CSV file
file_path = r"C:\Vehicle_CO2_Emissions_prediction\vehicle_co2_emissions_prediction.csv"

# Set up Streamlit UI
st.title("Vehicle CO2 Emissions Prediction")
st.write("This is a demo app for Vehicle CO2 Emissions prediction.")

# Check if the file exists and load the data
if os.path.exists(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    st.write("### Data Preview:")
    st.write(df.head())  # Display first 5 rows of the data
else:
    st.error(f"File not found: {file_path}. Please check the file location.")
