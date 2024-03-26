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


class RequiredObjectiveGetByUserIdOrSpecificObjectiveById401Response(TypedDict):
    pass

class OptionalObjectiveGetByUserIdOrSpecificObjectiveById401Response(TypedDict, total=False):
    message: str

class ObjectiveGetByUserIdOrSpecificObjectiveById401Response(RequiredObjectiveGetByUserIdOrSpecificObjectiveById401Response, OptionalObjectiveGetByUserIdOrSpecificObjectiveById401Response):
    pass
