import gradio as gr
import requests

# Function to query your API
def query_api(question):
    response = requests.post("YOUR_API_ENDPOINT", json={"question": question})
    if response.status_code == 200:
        return response.json().get("result", "No result found")
    else:
        return "Error querying the API"

# Create the Gradio interface
iface = gr.Interface(
    fn=query_api,
    inputs="text",
    outputs="text",
    title="Query Interface",
    description="Enter a question to query the Chroma database"
)

if __name__ == "__main__":
    iface.launch()
