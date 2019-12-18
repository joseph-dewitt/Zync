import datetime
from datetime import timedelta
from .googlecal import *


def last_sunday():
    today = datetime.date.today()
    offset = (today.weekday() - 6) % 7
    last_sunday = today - timedelta(days=offset)
    return last_sunday


def get_week_events():

