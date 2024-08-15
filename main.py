from llm import get_api_key, get_chat_model
from loader import load_and_split_documents
from vectorstore import create_vector_store
from retriever import create_retriever
from retriever import merge_docs

from langchain import hub
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def main():
    api_key = get_api_key()
    chat = get_chat_model()
    splits = load_and_split_documents("/Users/alookso/study/RAG_0806/solar_module_test2_public/sportclimbing.pdf")
    chroma_db = create_vector_store(splits)
    retriever = create_retriever(chroma_db)
 
    prompt = hub.pull("rlm/rag-prompt")
    
    rag_chain = (
        {"context": retriever | merge_docs, "question": RunnablePassthrough()}
        | prompt
        | chat
        | StrOutputParser()
    )
    
    query = input("클라이밍에 대해 궁금한 것을 물어보세요: ")
    result = rag_chain.invoke(query)
    print(result)

if __name__ == "__main__":
    main()

