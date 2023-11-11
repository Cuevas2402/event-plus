from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import DirectoryLoader
from langchain.llms import HuggingFaceHub
from langchain.embeddings import HuggingFaceInstructEmbeddings



def save_vectore_store(text_chunks):
    persist_directory = './vdb'


    instructor_embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base")

    vectordb = Chroma.from_documents(documents=text_chunks, embedding=instructor_embeddings, persist_directory=persist_directory)
    vectordb.persist()
    vectordb = None



def get_pdf_text():

    loader = DirectoryLoader('./pdf/', glob="./*.pdf", loader_cls=PyPDFLoader)

    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=512, chunk_overlap=200)
    texts = text_splitter.split_documents(documents)

    return texts

def main():
   texts = get_pdf_text()

   save_vectore_store(texts) 
    

if __name__ == "__main__":
    main()