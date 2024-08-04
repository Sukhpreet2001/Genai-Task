from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import chromadb
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Load Chroma client
client = chromadb.PersistentClient(path=r'C:\Users\Sukhpreet Kaur\Documents\Genai Task\local_db')

collection = client.get_or_create_collection(name="pdf_texts")

# Initialize the model
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

class QueryRequest(BaseModel):
    query: str

@app.post("/query/")
async def query_collection(request: QueryRequest):
    query_text = request.query
    query_embedding = model.encode([query_text])
    
    results = collection.query(
        query_embeddings=query_embedding,
        n_results=5  # Adjust as needed
    )
    
    print("Query Results:", results)  # Add this line to log results

    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    
    return results