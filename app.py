import tempfile
import streamlit as st
from langchain_community.document_loaders import CSVLoader
from utils import get_model_response

def main():
    st.set_page_config(page_title="Data Analyst AI", page_icon="📊")
    st.title("📊 Data Analyst AI")

    # body
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False) as f:
            f.write(uploaded_file.getvalue())
            tmp_file_path = f.name

        csv_loader = CSVLoader(tmp_file_path, encoding="utf-8", csv_args={'delimiter': ','})
        data = csv_loader.load()
        user_input = st.text_input("Your Questions:")
        answer_button = st.button("Get Answer")

        if answer_button:
            response = get_model_response(data, user_input)
            st.write(response)

if __name__ == "__main__":
    main()