# Student Result Calculator

import streamlit as st

st.title("Student Result Calculator")

name = st.text_input("Enter Student Name")
m1 = st.number_input("Subject 1 Marks", 0, 100, 0)
m2 = st.number_input("Subject 2 Marks", 0, 100, 0)
m3 = st.number_input("Subject 3 Marks", 0, 100, 0)

if st.button("Calculate Result"):
    total = m1 + m2 + m3
    percentage = total / 3

    st.write("Student Name:", name)
    st.write("Total Marks:", total, "/ 300")
    st.write(f"Percentage: {percentage:.2f}%")

    if m1 >= 40 and m2 >= 40 and m3 >= 40:
        st.success("Result: Pass")
    else:
        st.error("Result: Fail")
