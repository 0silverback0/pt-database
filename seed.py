from app import app
from models import db, Trainer, Client, Workout

with app.app_context():
    db.drop_all()
    db.create_all()

# Create trainers
trainer1 = Trainer(id='1', name='John', email='john@example.com')
trainer2 = Trainer(id='2', name='Jane', email='jane@example.com')

#Create clients
client_1 = Client(
    id='1', 
    trainer_id='1', 
    name='John Doe',
    email='john.doe@example.com'
)

client_2 = Client(
    id='2', 
    trainer_id='1', 
    name='Jane Doe',
    email='jane.doe@example.com'
)

client_3 = Client(
    id='3', 
    trainer_id='2', 
    name='Jack Johnson',
    email='jack.johnson@example.com'
)

client_4 = Client(
    id='4', 
    trainer_id='2', 
    name='Jill Johnson',
    email='jill.johnson@example.com'
)

#Create workouts
workout1 = Workout(id="1", client_id="1", name="Running", description="5km jog")
workout2 = Workout(id="2", client_id="2", name="Swimming", description="400m freestyle")
workout3 = Workout(id="3", client_id="3", name="Cycling", description="30km ride")

with app.app_context():
   trainer1.clients.append(client_1)
   trainer2.clients.append(client_2)
   trainer1.clients.append(client_3)
   trainer2.clients.append(client_4)
   db.session.add_all([trainer1, trainer2, client_1,
                       client_2, client_3, client_4, workout1,
                       workout2, workout3])
    # Commit the changes to the database
   db.session.commit()

