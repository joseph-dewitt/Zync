from collections import namedtuple
import datetime as dt
from pytz import timezone
import pprint as pp


def normalize(transform):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            element = func(*args, **kwargs)
            return transformer(transform, element)
        return wrapper_normalize
    return decorator_normalize


def normalize_list(transform):
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            results = func(*args, **kwargs)
            return [transformer(transform, element) for element in results]
        return wrapper_normalize
    return decorator_normalize


def denormalize(transform):
    def decorator_normalize(func):
        def wrapper_normalize(element):
            result = transformer(transform, element)
            return func(result)
        return wrapper_normalize
    return decorator_normalize


def denormalize_list(transform):
    def decorator_normalize(func):
        def wrapper_normalize(elements):
            result = [transformer(transform, element) for element in elements]
            return func(result)
        return wrapper_normalize
    return decorator_normalize

# TODO this function must be modified to resemble the transformer in the scratch file
def transformer(transform, element):
    result = {}
    for key, value in transform.items():
        if isinstance(value, list):
            field = element
            for key in value:
                field = field[key]
            result[key] = field
        else:
            result[key] = field[value]
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
