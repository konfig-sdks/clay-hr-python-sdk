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

from clay_hr_python_sdk.type.custom_field_style_model import CustomFieldStyleModel
from clay_hr_python_sdk.type.timestamp import Timestamp

class RequiredCustomTableColumnModel(TypedDict):
    pass

class OptionalCustomTableColumnModel(TypedDict, total=False):
    cid: int

    columnCode: str

    columnHeader: str

    columnType: str

    createts: Timestamp

    ctColumnId: int

    customFieldStyleModel: CustomFieldStyleModel

    customTableId: int

    fieldType: str

    helpText: str

    mandatory: int

    masked: int

    optionValues: str

    sequence: int

    style: str

class CustomTableColumnModel(RequiredCustomTableColumnModel, OptionalCustomTableColumnModel):
    pass
