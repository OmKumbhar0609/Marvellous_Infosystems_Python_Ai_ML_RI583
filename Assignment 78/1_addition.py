# Addition of Two Numbers

import streamlit as st

st.title("Addition of Two Numbers")

num1 = st.number_input("Enter first number:")
num2 = st.number_input("Enter second number:")

if st.button("Add"):
    result = num1 + num2
    st.success(f"Addition = {result}")
