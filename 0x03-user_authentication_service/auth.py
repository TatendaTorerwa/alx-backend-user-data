#!/usr/bin/env python3
"""
Authentication module
"""
import bcrypt
from db import DB
from user import User
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Registers new user
            Args:
                - email: user's email
                - password: user's password
            Return:
                - User instance created
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            user = db.add_user(email, _hash_password(password))
            return user
        else:
            raise ValueError(f"User {email} already exists")

    def valid_login(self, email: str, password: str) -> bool:
        """ Checks if password is valid
            Args:
                - email: user's email
                - password: user's password
            Return:
                - True if credentials are valid, otherwise False
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return False
        if not bcrypt.checkpw(password.encode('utf-8'), user.hashed_password):
            return False
        return True

    def create_session(self, email: str) -> str:
        """ Creates session for user
            Args:
                - email: user's email
            Return:
                - created session_id
        """
        db = self._db
        try:
            user = db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> User:
        """ Gets user based on their session id
            Args:
                - session_id: user's session_id
            Return:
                - User if found else None
        """
        if not session_id:
            return None
        db = self._db
        try:
            user = db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """ Destroys user session
        """
        db = self._db
        db.update_user(user_id, session_id=None)

def get_reset_password_token(self, email: str) -> str:
        """Generates a password reset token for a user.

        Args:
            email (str): A string representing the email address of the user to
            generate a password reset token for.

        Raises:
            ValueError: If no user with the specified email address is found.

        Returns:
            str: A string representing the password reset token generated for
            the user.
        """
        # Find the user with the specified email address
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        # If no user is found with specified email address, raise a ValueError
        if user is None:
            raise ValueError()
        # Generate a new password reset token & update the user's record in db
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        # Return the generated password reset token
        return reset_token

def update_password(self, reset_token: str, password: str) -> None:
        """Updates a user's password using a reset token.

        Args:
            reset_token (str): The reset token associated with the user.
            password (str): The new password to set.

        Raises:
            ValueError: If the reset token is invalid (i.e., not associated
            with a user)..

        Returns:
            None
        """
        # Find user associated with reset_token
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            # If no user found with given reset_token, raise ValueError
            raise ValueError("Invalid reset token")
        # Hash the new password
        new_hashed_password = _hash_password(password)
        # Update the user's hashed password and the reset_token field to None
        self._db.update_user(
            user.id,
            hashed_password=new_hashed_password,
            reset_token=None,
        )

def _hash_password(password: str) -> bytes:
    """ Creates password hash
        Args:
            - password: user password
        Return:
            - hashed password
    """
    e_pwd = password.encode()
    return bcrypt.hashpw(e_pwd, bcrypt.gensalt())


def _generate_uuid() -> str:
    """ Generates unique ids
        Return:
            - UUID generated
    """
    return str(uuid4())
