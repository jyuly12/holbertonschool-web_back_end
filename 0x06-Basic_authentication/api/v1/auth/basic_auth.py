#!/usr/bin/env python3
""" Basic authetication definition
"""

from api.v1.auth.auth import Auth
import base64


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

    def decode_base64_authorization_header(
                                            self,
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
