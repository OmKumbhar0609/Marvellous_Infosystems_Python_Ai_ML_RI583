# Celsius to Fahrenheit Converter

import streamlit as st

st.title("Celsius to Fahrenheit Converter")

celsius = st.number_input("Enter temperature in Celsius")

if st.button("Convert"):
    fahrenheit = (celsius * 9 / 5) + 32
    st.success(f"Temperature = {fahrenheit:.2f} °F")
