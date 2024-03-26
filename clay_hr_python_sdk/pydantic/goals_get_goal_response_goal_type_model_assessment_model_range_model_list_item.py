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


class GoalsGetGoalResponseGoalTypeModelAssessmentModelRangeModelListItem(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    strangeid: typing.Optional[str] = Field(None, alias='strangeid')

    score_temp_id: typing.Optional[str] = Field(None, alias='scoreTempId')

    range_min: typing.Optional[str] = Field(None, alias='rangeMin')

    range_max: typing.Optional[str] = Field(None, alias='rangeMax')

    interpretation: typing.Optional[str] = Field(None, alias='interpretation')

    color_code: typing.Optional[str] = Field(None, alias='colorCode')

    cid: typing.Optional[str] = Field(None, alias='cid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
