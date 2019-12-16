from flask import render_template
from app import app
from app import googlecal
from app import trello


@app.route('/')
@app.route('/index')
def index():
    events = googlecal.get_events()
    boards = trello.get_boards().json()
    return render_template('index.html',
                           title='Home',
                           events=events,
                           boards=boards,
                           get_lists=trello.get_lists,
                           get_cards=trello.get_cards)
