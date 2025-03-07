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

from clay_hr_python_sdk.pydantic.custom_list_entry_model import CustomListEntryModel

class CustomListModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    cid: typing.Optional[int] = Field(None, alias='cid')

    custom_list_entry_model: typing.Optional[typing.List[CustomListEntryModel]] = Field(None, alias='customListEntryModel')

    list_id: typing.Optional[int] = Field(None, alias='listId')

    list_name: typing.Optional[str] = Field(None, alias='listName')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
