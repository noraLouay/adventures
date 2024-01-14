import streamlit as st

def profile_page():
    st.header("User Profile")
    st.write("Welcome, user!")  # Replace with actual user data later

    if st.button("Create New Ad"):
        st.session_state.page = "create_ad"
        st.experimental_rerun()
