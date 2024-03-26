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


class RequiredPeopleAndPermissionsDeleteUserAddressResponse(TypedDict):
    pass

class OptionalPeopleAndPermissionsDeleteUserAddressResponse(TypedDict, total=False):
    message: str

class PeopleAndPermissionsDeleteUserAddressResponse(RequiredPeopleAndPermissionsDeleteUserAddressResponse, OptionalPeopleAndPermissionsDeleteUserAddressResponse):
    pass
