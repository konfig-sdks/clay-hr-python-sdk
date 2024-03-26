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


class SkillViewModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    average: typing.Optional[typing.Union[int, float]] = Field(None, alias='average')

    cid: typing.Optional[int] = Field(None, alias='cid')

    score_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='scoreMax')

    score_name: typing.Optional[str] = Field(None, alias='scoreName')

    score_template_id: typing.Optional[int] = Field(None, alias='scoreTemplateId')

    skill_code: typing.Optional[str] = Field(None, alias='skillCode')

    skill_id: typing.Optional[int] = Field(None, alias='skillId')

    skill_type_id: typing.Optional[int] = Field(None, alias='skillTypeId')

    skill_type_name: typing.Optional[str] = Field(None, alias='skillTypeName')

    socre_min: typing.Optional[typing.Union[int, float]] = Field(None, alias='socreMin')

    status: typing.Optional[str] = Field(None, alias='status')

    user_count: typing.Optional[int] = Field(None, alias='userCount')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
