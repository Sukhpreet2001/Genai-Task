import streamlit as st
import requests

st.title('Query Vector Database')

# Input field for the user to enter a query
query = st.text_input('Enter your query:')

# Button to submit the query
if st.button('Submit'):
    if query:
        try:
            # Send POST request to your FastAPI endpoint
            response = requests.post('YOUR_API_URL/query', json={'query': query})
            response.raise_for_status()  # Check for HTTP errors
            result = response.json()  # Parse JSON response
            
            # Display the result
            st.write('Result:', result)
        except requests.exceptions.RequestException as e:
            st.error(f'Error querying the API: {e}')
    else:
        st.write('Please enter a query.')
