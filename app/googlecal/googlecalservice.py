from app.helpers import normalize_list, week_span, date_to_rfc3339
import datetime as dt
from .googlecal import get_calendar, get_calendars, get_events
from .googlecaltransforms import *
from app.abstractservice import AbstractService, Group, Unit, Element


class GoogleCalService(AbstractService):

    @normalize_list(map_calendar_to_group)
    def get_groups(self):
        # TODO this needs to return a list of Calendars
        return get_calendars()

    def get_units(self, group):
        # This method needs to create a list of units from one calendar
        # These spans must also reference a specific calendar
        units = []
        day = dt.date.today()
        for _ in 4:
            units.append(self.get_unit(group, day))
            day = day + dt.timedelta(days=7)
        return units

    def get_unit(self, calendar, start):
        span = week_span(start)
        name = f'{span.start.strftime("%B %d, %Y")} - {span.end.strftime("%B %d, %Y")}'
        # TODO put this as a property in a abstract calendar class
        week = Week({'start': span.start,
                     'end': span.end,
                     'name': name,
                     'calendarId': calendar.id,
                     'timezone': calendar.timezone})
        return week

    @normalize_list(map_event_to_element)
    def get_elements(self, unit):
        # In this case, unit is a week span from a specific calendar
        # TODO this needs to return a list of Events
        events = [Event(body) for
                  body in
                  get_events(calendarId=unit.calendarId,
                             start=date_to_rfc3339(unit.start, unit.timezone),
                             end=date_to_rfc3339(unit.end, unit.timezone))
                  ]
        return events


class Calendar(Group):

    @property
    def units(self):
        return GoogleCalService.get_units(self)


class Week(Unit):

    @property
    def group(self):
        return get_calendar(self['calendarId'])

    @property
    def elements(self):
        return GoogleCalService.get_elements(self)


class Event(Element):

    @property
    def group(self):
        return get_calendar(self['calendarId'])

    @property
    def unit(self):
        return GoogleCalService.get_unit(self['calendarId'], self['start'])
