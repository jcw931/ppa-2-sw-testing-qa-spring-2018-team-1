from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class gen_dist_form(FlaskForm):
    x1 = IntegerField('x1:', validators=[DataRequired()])
    x2 = IntegerField('x2:', validators=[DataRequired()])
    y1 = IntegerField('y1:', validators=[DataRequired()])
    y2 = IntegerField('y2:', validators=[DataRequired()])