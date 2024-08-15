from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from llm import get_api_key 

def create_vector_store(documents):
    embeddings = OpenAIEmbeddings(
        api_key= get_api_key(),
        model="text-embedding-3-small")
    
    vectorstore = Chroma.from_documents(
        documents=documents, embedding=embeddings)
    
    return vectorstore