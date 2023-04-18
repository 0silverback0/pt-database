# Database Models
## This section contains the database models used in this application.
### Trainer
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
