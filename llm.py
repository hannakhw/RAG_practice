from langchain_openai import ChatOpenAI
import getpass
import os

def get_api_key():
    if "OPENAI_API_KEY" not in os.environ:
        api_key = getpass.getpass("OpenAI API 키를 입력하세요: ")
        
    else:
        api_key = os.environ["OPENAI_API_KEY"]
    return api_key

def get_chat_model():
    api_key = get_api_key()
    chat = ChatOpenAI(model="gpt-3.5-turbo", openai_api_key = api_key)
    return chat

