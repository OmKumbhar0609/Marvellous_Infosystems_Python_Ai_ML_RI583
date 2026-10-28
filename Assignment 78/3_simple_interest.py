# Simple Interest Calculator

import streamlit as st

st.title("Simple Interest Calculator")

principal = st.number_input("Principal Amount", min_value=0.0)
rate = st.number_input("Rate of Interest (%)", min_value=0.0)
time = st.number_input("Time Period (Years)", min_value=0.0)

if st.button("Calculate"):
    interest = (principal * rate * time) / 100
    st.success(f"Simple Interest = {interest:.2f}")
