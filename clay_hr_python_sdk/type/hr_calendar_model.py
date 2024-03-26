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

from clay_hr_python_sdk.type.timestamp import Timestamp
from clay_hr_python_sdk.type.user_view_model import UserViewModel

class RequiredHRCalendarModel(TypedDict):
    pass

class OptionalHRCalendarModel(TypedDict, total=False):
    calendarId: int

    cid: int

    colorCode: str

    createUserId: int

    createUserViewModel: UserViewModel

    createts: Timestamp

    name: str

class HRCalendarModel(RequiredHRCalendarModel, OptionalHRCalendarModel):
    pass
