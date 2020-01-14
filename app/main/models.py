from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Player(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True)

	def __repr__(self):
		return '<Player {}>'.format(self.username)
