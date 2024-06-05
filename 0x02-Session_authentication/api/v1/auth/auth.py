#!/usr/bin/env python3
""" Module of Authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """ Class to manage the API authentication """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method for validating if endpoint requires auth """
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        slash_path = path.endswith('/')

        tmp_path = path
        if not slash_path:
            tmp_path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('*'):
                # if the path starts with the excluded path without the '*'
                if path.startswith(excluded_path[:-1]):
                    return False
            else:
                # Check if the path exactly matches the excluded path
                if tmp_path == excluded_path:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ Method that handles authorization header """
        if request is None:
            return None

        return request.headers.get("Authorization", None)

    def current_user(self, request=None) -> TypeVar('User'):
        """ Validates current user """
        return None
