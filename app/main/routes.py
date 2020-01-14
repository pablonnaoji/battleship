from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm
from models import Player


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    form = LoginForm()
    winners = Player.query.all()
    print("winners",winners)
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['room'] = form.room.data
        return redirect(url_for('.battle'))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')
    return render_template('index.html', form=form, winners=winners)


@main.route('/battle')
def battle():
    """Game room. The player's name and room are stored in
    the session."""

    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('.index'))
    return render_template('battle.html', name=name, room=room)
