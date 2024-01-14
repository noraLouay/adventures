import streamlit as st
import json

def registration_page():
    st.header("Registration")

    email = st.text_input("Email")
    name = st.text_input("Name")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        # Validate input (optional)
        if not email or not name or not password:
            st.error("Please fill in all fields")
            return

        # Build user data
        user_data = {
            "email": email,
            "name": name,
            "password": password,
        }

        # Write data to JSON file
        with open("users.json", "w") as f:
            json.dump(user_data, f)

        # Success message and redirect to profile page
        st.success("Registration successful!")
        st.session_state.page = "profile"
        st.experimental_rerun()
