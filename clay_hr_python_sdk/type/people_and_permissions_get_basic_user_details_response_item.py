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


class RequiredPeopleAndPermissionsGetBasicUserDetailsResponseItem(TypedDict):
    pass

class OptionalPeopleAndPermissionsGetBasicUserDetailsResponseItem(TypedDict, total=False):
    userId: str

    firstName: str

    lastName: str

    name: str

    phone: str

    email: str

    status: str

    shortName: str

    timezone: str

    userStartDate: str

    cellPhone: str

    allocation: str

    userDateFormat: str

    star: str

    createuserid: str

    cid: str

    guid: str

    hasAccess: str

class PeopleAndPermissionsGetBasicUserDetailsResponseItem(RequiredPeopleAndPermissionsGetBasicUserDetailsResponseItem, OptionalPeopleAndPermissionsGetBasicUserDetailsResponseItem):
    pass
