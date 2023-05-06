from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.init_app(app)

class Trainer(db.Model):
    __tablename__ = 'trainer'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64),unique=True)
    clients = db.relationship('Client', backref='trainer', lazy=True, cascade="all, delete-orphan")

class Client(db.Model):
    __tablename__ = 'client'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.String, primary_key=True)
    trainer_id = db.Column(db.String, db.ForeignKey('trainer.id'))
    name = db.Column(db.String(64))
    email = db.Column(db.String(64))
    workouts = db.relationship('Workout', backref='client', lazy=True, cascade="all, delete-orphan")

class Workout(db.Model):
    __tablename__ = 'workout'
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.String, primary_key=True)
    client_id = db.Column(db.String, db.ForeignKey('client.id'))
    name = db.Column(db.String(64))
    description = db.Column(db.String(128))

class MealPlan(db.Model):
    __tablename__ = 'meal_plan'

    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String)
    meal_type = db.Column(db.String)
    meal = db.Column(db.String)
    calories = db.Column(db.Float)
    protein = db.Column(db.Float)
    carbs = db.Column(db.Float)
    fat = db.Column(db.Float)
    meal_plan_id = db.Column(db.Integer, db.ForeignKey('meal_plan_summary.id'))
    meal_plan = db.relationship("MealPlanSummary", back_populates="meal_plan")

class MealPlanSummary(db.Model):
    __tablename__ = 'meal_plan_summary'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    meal_plan = db.relationship("MealPlan", back_populates="meal_plan")

