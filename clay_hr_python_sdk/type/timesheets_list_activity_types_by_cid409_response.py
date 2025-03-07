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


class RequiredTimesheetsListActivityTypesByCid409Response(TypedDict):
    pass

class OptionalTimesheetsListActivityTypesByCid409Response(TypedDict, total=False):
    message: str

class TimesheetsListActivityTypesByCid409Response(RequiredTimesheetsListActivityTypesByCid409Response, OptionalTimesheetsListActivityTypesByCid409Response):
    pass
