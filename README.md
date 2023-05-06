# Welcome to the Trainer App
This app is designed to help personal trainers and their clients manage their workouts. It includes the following models:

Trainer
Client
Workout
The Trainer model stores information about the trainer, including their name and email address.

The Client model stores information about each client, including their name and email address.

The Workout model stores information about each workout, including its name and description.

This app is built using Flask, SQLAlchemy, and Python.

## How to Install
- Be sure to have postgres installed on your machine
- Fork this repo then create a new branch for your changes
- In the terminal cd to the new directory pt-database `cd pt-database`
- Create a new virtual environment `python3 -m venv venv`
- Next install the dependencies `pip install -r requirements.txt`
- In the terminal run `createdb <database name>` replace database name with the name you want
- In the root directory create a .env file and add your database URI `postgresql://<username>:<password>@localhost/<database name>`
- Run the seed.py file to pre-fill the database, type `python3 seed.py` in the terminal and press enter
- Login to the database type, `psql <database name>` in the terminal
- Finally type `\dt` and you should see the schema

## Database Models
### This section contains the database models used in this application.
#### Trainer
The Trainer model is used to store information about trainers.

| Attribute | Type | Description |
| ---------- | ------ | ------------------------------------ |
| id | String | Unique identifier for the trainer |
| name | String | Name of the trainer |
| email | String | Email address of the trainer |
| clients | Array | Array of associated Client objects |

Client
The Client model is used to store information about clients.

| Attribute | Type | Description |
| ---------- | ------ | ------------------------------------ |
| id | String | Unique identifier for the client |
| trainer_id | String | Unique identifier for the trainer |
| name | String | Name of the client |
| email | String | Email address of the client |
| workouts | Array | Array of associated Workout objects |

Workout
The Workout model is used to store information about workouts.

| Attribute | Type | Description |
| ---------- | ------ | ------------------------------------ |
| id | String | Unique identifier for the workout |
| client_id | String | Unique identifier for the client |
| name | String | Name of the workout |
| description| String | Description of the workout |

# MealPlan

This is a class that represents a meal plan in a database. It is a subclass of `db.Model`, which suggests that it is designed to work with a SQLAlchemy database.

| Attribute | Type | Description |
| ---------- | ------ | ------------------------------------ |
| id | Integer | Unique identifier for the meal plan |
| day | String | Day of the week for a particular meal |
| meal_type | String | Type of meal (e.g. breakfast, lunch, dinner) |
| meal | String | Name of the meal |
| calories | Float | Number of calories in the meal |
| protein | Float | Amount of protein in the meal |
| carbs | Float | Amount of carbohydrates in the meal |
| fat | Float | Amount of fat in the meal |
| meal_plan_id | Integer | Foreign key to the id column of the meal_plan_summary table |

## Relationships

* `meal_plan`: A relationship to the `MealPlanSummary` class via the `meal_plan` attribute. This relationship is defined in the `MealPlan` class.


# MealPlanSummary

This is a class that represents a meal plan summary in a database. It is a subclass of `db.Model`, which suggests that it is designed to work with a SQLAlchemy database.

| Attribute | Type | Description |
| ---------- | ------ | ------------------------------------ |
| id | Integer | Unique identifier for the meal plan summary |
| name | String | Name of the meal plan |

## Relationships

* `meal_plan`: A relationship to the `MealPlan` class via the `meal_plan` attribute. This relationship is defined in the `MealPlanSummary` class.


## Usage
To start writing SQL queries against the database login by typing `psql <database name>` in the terminal. From there you can view the tables by typing
`\dt` there you will be able to see the tables in the database. You can then begin typing queries.

## Sample Queries

### Insert Data
`INSERT INTO trainer (id, name, email) VALUES ('123', 'John Doe', 'john@example.com');`

`INSERT INTO client (id, trainer_id, name, email) VALUES ('456', '123', 'Jane Doe', 'jane@example.com');`

`INSERT INTO workout (id, client_id, name, description) VALUES ('789', '456', 'Workout 1', 'This is a sample workout');`

### Select Data
`SELECT * FROM trainer;`

`SELECT * FROM client;`

`SELECT * FROM workout;`

## Troubleshooting Steps

1. Check your database connection: Verify that your Flask app is able to connect to the PostgreSQL database. Check that the database server is running and that your app's database configuration settings are correct. If the connection is unsuccessful, check the error message to identify the cause of the problem.

2. Verify that the database schema exists: Make sure that the database schema you are using in your Flask app has been created in the PostgreSQL database. If the schema does not exist, create it using the appropriate SQL commands or by using a database migration tool like Alembic.

3. Check your SQL queries: Review your SQL queries to ensure that they are correct and formatted properly. Use a tool like pgAdmin to test your queries directly against the PostgreSQL database. You can also use logging to see the SQL queries generated by your Flask app.

4. Debug your Flask app: Enable Flask's built-in debugging features to help identify any issues with your app's code. This can include using Flask's `debug=True` option, setting breakpoints in your code, and using logging to track the flow of your app.

5. Check your PostgreSQL logs: Examine the PostgreSQL server logs to see if there are any errors or issues reported by the database server. This can help identify problems with your database configuration, queries, or schema.

6. Check your dependencies: Make sure that all the dependencies used by your Flask app and PostgreSQL database are up-to-date and compatible with each other. Use a virtual environment to isolate your app's dependencies and prevent conflicts.

7. Verify your server configuration: Check your server configuration to ensure that it is set up correctly to run your Flask app and PostgreSQL database. This can include verifying the installation of required packages, checking system resources like memory and disk space, and making sure that the server is configured to allow connections to the database.

By following these troubleshooting steps, you can identify and resolve issues with your Flask app and PostgreSQL database, and ensure that your app is running smoothly.
