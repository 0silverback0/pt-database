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
