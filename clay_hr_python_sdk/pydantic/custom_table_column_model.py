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
from pydantic import BaseModel, Field, RootModel, ConfigDict

from clay_hr_python_sdk.pydantic.custom_field_style_model import CustomFieldStyleModel
from clay_hr_python_sdk.pydantic.timestamp import Timestamp

class CustomTableColumnModel(BaseModel):
    cid: typing.Optional[int] = Field(None, alias='cid')

    column_code: typing.Optional[str] = Field(None, alias='columnCode')

    column_header: typing.Optional[str] = Field(None, alias='columnHeader')

    column_type: typing.Optional[str] = Field(None, alias='columnType')

    createts: typing.Optional[Timestamp] = Field(None, alias='createts')

    ct_column_id: typing.Optional[int] = Field(None, alias='ctColumnId')

    custom_field_style_model: typing.Optional[CustomFieldStyleModel] = Field(None, alias='customFieldStyleModel')

    custom_table_id: typing.Optional[int] = Field(None, alias='customTableId')

    field_type: typing.Optional[str] = Field(None, alias='fieldType')

    help_text: typing.Optional[str] = Field(None, alias='helpText')

    mandatory: typing.Optional[int] = Field(None, alias='mandatory')

    masked: typing.Optional[int] = Field(None, alias='masked')

    option_values: typing.Optional[str] = Field(None, alias='optionValues')

    sequence: typing.Optional[int] = Field(None, alias='sequence')

    style: typing.Optional[str] = Field(None, alias='style')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
