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


class RequiredPositionStatusModel(TypedDict):
    pass

class OptionalPositionStatusModel(TypedDict, total=False):
    cid: int

    defaultStatus: bool

    internalStatus: str

    statusId: int

    statusName: str

class PositionStatusModel(RequiredPositionStatusModel, OptionalPositionStatusModel):
    pass
