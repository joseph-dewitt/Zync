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


def week_span():
    today = dt.date.today()
    offset = (today.weekday() - 6) % 7
    last_sunday = today - dt.timedelta(days=offset)
    next_sunday = last_sunday + dt.timedelta(days=7)
    return last_sunday, next_sunday


def date_to_rfc3339(date, tz):
    new_date = dt.datetime.combine(date, dt.datetime.min.time())
    new_date = new_date.replace(tzinfo=timezone(tz))
    return new_date.isoformat()
