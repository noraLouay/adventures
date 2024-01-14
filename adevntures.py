import streamlit as st
from ad_display_page import ad_display_page
from registration_page import registration_page
from profile_page import profile_page
from create_ad_page import create_ad_page

page = st.session_state.get("page", "registration")

if page == "registration":
    registration_page()
elif page == "profile":
    profile_page()
elif page == "create_ad":
    create_ad_page()
elif page == "ad_display":
    ad_display_page()
