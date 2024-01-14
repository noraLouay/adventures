import streamlit as st
from PIL import Image
# from streamlit_extras.buttons import st_download_button

def ad_display_page():
    image_path = st.session_state.get("ad_image_path")
    # ad_prompt = st.session_state.get("ad_prompt")  # Add if storing prompt data

    if image_path:
        image = Image.open(image_path)
        st.image(image)

        # Download button using st_download_button from streamlit-extras
        # st_download_button(image, f"ad-{image_path.split('/')[-1]}")  # Customize button text and filename
    if st.sidebar.button("Back to Profile"):
        st.session_state.page = "profile"
        st.experimental_rerun()
