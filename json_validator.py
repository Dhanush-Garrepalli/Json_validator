import streamlit as st
import json

st.title('JSON Validator and Formatter')

# Create two columns for the layout
col1, col2 = st.columns(2)

# User input text area in the left column
with col1:
    user_input = st.text_area("Enter your JSON here:", height=300, key='user_input')

# Button and output in the right column
with col2:
    if st.button('Validate and Format JSON'):
        try:
            # Parse the JSON to validate it and then format it with indentation
            parsed_json = json.loads(user_input)
            formatted_json = json.dumps(parsed_json, indent=4)
            st.success('Valid JSON')
            # Display the formatted JSON in the right column
            st.text_area("Formatted JSON:", value=formatted_json, height=300, key='formatted_json')
        except ValueError as e:
            st.error(f'Invalid JSON: {e}')

