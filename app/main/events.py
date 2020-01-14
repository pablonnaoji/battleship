from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from flask_sqlalchemy import SQLAlchemy
from models import Player

db = SQLAlchemy()


@socketio.on('joined', namespace='/battle')
def joined(message):
    """Sent by clients when they enter a room."""
    room = session.get('room')
    join_room(room)
    emit('status', {'msg': session.get('name') + ' has entered the battlefield.'}, room=room)


@socketio.on('text', namespace='/battle')
def text(message):
    """Sent by a client when the user entered a new message."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ':' + message['msg']}, room=room)

@socketio.on('win', namespace='/battle')
def text(message):
    """Sent by a client when a user wins the battle."""
    name = session.get('name')
    print(name +" is our winner ")
    u = Player(username=name)
    db.session.add(u)
    db.session.commit()
    print("added winner to db")


@socketio.on('left', namespace='/battle')
def left(message):
    """Sent by clients when they leave a room"""
    room = session.get('room')
    leave_room(room)
    emit('status', {'msg': session.get('name') + ' has retreated from the battlefield. You Win!'}, room=room)

