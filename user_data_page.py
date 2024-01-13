# user_data_page.py

import streamlit as st

st.set_page_config(page_title="Registered Users")

# Read user data from file
with open("customer_data.txt", "r") as f:
    user_data = f.readlines()

# Display user data in a clear and informative way
for user in user_data:
    st.write("---")  # Visual separator between users
    st.write(user.strip())  # Remove trailing newline

if st.sidebar.button("Back to Registration"):
    st.session_state.page = "registration"
    st.experimental_rerun()
