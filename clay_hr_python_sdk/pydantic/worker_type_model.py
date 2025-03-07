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


class WorkerTypeModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    cid: typing.Optional[int] = Field(None, alias='cid')

    code: typing.Optional[str] = Field(None, alias='code')

    createuserid: typing.Optional[int] = Field(None, alias='createuserid')

    wtid: typing.Optional[int] = Field(None, alias='wtid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
