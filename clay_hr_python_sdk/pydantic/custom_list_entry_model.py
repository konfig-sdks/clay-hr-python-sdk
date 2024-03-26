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


class CustomListEntryModel(BaseModel):
    cid: typing.Optional[int] = Field(None, alias='cid')

    entry_code: typing.Optional[str] = Field(None, alias='entryCode')

    entry_id: typing.Optional[int] = Field(None, alias='entryId')

    entry_value: typing.Optional[str] = Field(None, alias='entryValue')

    list_id: typing.Optional[int] = Field(None, alias='listId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
