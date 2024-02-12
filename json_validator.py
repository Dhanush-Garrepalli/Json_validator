import streamlit as st
import json

# Streamlit application layout
st.title('JSON Validator')

# Initialize or update the session state for the text area
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ""

# Text area for user to input JSON, bound to the session state
user_input = st.text_area("Enter your JSON here:", value=st.session_state['user_input'], height=300)

# Button to validate JSON
if st.button('Validate JSON'):
    try:
        # Attempt to load the JSON data
        json.loads(user_input)
        # If successful, indicate valid JSON
        st.success('Valid JSON')
    except ValueError as e:
        # If error, display it to the user
        st.error(f'Invalid JSON: {e}')

# Button to clear the user input
if st.button('Clear'):
    # Clear the text area by setting its value in the session state to an empty string
    st.session_state['user_input'] = ""
    # Use st.experimental_rerun() to refresh the page and reflect the cleared state
    st.experimental_rerun()
