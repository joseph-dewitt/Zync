from flask import render_template
from app import app
from app import googlecal
from app import wunder


@app.route('/')
@app.route('/index')
def index():
    events = googlecal.get_events()
    todos = wunder.get_lists()
    return render_template('index.html', title='Home', events=events, todos=todos)
