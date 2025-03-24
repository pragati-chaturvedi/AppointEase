from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import os

scopes = ["https://www.googleapis.com/auth/calendar.events"]

def authenticate_google_calendar():
    if os.path.exists('tokencal.pkl'):
        credentials = pickle.load(open ("tokencal.pkl", "rb" ))

    else :
        flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes = scopes)
        credentials =  flow.run_local_server()
        pickle.dump(credentials, open ("tokencal.pkl", "wb" ))
        credentials = pickle.load(open ("tokencal.pkl", "rb" ))
        
    service = build("calendar", "v3", credentials = credentials)
    return service

def schedule_appointment( summary, description, start_time, end_time):
    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'America/Los_Angeles',
        },
    }
    service = authenticate_google_calendar()
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
    
    return ('Event created: %s' % (event.get('htmlLink')))



