from app import app , mysql, socketio
from flask import render_template, request, session, url_for, redirect
from flask_socketio import send
from langchain.llms import CTransformers
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import HuggingFaceHub
from langchain.vectorstores import Chroma

def get_retrievalqa():
    persist_directory = './vdb'

    instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")

    vectordb = Chroma(persist_directory=persist_directory, embedding_function=instructor_embeddings)

    retriever = vectordb.as_retriever(search_kwargs={"k": 1})

    llm = HuggingFaceHub(repo_id="JorgeSarry/est5-summarize", model_kwargs={"temperature":0.5, "max_length":512})

    qa_chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

    return qa_chain


@socketio.on('message')
def handle_message(message):

    if message != "User connected!": 
        qa_chain = get_retrievalqa()

        response = qa_chain(message)

        send("Bot: "+response['result'], broadcast=True)

@app.route('/chat')
def show_chat():
    return render_template('pages/chat.html')
