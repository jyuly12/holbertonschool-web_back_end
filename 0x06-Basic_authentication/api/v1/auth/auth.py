#!/usr/bin/env python3

from queue import Empty
from flask import request
from typing import List, TypeVar


class Auth():
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ public method
        """
        if path is None:
            return True
        if (excluded_paths is None) or (excluded_paths == ""):
            return True
        for item in excluded_paths:
            if item == path:
                return False
        return False

    def authorization_header(self, request=None) -> str:
        """ public method
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ public method
        """
        return None
