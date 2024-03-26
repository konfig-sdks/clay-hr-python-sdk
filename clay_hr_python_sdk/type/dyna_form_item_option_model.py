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

class RequiredDynaFormItemOptionModel(TypedDict):
    pass

class OptionalDynaFormItemOptionModel(TypedDict, total=False):
    cid: int

    createts: Timestamp

    dynaFormItemId: int

    optionId: int

    optionValue: str

class DynaFormItemOptionModel(RequiredDynaFormItemOptionModel, OptionalDynaFormItemOptionModel):
    pass
