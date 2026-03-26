# 🚀 RAGenius AI – Multi-Document Assistant

> An intelligent **RAG-based AI assistant** that allows users to interact with documents like resumes, PDFs, notes, and FAQs in a conversational way.

---

## 🧠 What is RAGenius AI?

RAGenius AI leverages **Retrieval-Augmented Generation (RAG)** to combine semantic document search with powerful LLM responses.

Instead of just reading documents, you can:

* Ask questions
* Extract insights
* Perform semantic search
  —all through a chatbot interface.

---

## ✨ Key Features

🔹 **📄 Resume Chatbot**
Upload your resume and ask questions about your skills, experience, and projects.

🔹 **📚 PDF Q&A**
Chat with any PDF (books, reports, notes).

🔹 **📝 Notes Assistant**
Convert study materials into an AI-powered assistant.

🔹 **❓ FAQ Bot**
Preload FAQs and get instant answers.

🔹 **🔍 Semantic Search**
Search documents based on meaning, not just keywords.

---

## 🏗️ Architecture (Workflow)

```
User Query
   ↓
Document Upload
   ↓
Text Splitting
   ↓
Embeddings (HuggingFace)
   ↓
Vector Store (FAISS)
   ↓
Retriever
   ↓
LLM (Groq)
   ↓
Final Answer
```

---

## 🧰 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM:** Groq
* **Framework:** LangChain
* **Vector Database:** FAISS
* **Embeddings:** HuggingFace

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Prashantpp6/RAGenius_AI.git
cd RAGenius_AI
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
streamlit run app_ui.py
```

---

## 📸 Demo

> Add screenshots or a demo video link here to showcase your project.

---

## 📌 Use Cases

* 🎯 Students → Study smarter with notes
* 💼 Job Seekers → Analyze resumes
* 📊 Analysts → Extract insights from documents
* 🏢 Businesses → Internal knowledge chatbot

---

## 🚀 Future Improvements

* Multi-document upload
* Chat history memory
* Deployment (Streamlit Cloud / AWS)
* User authentication

---

## 👨‍💻 Author

**Prashant Singh Parmar**
🔗 LinkedIn: https://www.linkedin.com/in/prashant-singh-parmar/
💻 GitHub: https://github.com/Prashantpp6

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
