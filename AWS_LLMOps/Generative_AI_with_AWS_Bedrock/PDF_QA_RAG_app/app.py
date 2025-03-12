import json 
import os 
import sys 
import boto3 # sdk
import certifi # SSL certificate
import streamlit as st

## AWS SDK credentials
session = boto3.Session()
credentials = session.get_credentials()

## Amazon Titan Embedding Model via LangChain API
#from langchain.embeddings import BedrockEmbeddings
from langchain_aws import BedrockEmbeddings
#from langchain.llms.bedrock import Bedrock
from langchain_community.chat_models import BedrockChat

## Data ingestion libraries
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader

## Vector Embeddings and Vector Store 
from langchain_community.vectorstores import FAISS

### LLM models via AWS Bedrock
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

## AWS Bedrock Clients
## 1. Setup Bedrock Client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='<your region here>', ## add your region here
    verify=certifi.where() ## to avoid SSL error
)
## 2. Setup bedrock embeddings
bedrock_embeddings = BedrockEmbeddings(model_id="<model id here>",
                                       client=bedrock)


#### Data Ingestion
def data_ingestion():
    """Data Ingestion Pipeline Function"""
    ## Load the documents from data folder
    loader=PyPDFDirectoryLoader("data")
    documents=loader.load()

    ## text splitter
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=10000,
                                                 chunk_overlap=1000)
    ## split the documents
    docs=text_splitter.split_documents(documents)
    return docs

#### Vector Embeddings and Vector Store -- Titan Embeddings & FAISS
def get_vector_store(docs):
    """Vector Store Function"""
    ## Create Vector Store
    vectorstore_faiss=FAISS.from_documents(
        docs,
        bedrock_embeddings,
        #num_dimensions=512, ## model specific
    )
    ## Save vector store in local file index
    vectorstore_faiss.save_local("faiss_index")
    return vectorstore_faiss

#### LLM Models via AWS Bedrock
def get_haiku_llm():
    """Function to create Anthropic Claude LLM from Bedrock"""
    llm=BedrockChat(model_id="<model id here>",
                client=bedrock,
                model_kwargs={"max_tokens": 1000})
    return llm

## if you want to use llama-3 instead
# def get_llama_llm():
#     """Function to create Meta Llama 3 LLM from Bedrock"""
#     llm=Bedrock(model_id="<model id here>",
#                 client=bedrock,
#                 model_kwargs={"max_new_tokens": 512,
#                               "top_p":0.9,
#                               "temperature":0.6})
#     return llm

#### Prompt Template
prompt_template= """

Human: Use the following pieces of context to provide a concise answer to the question
at the end but use at least 3 of the pieces of context in your answer.
Please summarize with 250 words with detailed explanations.
If you don't know the answer, just say "I don't know", do not try to make up an answer." \
<context>
{context}
</context>

Question: {question}
Assistant: """

PROMPT=PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"],
)

#### Response 
def get_response(llm, vectorstore_faiss, query):
    """Function to get response from LLM"""
    ## Create a retrieval QA chain
    qa=RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        ## Search within the vector store
        retriever=vectorstore_faiss.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5},
        ),
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
        
    )   ## return answer
    answer=qa({"query": query})
    return answer['result']


#### Build Streamlit App
def main():
    st.set_page_config("Chat PDF QA RAG App")
    st.header("Chat PDF file using AWS Bedrock")

    ## user query
    user_question=st.text_input("Ask a question about the PDF files")

    ## data ingestion button
    with st.sidebar:
        st.title("Update or Create Vector Store:")

        if st.button("Vectors Update"):
            with st.spinner("Processing...."):
                docs=data_ingestion()
                vectorstore = get_vector_store(docs)
                st.success("Done")

    ## LLM output button -- Claude Haiku
    if st.button("Claude Haiku Output"):
        with st.spinner("Processing..."):
            ## access the faiss index with the embeddings
            try:
                # First, try loading with the allow_dangerous_deserialization parameter
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            except TypeError:
                # If that fails, load without the parameter
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings)
        
            llm = get_haiku_llm()

            st.write(get_response(llm, faiss_index, user_question))
            st.success("Done")

    ## LLM output button -- Meta Llama 3
    if st.button("Llama 3 Output"):
        with st.spinner("Processing..."):
            ## access the faiss index with the embeddings
            try:
                # First, try loading with the allow_dangerous_deserialization parameter
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings, allow_dangerous_deserialization=True)
            except TypeError:
                # If that fails, load without the parameter
                faiss_index = FAISS.load_local("faiss_index", bedrock_embeddings)
        
            llm = get_haiku_llm()

            st.write(get_response(llm, faiss_index, user_question))
            st.success("Done")


if __name__ == "__main__":
    main()
