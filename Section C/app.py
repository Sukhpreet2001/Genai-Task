import streamlit as st
import requests

# Define the URL of your deployed FastAPI app on Google Cloud Run
api_url = "http://localhost:8080/query/"

# Function to query the API with the user's input
def query_api(query_text):
    response = requests.post(api_url, json={"query": query_text})
    return response.json()

# Streamlit app layout
st.title("Document Query Interface")

# Input for the query
query_text = st.text_input("Enter your query:")

# Button to trigger the query
if st.button("Search"):
    if query_text:
        # Query the API
        response_json = query_api(query_text)

        # Extract the documents from the response
        documents = response_json.get("documents", [[]])[0]
        
        if documents:
            st.subheader("Search Results:")
            for doc in documents:
                st.write(doc)
        else:
            st.write("No documents found.")
    else:
        st.write("Please enter a query.")

