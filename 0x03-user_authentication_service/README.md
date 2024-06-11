
User Authentication Service

This project implements a user authentication service using Flask and SQLAlchemy. The goal is to understand the mechanisms behind user authentication by building a service from scratch. The project includes tasks such as creating a user model, hashing passwords, validating login credentials, and managing user sessions.

Learning Objectives
By the end of this project, you should be able to:

Declare API routes in a Flask app.
Handle cookies in Flask.
Retrieve and process request form data.
Return various HTTP status codes.

Requirements

Editors: vi, vim, emacs
Environment: Ubuntu 18.04 LTS, Python 3.7
Code Style: pycodestyle (version 2.5)
ORM: SQLAlchemy 1.3.x
All files must end with a new line.
The first line of all files should be #!/usr/bin/env python3.
All files must be executable.
All modules, classes, and functions must have proper documentation.
All functions should be type annotated.

Setup
Install bcrypt:

pip3 install bcrypt


Project Structure

alx-backend-user-data/
├── 0x03-user_authentication_service/
│   ├── app.py
│   ├── auth.py
│   ├── db.py
│   ├── user.py
│   ├── README.md
│   └── ...

Tasks
0. User Model
Create a SQLAlchemy model named User for the users table with the following attributes:

id (integer primary key)
email (non-nullable string)
hashed_password (non-nullable string)
session_id (nullable string)
reset_token (nullable string)
1. Create User
Implement the DB.add_user method to save a new user to the database. This method takes email and hashed_password as arguments and returns a User object.

2. Find User
Implement the DB.find_user_by method. This method takes arbitrary keyword arguments and returns the first row found in the users table. Raise NoResultFound or InvalidRequestError as appropriate.

3. Update User
Implement the DB.update_user method to update user attributes. This method takes a user_id and arbitrary keyword arguments. Use find_user_by to locate the user and update their attributes.

4. Hash Password
Define a _hash_password method that takes a password string and returns its salted hash using bcrypt.hashpw.

5. Register User
Implement Auth.register_user to register a new user. If the user already exists, raise a ValueError. Otherwise, hash the password, save the user, and return the User object.

6. Basic Flask App
Set up a basic Flask app with a single GET route (/) that returns a JSON payload {"message": "Bienvenue"}.

7. Register User Endpoint
Implement a users function to handle POST /users requests. This endpoint registers a new user or returns an error if the user already exists.

8. Credentials Validation
Implement Auth.valid_login to validate login credentials. This method should return True if the credentials are correct and False otherwise.

9. Generate UUIDs
Implement a _generate_uuid function that returns a string representation of a new UUID.

10. Get Session ID
Implement Auth.create_session to create a new session for a user and return the session ID.

11. Log In
Implement a login function to handle POST /sessions requests. If the credentials are correct, create a session and store the session ID as a cookie.

12. Find User by Session ID
Implement Auth.get_user_from_session_id to return a user corresponding to a given session ID.

13. Destroy Session
Implement Auth.destroy_session to destroy a user's session by setting their session_id to None.

14. Log Out
Implement a logout function to handle DELETE /sessions requests. This endpoint should destroy the user's session and redirect to the root URL.

15. User Profile
Implement a profile function to handle GET /profile requests. This endpoint returns the user's email if the session ID is valid or returns a 403 status if not.

Running the Application
Start the Flask App:

python3 app.py

Example Requests:

Register a user:
curl -XPOST localhost:5000/users -d 'email=bob@bob.com' -d 'password=mySuperPwd'

Log in:
curl -XPOST localhost:5000/sessions -d 'email=bob@bob.com' -d 'password=mySuperPwd'

Get profile:
curl -XGET localhost:5000/profile -b "session_id=<session_id>"

Log out:
curl -XDELETE localhost:5000/sessions -b "session_id=<session_id>
