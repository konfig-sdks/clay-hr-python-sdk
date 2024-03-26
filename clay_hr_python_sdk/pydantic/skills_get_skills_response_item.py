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


class SkillsGetSkillsResponseItem(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    sequence: typing.Optional[str] = Field(None, alias='sequence')

    create_user_id: typing.Optional[str] = Field(None, alias='createUserId')

    skill_code: typing.Optional[str] = Field(None, alias='skillCode')

    createts: typing.Optional[str] = Field(None, alias='createts')

    id: typing.Optional[str] = Field(None, alias='id')

    status: typing.Optional[str] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
