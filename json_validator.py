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

# Simulated visitor count - for demonstration purposes
if 'visitor_count' not in st.session_state:
    st.session_state.visitor_count = 1  # Initialize with 1 at the first load
else:
    st.session_state.visitor_count += 1  # Increment on each run

st.markdown(f"### Visitor Count: {st.session_state.visitor_count}")
st.markdown("Created by Dhanush Garrepalli")
