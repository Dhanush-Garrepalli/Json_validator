import streamlit as st
import json

st.title('JSON Validator and Formatter')
user_input = st.text_area("Enter your JSON here:", height=300)

if st.button('Validate and Format JSON'):
    try:
        json.loads(user_input)
        st.success('Valid JSON')
        st.text_area("Formatted JSON:", value=user_input, height=300, key='formatted_json')
    except ValueError as e:
        st.error(f'Invalid JSON: {e}')
