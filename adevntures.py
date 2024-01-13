# main.py

import streamlit as st

page = st.session_state.get("page", "registration")

if page == "registration":
    import registration_page
elif page == "user_data":
    import user_data_page
