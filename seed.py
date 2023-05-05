from app import app
from models import db, Trainer, Client, Workout, MealPlan, MealPlanSummary

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

# Create a MealPlanSummary object
summary = MealPlanSummary(name="John Doe")
summary1 = MealPlanSummary(name='Jane Smith')

# Create MealPlan objects for each meal on each day of the week
monday_breakfast = MealPlan(day='Monday', meal_type='Breakfast', meal='Oatmeal', calories=350, protein=15, carbs=55, fat=7)
monday_lunch = MealPlan(day='Monday', meal_type='Lunch', meal='Turkey Sandwich', calories=450, protein=25, carbs=40, fat=18)
monday_dinner = MealPlan(day='Monday', meal_type='Dinner', meal='Grilled Chicken with Quinoa', calories=550, protein=45, carbs=40, fat=12)
tuesday_breakfast = MealPlan(day='Tuesday', meal_type='Breakfast', meal='Scrambled Eggs with Avocado', calories=400, protein=20, carbs=10, fat=30)
tuesday_lunch = MealPlan(day='Tuesday', meal_type='Lunch', meal='Tuna Salad', calories=350, protein=30, carbs=20, fat=15)
tuesday_dinner = MealPlan(day='Tuesday', meal_type='Dinner', meal='Salmon with Roasted Vegetables', calories=600, protein=40, carbs=30, fat=25)
# Repeat for Wednesday through Sunday

#jane smiths objects
meal1 = MealPlan(day='Monday', meal_type='Breakfast', meal='Scrambled eggs with spinach and whole grain toast', calories=350, protein=25, carbs=35, fat=12)
meal2 = MealPlan(day='Monday', meal_type='Lunch', meal='Grilled chicken salad with mixed greens, tomatoes, and balsamic vinaigrette', calories=400, protein=40, carbs=20, fat=18)
meal3 = MealPlan(day='Monday', meal_type='Dinner', meal='Baked salmon with roasted asparagus and quinoa', calories=450, protein=35, carbs=35, fat=20)
meal4 = MealPlan(day='Tuesday', meal_type='Breakfast', meal='Greek yogurt with mixed berries and granola', calories=300, protein=20, carbs=40, fat=6)
meal5 = MealPlan(day='Tuesday', meal_type='Lunch', meal='Turkey and avocado wrap with carrot sticks', calories=400, protein=30, carbs=40, fat=14)
meal6 = MealPlan(day='Tuesday', meal_type='Dinner', meal='Beef stir-fry with broccoli and brown rice', calories=500, protein=40, carbs=45, fat=18)
meal7 = MealPlan(day='Wednesday', meal_type='Breakfast', meal='Protein smoothie with banana, peanut butter, and almond milk', calories=350, protein=25, carbs=30, fat=12)
meal8 = MealPlan(day='Wednesday', meal_type='Lunch', meal='Tuna salad with whole grain crackers', calories=350, protein=30, carbs=25, fat=12)
meal9 = MealPlan(day='Wednesday', meal_type='Dinner', meal='Grilled shrimp skewers with mixed vegetables and quinoa', calories=450, protein=30, carbs=40, fat=16)

# Add the MealPlan objects to the MealPlanSummary object
summary.meal_plan.extend([monday_breakfast, monday_lunch, monday_dinner, tuesday_breakfast, tuesday_lunch, tuesday_dinner]) # Add all MealPlan objects
summary1.meal_plan.extend([meal1, meal2, meal3, meal4, meal5, meal6, meal7, meal8, meal9])

# Add the MealPlanSummary object to the database and commit changes
with app.app_context():
    db.session.add_all([summary, summary1])
    db.session.commit()
