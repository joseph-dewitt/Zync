map_calendar_to_group = {
    'name': 'summary',
    'id': 'id',
    'timezone': 'timeZone'
}

map_group_to_calendar = {
    'summary': 'name',
    'timeZone': 'timezone'
}

map_event_to_element = {
    'start': ['start', 'dateTime'],
    'end': ['end', 'dateTime'],
    'calendarId': ['organizer', 'email'],
    'name': 'summary',
    'id': 'id',
    'description': 'description',
    'url': 'htmlLink',
    'location': 'location'
}

map_element_to_event = {
    'summary': 'name',
    'id': 'id'
}
