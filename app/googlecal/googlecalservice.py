from .googlecal import *
from .googlecaltransforms import *
from app.helpers import normalize_list, week_span, date_to_rfc3339


@normalize_list(map_event_to_element)
def get_week_events():
    last_sunday, next_sunday = week_span()
    last_sunday = date_to_rfc3339(last_sunday, 'America/New_York')
    next_sunday = date_to_rfc3339(next_sunday, 'America/New_York')
    return get_events(calendarId='primary',
                      start=last_sunday,
                      end=next_sunday)
