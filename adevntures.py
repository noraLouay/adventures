import streamlit as st

# Session state to track the current page
page = st.session_state.get("page", "registration")

# Registration page
if page == "registration":
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
        color: #000000;             /* Black text */
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
        color: #000000;
    }
    .st-form-input {
        border-color: #000000;
    }
    .st-button {
        background-color: #008000;  /* Green button background */
        color: #ffffff;             /* White text on button */
        border-color: #000000;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
    }
    .st-button:hover {
        background-color: #00a000;  /* Darker green on hover */
    }
    .st-success {
        color: #008000;  /* Green success message */
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

    # Navigation button
    if st.sidebar.button("View Registered Users"):
        st.session_state.page = "user_data"
        st.experimental_rerun()

# User data page
elif page == "user_data":
    st.set_page_config(page_title="Registered Users")

    # Read user data from file
    with open("customer_data.txt", "r") as f:
        user_data = f.readlines()

    # Display user data in a clear and informative way
    for user in user_data:
        st.write("---")  # Visual separator between users
        st.write(user.strip())  # Remove trailing newline

    # Navigation button (optional)
    if st.sidebar.button("Back to Registration"):
        st.session_state.page = "registration"
        st.experimental_rerun()
