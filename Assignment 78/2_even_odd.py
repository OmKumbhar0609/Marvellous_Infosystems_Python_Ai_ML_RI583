# Even or Odd Number

import streamlit as st

st.title("Even or Odd Checker")

num = st.number_input("Enter an integer", step=1, value=0)

if st.button("Check"):
    if int(num) % 2 == 0:
        st.success("The number is Even")
    else:
        st.success("The number is Odd")
