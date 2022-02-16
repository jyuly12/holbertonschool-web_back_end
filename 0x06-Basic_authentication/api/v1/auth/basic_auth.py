#!/usr/bin/env python3
""" Basic authetication definition
"""
from api.v1.auth.auth import Auth


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
