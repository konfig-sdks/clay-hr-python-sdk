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


class Timestamp(BaseModel):
    date: typing.Optional[int] = Field(None, alias='date')

    hours: typing.Optional[int] = Field(None, alias='hours')

    minutes: typing.Optional[int] = Field(None, alias='minutes')

    month: typing.Optional[int] = Field(None, alias='month')

    nanos: typing.Optional[int] = Field(None, alias='nanos')

    seconds: typing.Optional[int] = Field(None, alias='seconds')

    time: typing.Optional[int] = Field(None, alias='time')

    year: typing.Optional[int] = Field(None, alias='year')

    day: typing.Optional[int] = Field(None, alias='day')

    timezone_offset: typing.Optional[int] = Field(None, alias='timezoneOffset')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
