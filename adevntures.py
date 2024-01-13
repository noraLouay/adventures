# Import the Streamlit library
import streamlit as st

# Define the main function for the Streamlit app
def main():
    # Set the title of the app
    st.title("Simple Square Calculator")

    # Add a text input for the user to enter a number
    user_input = st.number_input("Enter a number:")

    # Calculate the square of the entered number
    square_result = user_input ** 2

    # Display the result
    st.write(f"The square of {user_input} is: {square_result}")

# Run the Streamlit app
if __name__ == "__main__":
    main()
