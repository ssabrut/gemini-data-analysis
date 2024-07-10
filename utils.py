import os

import google.generativeai as genai

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

PROMPT_TEMPLATE = """
You have to answer the question from the provided context and make sure that you provide all the details.
Context: {context}
Question: {question}

Answer:
"""

model = ChatGoogleGenerativeAI(model='gemini-pro', temperature=.9)

def get_model_response(file, query):
    # split context into chunk
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=200)
    context = '\n\n'.join(str(p.page_content) for p in file)
    data = text_splitter.split_text(context)

    # generate embedding
    embeddings = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    searcher = Chroma.from_texts(data, embeddings).as_retriever()
    records = searcher.get_relevant_documents(query)
    prompt = PromptTemplate(PROMPT_TEMPLATE, input_variables=['context', 'question'])
    chain = load_qa_chain(model, chain_type='stuff', prompt=prompt)
    response = chain(
        {
            'input_documents': records,
            'question': query
        },
        return_only_outputs=True
    )

    return response['output_text']