# Building a simple PDF-QA-RAG-LLM app on Bedrock
* This repo so far contains 2 applications.


## `app.py`
* This file runs the PDF-RAG-LLM question answer application.
* This was built using streamlit as the user interface and AWS Bedrock for Amazon Titan Text Embeddings v2 and Claude-3-Haiku LLM or Meta-Llama-3.
* The concept is that PDF files are stored on the backend and vectorized as embeddings in a FAISS-CPU vector store.
* The user can then ask queries of the PDF documents using the LLM of their choice.
* To run this you need to:
  * 1) setup a virtual env: `python -m venv venv`
    2) activate the venv `source venv/bin/activate`
    3) Install requirements.txt file: `pip install -r requirements.txt`
    4) Setup AWS CLI config: make sure you aws CLI is downloaded and run: `aws configure`.

## `claude
