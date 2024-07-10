import tempfile
import streamlit as st
from langchain_community.document_loaders import CSVLoader

def main():
    st.set_page_config(page_title="Data Analyst AI", page_icon="📊")
    st.title("📊 Data Analyst AI")

    # body
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

if __name__ == "__main__":
    main()