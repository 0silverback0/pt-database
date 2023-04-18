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
- be sure to have postgres installed on your machine
- fork this repo 
- then create a clone of the forked repo on your machine
- in the terminal cd to the new directory pt-database `cd pt-database`
- create a new virtual environment `python3 -m venv venv`
- next install the dependencies `pip install -r requirements.txt`

### Create Database
- in the terminal run `createdb <database name>`

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
