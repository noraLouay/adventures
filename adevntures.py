import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Customer Registration",
    page_icon="",  # Choose a suitable icon
    layout="centered",
    initial_sidebar_state="expanded",
)

# Set theme
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;  /* White background */
        color: #ff0000;             /* Red text */
        font-family: Arial, sans-serif;
    }
    .st-bf {
        font-weight: bold;
    }
    .st-header {
        background-color: #ff0000;  /* Red header background */
        color: #ffffff;             /* White text on header */
        padding: 10px;
    }
    .st-form-label {
        color: #ff0000;
    }
    .st-form-input {
        border-color: #ff0000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create form header
st.header("Customer Registration")

# Form elements
name = st.text_input("Name", placeholder="Enter your name")
gender = st.radio("Gender", options=["Male", "Female", "Other"])
phone_number = st.text_input("Phone Number", placeholder="Enter your phone number")
age_range = st.selectbox("Age Range", options=["18-24", "25-34", "35-44", "45-54", "55+"])

# Submit button
if st.button("Register"):
    # Write user information to a file
    with open("customer_data.txt", "a") as f:
        f.write(f"Name: {name}\nGender: {gender}\nPhone Number: {phone_number}\nAge Range: {age_range}\n\n")
    st.success("Registration successful!")
