map_calendar_to_group = {
    'name': 'summary',
    'timezone': 'timeZone'
}

map_group_to_calendar = {
    'summary': 'name',
    'timeZone': 'timezone'
}

map_event_to_element = {
    'start': ['start', 'dateTime'],
    'end': ['end', 'dateTime'],
    'timezone': ['start', 'timeZone'],
    'calendarId': ['organizer', 'email'],
    'name': 'summary',
    'description': 'description',
    'url': 'htmlLink',
    'location': 'location'
}

map_element_to_event = {
    'summary': 'name'
}
