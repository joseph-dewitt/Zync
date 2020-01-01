import datetime
import os.path
import pickle
from app.googlecal.googlecaltransforms import *
from app.helpers import denormalize, normalize, normalize_list
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.


SCOPES = ['https://www.googleapis.com/auth/calendar']


"""Shows basic usage of the Google Calendar API.
Prints the start and name of the next 10 events on the user's calendar.
"""
creds = None
# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pickle_path = os.path.join(BASE_DIR, 'token.pickle')
credentials_path = os.path.join(BASE_DIR, 'credentials.json')

if os.path.exists(pickle_path):
    with open(pickle_path, 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_path, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open(pickle_path, 'wb') as token:
        pickle.dump(creds, token)

service = build('calendar', 'v3', credentials=creds)

# Call the Calendar API
now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
events_result = service.events().list(calendarId='primary', timeMin=now,
                                      maxResults=10, singleEvents=True,
                                      orderBy='startTime').execute()
events = events_result.get('items', [])

if not events:
    print('No upcoming events found.')
# for event in events:
#     start = event['start'].get('dateTime', event['start'].get('date'))
#     print(start, event['summary'])


def create_calendar(title, description):
    body = {
        'kind': 'calendar#calendar',
        'summary': title,
        'description': description
    }
    return service.calendars().insert(body=body).execute()


@normalize_list(map_calendar_to_group)
def get_calendars():
    return service.calendarList().list().execute().get('items')


@normalize(map_calendar_to_group)
def get_calendar(calendarId='primary'):
    return service.calendars().get(calendarId=calendarId).execute()


def update_calendar(calendarId, body):
    return service.calendar().patch(calendarId, body).execute()


@denormalize(map_element_to_event)
def create_event(event):
    return service.events().insert(calendarId='primary', body=event)


@normalize_list(map_event_to_element)
def get_events(calendarId='primary', start=None, end=None):
    # TODO: SORT THE RESULTS, GCAL DOESN'T SORT WHEN YOU EXCLUDE REPEATS
    # TODO: ALL POSSIBLE FILTERS NEED TO BE ARGUMENTS
    return service.events().list(calendarId=calendarId,
                                 singleEvents=True,
                                 orderBy='startTime',
                                 timeMin=start,
                                 timeMax=end).execute().get('items')


def get_event(calendarId, eventId):
    return service.events().get(calendarId=calendarId, eventId=eventId).execute()


def update_event(calendarId, eventId, body):
    return service.events().patch(calendarId=calendarId, eventId=eventId, body=body)
