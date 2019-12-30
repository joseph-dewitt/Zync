import datetime
import os.path
import pickle

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


def get_calendars():
    return service.calendarList().list().execute().get('items')


def get_calendar(calendarId='primary'):
    return service.calendars().get(calendarId=calendarId).execute()


def update_calendar(calendarId, body):
    return service.calendar().patch(calendarId, body).execute()


def create_event(calendar, title, description, start, end):
    body = {
        'summary': title,
        'description': description,
        'start': start,
        'end': end
    }
    return service.events().insert(calendar, body).execute()


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


# import pytz
# from datetime import timedelta
# from datetime import datetime
# from datetime import date
# today = date.today()
# offset = (today.weekday() - 6) % 7
# last_sunday = today - timedelta(days=offset)
# end = last_sunday + timedelta(days=7)
# last_sunday = datetime.combine(last_sunday, datetime.min.time())
# end = datetime.combine(end, datetime.min.time())
# last_sunday = last_sunday.replace(tzinfo=pytz.UTC)
# end = end.replace(tzinfo=pytz.UTC)
# things = service.events().list(calendarId='primary',
#                       singleEvents=True,
#                       timeMin=last_sunday.isoformat(),
#                       timeMax=end.isoformat()).execute()
# print(last_sunday.isoformat())
# print(end.isoformat())
# import pprint as pp
# pp.pprint(things)
