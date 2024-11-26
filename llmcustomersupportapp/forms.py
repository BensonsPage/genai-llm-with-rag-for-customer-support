"""Sign-up & log-in forms."""
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import (
    Length,
    DataRequired
)

class Request(FlaskForm):
    """Customer Query Form."""
    customer_query = StringField(
        'Query',
        validators=[
            Length(min=5),
            DataRequired()
        ]
    )
    submit = SubmitField('Ask me')