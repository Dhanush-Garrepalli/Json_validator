import streamlit as st
import json

# Streamlit application layout
st.title('JSON Validator and Formatter')

# Text area for user to input JSON
user_input = st.text_area("Enter your JSON here:", height=300)

# Button to validate and format JSON
if st.button('Validate and Format JSON'):
    try:
        # Attempt to load the JSON data
        parsed_json = json.loads(user_input)
        # If successful, display the formatted JSON
        st.json(parsed_json)
        st.success('Valid JSON')
    except ValueError as e:
        # If error, display it to the user
        st.error(f'Invalid JSON: {e}')
