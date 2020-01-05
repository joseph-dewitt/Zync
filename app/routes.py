from app import app
from app.googlecal import GoogleCalService
from app.trello import TrelloService
from flask import render_template
import pprint as pp
from flask_wtf import Form
from wtforms import SubmitField
from wtforms.fields.html5 import DateField


class ExampleForm(Form):
    dt = DateField('DatePicker', format='%Y-%m-%d')
    submit = SubmitField()

# To avoid naming conflicts here, both Service classes
# need to be imported. That way, both can call their
# get_groups method. These services will extend the
# AbstractService class, which for now will only enforce
# the get_groups method. This method will be static. Each package's
# init will only import this service class.


@app.route('/')
@app.route('/index')
def index():
    form = ExampleForm()
    if form.validate_on_submit():
        return form.dt.data.strftime('%Y-%m-%d')
    calendars = GoogleCalService.get_groups()
    boards = TrelloService.get_groups()
    return render_template('index.html',
                           title='Home',
                           calendars=calendars,
                           boards=boards,
                           form=form)
