# AI Medical Assistant 🩺🤖

https://medicalgptanish.streamlit.app/

A Retrieval-Augmented Generation (RAG)-based AI medical assistant that allows users to upload medical PDFs and ask context-aware questions using Large Language Models, semantic search, and vector databases.

Built using FastAPI, Streamlit, LangChain, Pinecone, and Groq LLaMA3-70B.

---

## 🚀 Features

- 📄 Upload medical PDFs
- 🔍 Semantic document retrieval
- 🧠 Context-aware AI responses using RAG
- ⚡ Fast inference with Groq LLaMA3-70B
- 🗂️ Pinecone vector database integration
- 🌐 FastAPI backend
- 💬 Streamlit chatbot frontend
- 📥 Download chat history

---

## 🏗️ Architecture

```text
                ┌─────────────────────┐
                │   User Uploads PDF  │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ PDF Text Extraction │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │  Text Chunking      │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Embedding Generation│
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Pinecone Vector DB  │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Relevant Retrieval  │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Groq LLaMA3-70B LLM │
                └─────────┬───────────┘
                          │
                          ▼
                ┌─────────────────────┐
                │ Final AI Response   │
                └─────────────────────┘
```

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|------------|
| Frontend | Streamlit |
| Backend | FastAPI |
| Framework | LangChain |
| LLM | Groq LLaMA3-70B |
| Vector DB | Pinecone |
| Embeddings | Google Generative AI |
| PDF Parsing | PyPDF |
| Deployment | Render |

---

## 📂 Project Structure

```bash
medicalAssistant/
│
├── assets/
│   ├── DIABETES.pdf
│   ├── MedicalAssistant.pdf
│   └── medicalAssistant.png
│
├── client/
│   ├── components/
│   │   ├── chatUI.py
│   │   ├── history_download.py
│   │   └── upload.py
│   │
│   ├── utils/
│   │   └── api.py
│   │
│   ├── app.py
│   ├── config.py
│   └── requirements.txt
│
├── server/
│   ├── middlewares/
│   │   └── exception_handlers.py
│   │
│   ├── modules/
│   │   ├── llm.py
│   │   ├── load_vectorstore.py
│   │   └── query_handlers.py
│   │
│   └── routes/
│
├── main.py
├── pyproject.toml
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/snsupratim/medicalAssistant.git
cd medicalAssistant
```

---

### 2. Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r client/requirements.txt
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name
```

---

## ▶️ Running the Application

### Start Backend

```bash
uvicorn main:app --reload
```

Backend runs on:

```text
http://127.0.0.1:8000
```

---

### Start Frontend

```bash
streamlit run client/app.py
```

Frontend runs on:

```text
http://localhost:8501
```

---

## 📡 API Endpoints

### Upload PDFs

```http
POST /upload_pdfs/
```

Upload one or multiple PDF files.

---

### Ask Questions

```http
POST /ask/
```

Form Data:

```text
question=What are the symptoms of diabetes?
```

---

## 💡 Example Workflow

1. Upload medical PDFs
2. Documents are chunked and embedded
3. Embeddings are stored in Pinecone
4. User asks a question
5. Relevant chunks are retrieved
6. LLaMA3 generates a grounded response

---

## 🧠 What is RAG?

Retrieval-Augmented Generation (RAG) improves LLM responses by retrieving relevant external information before generating an answer. This helps reduce hallucinations and improves factual accuracy in domain-specific applications like healthcare.

---

## 🔮 Future Improvements

- 🏥 Multi-document memory
- 🧾 OCR support for scanned reports
- 🌍 Multilingual support
- 🔐 Authentication system
- ☁️ Docker & Kubernetes deployment
- 📊 Medical analytics dashboard

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment.

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---


## 👨‍💻 Author

**Anish Lotake**  
Computer Science Student at The University of Texas at Austin
