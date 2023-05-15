from flask import Flask, render_template, redirect, url_for, request
from models import connect_db, db, Trainer, Client, Workout, MealPlan
from mealform import MealForm
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

connect_db(app)

# with app.app_context():
#     trainer = Trainer.query.first()
#     clients = trainer.clients

@app.route('/', methods=['GET', 'POST'])
def index():
    form = MealForm()
    if form.validate_on_submit():
        day = form.day.data
        meal = form.meal.data
        meal_type = form.meal_type.data
        meal = form.meal.data
        calories = form.calories.data
        protein = form.protein.data
        carbs = form.carbs.data
        fat = form.fat.data

        print( day, meal, meal_type, calories, protein, carbs, fat)

    return render_template('index.html', form=form)
   

@app.route('/add_meal', methods=['GET', 'POST'])
def add_meal():
  form = MealForm()
  if form.validate():
    # Get data from form
    client = form.client.data
    day = form.day.data
    meal_type = form.meal_type.data
    meal = form.meal.data
    calories = form.calories.data
    protein = form.protein.data
    carbs = form.carbs.data
    fat = form.fat.data

    # Redirect to meal list
    return redirect(url_for('list_meals'))
  else:
    # Render form with errors
    return render_template('add_meal.html', form=form)
  
@app.route('/list_meals')
def list_meals():
    meals = MealPlan.query.all()
    return render_template('list_meals.html', meals=meals)

@app.route('/meal_plan/<int:meal_plan_id>')
def meal_plan(meal_plan_id):
    meal_plan_details = MealPlan.query.filter_by(id=meal_plan_id).all()
    print(meal_plan_details[0].id)
    return render_template('meal_plan.html', meal_plan_details=meal_plan_details)