import fitz  # PyMuPDF
from chromadb import PersistentClient
from dotenv import load_dotenv
import os

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text += page.get_text()
    return text

# Load environment variables
load_dotenv('.env.local')
storage_path = os.getenv('STORAGE_PATH')
if storage_path is None:
    raise ValueError('STORAGE_PATH environment variable is not set')

# Initialize Chroma client with persistent storage
client = PersistentClient(path=storage_path)

# Extract text from PDF
pdf_text = extract_text_from_pdf('sample.pdf')

# Create or get the collection
collection = client.get_or_create_collection(name="pdf_texts")

# Add text to collection without generating embeddings
collection.add(
    documents=[pdf_text],
    metadatas=[{"source": "R20CSE3122-Artificial-Intelligence.pdf"}],
    ids=["pdf1"]
)

# Verify the collection count
print(collection.count())
