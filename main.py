import os
import uvicorn
from fastapi import FastAPI, Form
from twilio.twiml.voice_response import VoiceResponse
from dotenv import load_dotenv
import chromadb
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Load environment variables
load_dotenv()

# Define the FastAPI app
app = FastAPI()

# Configuration
CHROMA_DB_PATH = "data/chroma_db"
API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")

# Initialize the LLM and RAG chain
embedding_function = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vector_store = Chroma(
    persist_directory=CHROMA_DB_PATH,
    embedding_function=embedding_function
)
llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=API_KEY)
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=vector_store.as_retriever(),
    return_source_documents=True
)

@app.post("/voice")
async def handle_voice_request(SpeechResult: str = Form(...)):
    """
    Twilio webhook endpoint to handle incoming voice calls.
    It receives the transcribed speech and returns a TwiML response.
    """
    print(f"Received speech result: {SpeechResult}")
    
    if not SpeechResult:
        response_text = "Sorry, I didn't catch that. Please try again."
    else:
        try:
            # Get the response from the RAG chain
            result = rag_chain({"query": SpeechResult})
            response_text = result["result"]
            print(f"Generated response: {response_text}")
        except Exception as e:
            print(f"Error during RAG chain execution: {e}")
            response_text = "I am currently facing a technical issue. Please try again later."
    
    # Create TwiML response
    twiml_response = VoiceResponse()
    twiml_response.say(response_text, voice="Polly.Aditi")  # Using a suitable voice
    
    return twiml_response.to_xml()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
