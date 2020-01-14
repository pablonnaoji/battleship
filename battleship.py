#!/bin/env python
from app import create_app, socketio
from sqlalchemy.orm import mapper
from sqlalchemy.orm import scoped_session, sessionmaker
from app.main.models import db

app = create_app(debug=True)

with app.app_context():
	session = scoped_session(sessionmaker(bind=db.engine))
	db.create_all()

if __name__ == '__main__':
    socketio.run(app)
