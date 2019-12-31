from app.helpers import week_span, date_to_rfc3339
import datetime as dt
from .googlecal import get_calendar, get_calendars, get_events
from app.abstractservice import AbstractService, Group, Unit, Element


class GoogleCalService(AbstractService):

    @staticmethod
    def get_groups():
        return [Calendar(body) for body in get_calendars()]


# TODO create a calendar helper module
def get_units(calendar):
    # This method needs to create a list of units from one calendar
    # These spans must also reference a specific calendar
    units = []
    day = dt.date.today()
    for _ in range(4):
        units.append(get_unit(calendar, day))
        day = day + dt.timedelta(days=7)
    return units


# TODO put this function somewhere else, and move the
# TODO week instantiation in the units property in Calendar
def get_unit(calendar, start):
    span = week_span(start)
    name = f'{span.start.strftime("%B %d, %Y")} - {span.end.strftime("%B %d, %Y")}'
    # TODO put this as a property in a abstract calendar class
    week = {'id': str(span.start)+calendar['id'],
            'start': span.start,
            'end': span.end,
            'name': name,
            'calendarId': calendar['id'],
            'timezone': calendar['timezone']}
    return week


class Calendar(Group):

    @property
    def units(self):
        return [Week(body) for body in get_units(self)]


class Week(Unit):

    @property
    def group(self):
        return Calendar(get_calendar(self['calendarId']))

    @property
    def elements(self):
        events = [Event(body) for body in
                  get_events(calendarId=self['calendarId'],
                             start=date_to_rfc3339(self['start'], self['timezone']),
                             end=date_to_rfc3339(self['end'], self['timezone']))]
        return events


class Event(Element):

    @property
    def group(self):
        return get_calendar(self['calendarId'])

    @property
    def unit(self):
        return GoogleCalService.get_unit(self['calendarId'], self['start'])
