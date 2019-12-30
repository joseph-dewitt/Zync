from flask import render_template
from app import app
from app.googlecal import GoogleCalService
from app import trello
import pprint as pp


@app.route('/')
@app.route('/index')
def index():
    calendars = GoogleCalService.get_groups()
    boards = trello.get_boards_from_user()
    return render_template('index.html',
                           title='Home',
                           calendars=calendars,
                           boards=boards,
                           get_lists=trello.get_lists,
                           get_cards=trello.get_cards)
