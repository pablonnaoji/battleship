from flask_wtf import Form
from wtforms.fields import StringField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    """Accepts a nickname and a room."""
    name = StringField('Soldier Name', render_kw={"placeholder": "Player1 or Player2 only"},validators=[Required()])
    room = StringField('Battlefield', validators=[Required()])
    submit = SubmitField('Enter Battlefield!')
