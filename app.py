from flask import Flask
from models import connect_db, db, Trainer, Client, Workout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Deja1218@localhost/open-source'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
   

@app.route('/')
def index():
    return 'hey'
