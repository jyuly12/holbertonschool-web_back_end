#!/usr/bin/env python3
""" Basic Authentication module
"""
from queue import Empty
from flask import request
from typing import List, TypeVar


class Auth():
    """ Authentication process
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method
        """
        if path is None:
            return True

        if (excluded_paths is None) or not len(excluded_paths):
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """ public method
        """
        if request is None:
            return None
        if "Authorization" not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method
        """
        return None
