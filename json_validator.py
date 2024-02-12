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

'''
if 'visitor_count' not in st.session_state:
    st.session_state['visitor_count'] = 1
else:

    st.session_state['visitor_count'] += 1

footer = """<div style='text-align: center;'>
                <p style='margin: 0; padding-bottom: 2rem;'>Visitor Count: {} | Dhanush Garrepalli</p>
            </div>""".format(st.session_state.get('visitor_count', 1))
st.markdown(footer, unsafe_allow_html=True)'''
