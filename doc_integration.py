import os
from langchain_community.llms import openai
from langchain_community.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain_community.chat_models import ChatOpenAI
import pickle
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import constants 

os.environ["OPENAI_API_KEY"] = constants.APIKEY
openai.api_key = os.getenv("OPENAI_API_KEY")

scopes = ['https://www.googleapis.com/auth/documents']

def get_docs_service():
    if os.path.exists('token.pkl'):
        credentials = pickle.load(open ("token.pkl", "rb" ))
    else :
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes = scopes)
        credentials =  flow.run_local_server()
        pickle.dump(credentials, open ("token.pkl", "wb" ))
        credentials = pickle.load(open ("token.pkl", "rb" ))
    
    service = build('docs', 'v1', credentials=credentials)
    return service

def fetch_schedule():
    service = get_docs_service()
    document = service.documents().get(documentId=constants.DOC_ID).execute()
    content = document.get('body').get('content')
    schedule = ""
    for element in content:
        if 'paragraph' in element:
            text_run = element['paragraph']['elements'][0]['textRun']
            schedule += text_run['content']
    # print(schedule)
    f = open("schedule.txt", "w")
    f.write(schedule)
    f.close()
    
    return schedule

def print_schedule(prompt):
    fetch_schedule()
    loader = TextLoader('schedule.txt')
    index = VectorstoreIndexCreator().from_loaders([loader])
    response = index.query(prompt, llm = ChatOpenAI())

    return response

# chat = print_schedule("Get me schedule for 15 May")
# print(chat)
