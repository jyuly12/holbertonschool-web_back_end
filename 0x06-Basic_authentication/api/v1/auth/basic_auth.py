#!/usr/bin/env python3
""" Basic authetication definition
"""
from api.v1.auth.auth import Auth
import base64
from re import search
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ Authentication process
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Returns the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None

        if type(authorization_header) is not str:
            return None

        header = authorization_header.split(" ")
        if header[0] != "Basic":
            return None
        else:
            return header[1]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """ Decoded value of a Base64 string
        """
        if base64_authorization_header is None:
            return None

        if type(base64_authorization_header) is not str:
            return None

        try:
            encode_value = base64_authorization_header.encode('utf-8')
            decode_value = base64.b64decode(encode_value)
            decoded_Value = decode_value.decode('utf-8')
            return decoded_Value
        except Exception:
            return None

    def extract_user_credentials(
                                    self,
                                    decoded_base64_authorization_header: str
                                    ) -> (str, str):
        """ Function that returns the user email and password.
        """

        if decoded_base64_authorization_header is None:
            return (None, None)

        if type(decoded_base64_authorization_header) is not str:
            return (None, None)

        value = decoded_base64_authorization_header.split(":")
        if len(value) >= 2:
            return (value[0], value[1])
        else:
            return (None, None)

    def user_object_from_credentials(
                                        self,
                                        user_email: str,
                                        user_pwd: str
                                        ) -> TypeVar('User'):
        """ Returns the User instance based on his email
            and password.
        """

        if user_email is None or type(user_email) is not str:
            return None

        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Basic authentication.
        """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
            return user
        except Exception:
            return None
