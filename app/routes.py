from app import app
from app.googlecal import GoogleCalService
from app.trello import TrelloService
from flask import render_template
import pprint as pp


# To avoid naming conflicts here, both Service classes
# need to be imported. That way, both can call their
# get_groups method. These services will extend the
# AbstractService class, which for now will only enforce
# the get_groups method. This method will be static. Each package's
# init will only import this service class.

@app.route('/')
@app.route('/index')
def index():
    calendars = GoogleCalService.get_groups()
    pp.pprint(calendars[0].units)
    boards = TrelloService.get_groups()
    pp.pprint(boards[0].units)
    return render_template('index.html',
                           title='Home',
                           calendars=calendars,
                           boards=boards)
