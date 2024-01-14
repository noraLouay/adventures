import streamlit as st
import os
import json
import subprocess


def create_ad_page():
    st.header("Create Ad")

    uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])
    prompt = st.text_area("Ad Prompt")

    if st.button("Generate"):
        if uploaded_file is not None:
            # Create ads directory if it doesn't exist
            if not os.path.exists("ads"):
                os.mkdir("ads")
            if not os.path.exists("ads/images"):
                os.mkdir("ads/images")

            # Save image
            with open(f"ads/images/{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Save prompt to ads.json
            with open("ads.json", "r") as f:
                ads = json.load(f) or []
            ads.append({"image_path": f"ads/images/{uploaded_file.name}", "prompt": prompt})
            with open("ads.json", "w") as f:
                json.dump(ads, f)

        st.success("Ad created successfully!")
        try:
            subprocess.run(["python", "test_script.py"])  # Replace with the actual path
            st.info("Additional script execution complete!")
        except subprocess.CalledProcessError as e:
            st.error(f"Error running script: {e}")
        st.session_state.page = "ad_display"
        st.session_state.ad_image_path = f"ads/images/{uploaded_file.name}"  # Store image path
        st.experimental_rerun()
    if st.sidebar.button("Back to Profile"):
        st.session_state.page = "profile"
        st.experimental_rerun()


