from collections import namedtuple
import datetime as dt
from pytz import timezone


def normalize(transform):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            result = func(*args, **kwargs)
            return transformer(transform, result)
        return wrapper_normalize
    return decorator_normalize


def normalize_list(transform):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            result = func(*args, **kwargs)
            normal_list = [transformer(transform, element) for element in result]
            return normal_list
        return wrapper_normalize
    return decorator_normalize


def transformer(transform, element):
    result = {}
    for key, value in element.items():
        if key in transform:
            result[transform[key]] = value
        else:
            result[key] = value
    return result


Span = namedtuple('Span', 'start end')


def week_span(day=dt.date.today()):
    offset = (day.weekday() - 6) % 7
    prev_sunday = day - dt.timedelta(days=offset)
    next_saturday = prev_sunday + dt.timedelta(days=6)
    week = Span(start=prev_sunday, end=next_saturday)
    return week


def date_to_rfc3339(date, tz):
    new_date = dt.datetime.combine(date, dt.datetime.min.time())
    new_date = new_date.replace(tzinfo=timezone(tz))
    return new_date.isoformat()
