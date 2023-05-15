from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, IntegerField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired
from models import Trainer

def choices():
    trainer = Trainer.query.first()
    clients = trainer.clients
    return clients

class MealForm(FlaskForm):
    client = QuerySelectField('Client', query_factory=choices, get_label='name')
    day = SelectField('Day', choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], validators=[DataRequired()])
    meal_type = SelectField('Meal type', choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], validators=[DataRequired()])
    meal = StringField('Meal', validators=[DataRequired()])
    calories = IntegerField('Calories', validators=[DataRequired()])
    protein = StringField('Protein', validators=[DataRequired()])
    carbs = StringField('Carbs', validators=[DataRequired()])
    fat = StringField('Fat', validators=[DataRequired()])
