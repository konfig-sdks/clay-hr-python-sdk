# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredAuthenticationGetAccessToken403Response(TypedDict):
    pass

class OptionalAuthenticationGetAccessToken403Response(TypedDict, total=False):
    message: str

class AuthenticationGetAccessToken403Response(RequiredAuthenticationGetAccessToken403Response, OptionalAuthenticationGetAccessToken403Response):
    pass
