from collections import namedtuple, defaultdict
import datetime as dt
from pytz import timezone
import pprint as pp

"""
TODO normalize/denormalize is based on read/write API calls.
"""

def normalize(transform):
    """The decorator to be applied to service API calls which return single objects.

    Normalize takes a transform for whichever service it is used in, and returns a
    decorator, decorator_normalize. This decorator takes the function, the service
    method, and applies the transformer method to the dict which the service method returns.

    The purpose of this decorator is to provide a simple means of taking the data
    returned by the service and changing the keys into the common keys. By doing this
    with every service, all data can be represented in the same way.

    Argument:
    transform -- the map used by transformer connecting the normal key-name to the
    service key-name, or path to service key-name in the case of nested JSON.
    """
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            element = func(*args, **kwargs)
            return transformer(transform, element)
        return wrapper_normalize
    return decorator_normalize


def normalize_list(transform):
    """The decorator to be applied to service API calls which return multiple objects.

    This decorator is identical to normalize, save for expecting a list of objects
    rather than just one. It applies to transform using transformer on each one.

    Argument:
    transform -- the map used by transformer connecting the normal key-name to the
    service key-name, or path to service key-name in the case of nested JSON.
    """
    def decorator_normalize(func):
        def wrapper_normalize(*args, **kwargs):
            results = func(*args, **kwargs)
            return [transformer(transform, element) for element in results]
        return wrapper_normalize
    return decorator_normalize


def denormalize(transform):
    def decorator_normalize(func):
        def wrapper_normalize(element):
            result = reverse_transformer(transform, element)
            return func(result)
        return wrapper_normalize
    return decorator_normalize


def denormalize_list(transform):
    def decorator_normalize(func):
        def wrapper_normalize(elements):
            result = [reverse_transformer(transform, element) for element in elements]
            return func(result)
        return wrapper_normalize
    return decorator_normalize


def transformer(transform, element):
    result = {}
    for key, value in transform.items():
        if isinstance(value, list):
            field = element
            for name in value:
                field = field.get(name)
            result[key] = field
        else:
            result[key] = element.get(value)
    return result


def ddict():
    return defaultdict(ddict)


def reverse_transformer(transform, element):
    result = ddict()
    for key, value in transform.items():
        if isinstance(value, list):
            field = result
            for name in value[:-1]:
                field = field[name]
            field[value[-1]] = element[key]
        else:
            result[value] = element[key]
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
