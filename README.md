# 🤖 RAG-Powered Meeting Assistant

An intelligent **Retrieval-Augmented Generation (RAG)** based tool that helps you quickly query and summarize meeting transcripts.  
Upload your meeting transcript, ask questions in natural language, and get precise, context-aware answers instantly.

---

## 📌 Features
- **Smart Q&A** – Ask questions about any uploaded meeting transcript.
- **Context-Aware Retrieval** – Uses RAG to provide accurate answers from relevant transcript sections.
- **Interactive UI** – Built with Streamlit for an intuitive user experience.
- **Fast Processing** – Handles large transcripts efficiently.
- **Secure** – API keys stored in environment variables.

---

## 🛠 Tech Stack
- **Python** – Core logic
- **Streamlit** – Web interface
- **LangChain / RAG** – Retrieval-augmented generation pipeline
- **dotenv** – Secure API key loading

---

## 📂 Project Structure
```plaintext
rag-meeting-assistant/
│── app.py             # Streamlit app
│── rag_core.py        # RAG pipeline logic
│── requirements.txt   # Python dependencies
│── .env               # API keys (not committed to GitHub)
│── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<username>/rag-meeting-assistant.git
cd rag-meeting-assistant
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set API Key
Create a `.env` file in the root folder and add your API key:
```ini
OPENAI_API_KEY=your_api_key_here
```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

---

## 📈 How It Works
1. **Upload Transcript** – Upload a `.txt` file of your meeting.
2. **RAG Pipeline** – The transcript is processed, indexed, and stored for retrieval.
3. **Ask Questions** – Enter your question in the text box.
4. **Get Answers** – The system retrieves relevant chunks and generates a precise answer.
---

## 🚀 Real-World Impact
- Saves hours spent manually reviewing long meeting notes.
- Ensures no key decision points are missed.
- Improves productivity for teams, managers, and project stakeholders.

---

## 📜 License
This project is licensed under the **MIT License**.
