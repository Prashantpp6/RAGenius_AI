import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
import tempfile
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Multi RAG App")

st.title("📄 Multi-Document AI Assistant")

option = st.sidebar.selectbox(
    "Choose Feature",
    ["Resume Chatbot", "PDF Q&A", "Notes Assistant", "FAQ Bot", "Search"]
)

# File upload only for these options
uploaded_file = None
if option in ["Resume Chatbot", "PDF Q&A", "Notes Assistant"]:
    uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

elif option == "FAQ Bot":
    st.write("Using preloaded FAQ data")

elif option == "Search":
    st.write("Search across documents")

# MAIN LOGIC
if uploaded_file:

    st.success("File uploaded successfully ✅")

    # Save file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(uploaded_file.read())
        file_path = tmp_file.name

    # Load PDF
    loader = PyPDFLoader(file_path)
    docs = loader.load()

    st.write(f"Loaded {len(docs)} pages ✅")

    # Split
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    st.write(f"Created {len(chunks)} chunks ✅")

    # Embeddings
    embeddings = HuggingFaceEmbeddings()

    # Vector DB
    vector_db = FAISS.from_documents(chunks, embeddings)

    st.success("Vector database ready ✅")

    # Query input
    query = st.text_input("Ask a Question")

    if query:
        # LLM
        llm = ChatGroq(model="llama-3.1-8b-instant")

        # Retrieve relevant docs
        results = vector_db.similarity_search(query)

        # Create context
        context = "\n\n".join([doc.page_content for doc in results])

        # Prompt
        prompt = f"""
        Answer the question based on the context below.

        Context:
        {context}

        Question:
        {query}
        """

        # Get response
        response = llm.invoke(prompt)

        st.write("🤖 Answer:")
        st.write(response.content)