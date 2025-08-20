# Krishi-Vani: An AI-Powered Agricultural Advisory System 🧑‍🌾

Krishi-Vani is a voice-first AI assistant designed to provide timely and actionable agricultural advice to farmers in rural India. By leveraging publicly available data and a powerful Retrieval-Augmented Generation (RAG) pipeline, the system delivers critical information on weather forecasts, crop prices, and pest advisories directly to farmers' mobile phones. Our goal is to bridge the information gap and empower farmers with the knowledge they need to improve crop yields and profitability.

## 🚀 Key Features

- **Voice-Based Interface:** Farmers can call a toll-free number and ask questions in natural language.
- **Intelligent Responses:** The system provides intelligent, context-aware answers by referencing a comprehensive knowledge base.
- **Multi-Source Data:** Integrates public data from key government portals to provide reliable information.
- **Proactive Alerts:** Can be extended to send proactive SMS alerts about extreme weather or market price fluctuations.

## 🛠️ Setup and Installation

### Prerequisites

- To run this project, you will need the following installed on your local machine:
- Python 3.8 or higher
- pip (Python package installer)
- ngrok (for exposing your local server to the internet)
- A **Twilio** account with a voice-enabled phone number.

### Installation Steps

- **Clone the Repository**

    ```
    git clone https://github.com/your-username/krishi-vaani.git
    cd krishi-vani
    ```
- **Create a Virtual Environment:**

  ```
  python -m venv venv
  # On Windows:
  # venv\Scripts\activate
  # On macOS/Linux:
  source venv/bin/activate
  ```
- **Install Dependencies:**

  ```
  pip install -r requirements.txt
  ```
  The requirements.txt file contains all the necessary libraries: ```fastapi```, ```uvicorn```, ```twilio```, ```python-dotenv```, ```langchain```, ```chromadb```, ```sentence-transformers```.
  
- **Set Up Environment Variables:**

  Create a ```.env``` file in the root directory and add your Twilio credentials.

  ```
  TWILIO_ACCOUNT_SID=your_account_sid
  TWILIO_AUTH_TOKEN=your_auth_token
  ```

## 📂 Project Structure

  ```
  krishi-vani/
  ├── .env                  # Environment variables for API keys
  ├── main.py               # The FastAPI application with API endpoints
  ├── data/                 # Directory for raw and processed public datasets
  │   ├── raw/              # Original downloaded files (e.g., PDFs, CSVs)
  │   ├── processed/        # Cleaned and formatted data
  ├── scripts/              # Scripts for data ingestion and processing
  │   ├── data_ingestion.py # Actual script for data processing
  ├── README.md             # This file
  ├── requirements.txt      # Project dependencies
  ```

## 📄 Scripts

This project includes a suite of scripts for data management and model serving. While the current prototype uses hardcoded logic, these scripts lay the foundation for a fully functional solution.

- **Data Ingestion & RAG Indexing**

  This script is responsible for the crucial first step of the RAG pipeline.

  - **Data Sources:** The script is designed to process datasets from the following public portals:

     - **IMD:** For weather and climate advisories.

     - **AGMARKNET:** For real-time market prices.

     - **ICAR & OGD:** For crop management and pest advisories.

     - **NABARD & PMFBY:** For financial schemes and policy information.

  - **How it Works:** It ingests raw data, cleans it, and uses a Hugging Face sentence transformer model to create embeddings. These embeddings, along with the original text, are then stored in     a ChromaDB vector store.

  - **Usage:**

    ```python scripts/data_ingestion.py```

  - **Running the Agent API**

    This command starts the FastAPI server, which hosts your AI agent. The server listens for incoming calls from Twilio and processes them using the agentic logic.

    ```uvicorn main:app --reload```

 ## Simulating Real-World Usage

 - **Run your local server:**

      ```uvicorn main:app --reload```

 - **Start ```ngrok``` in a new terminal:**

      ```ngrok http 8000```

 - **Configure Twilio:** In your Twilio console, set your phone number's webhook URL to your ngrok URL with the /voice endpoint (e.g., https://abcdef123.ngrok.io/voice). Set the method to POST.

 - **Make a test call:** Call your Twilio number and ask a question from one of the hardcoded test cases to see the intelligent response.
