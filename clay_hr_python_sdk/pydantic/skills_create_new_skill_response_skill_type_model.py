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


class SkillsCreateNewSkillResponseSkillTypeModel(BaseModel):
    skill_type_id: typing.Optional[str] = Field(None, alias='skillTypeId')

    skill_type_name: typing.Optional[str] = Field(None, alias='skillTypeName')

    skill_type_desc: typing.Optional[str] = Field(None, alias='skillTypeDesc')

    skill_view_model_list: typing.Optional[str] = Field(None, alias='skillViewModelList')

    create_user_id: typing.Optional[str] = Field(None, alias='createUserId')

    createts: typing.Optional[str] = Field(None, alias='createts')

    skill_category_model: typing.Optional[str] = Field(None, alias='skillCategoryModel')

    cid: typing.Optional[str] = Field(None, alias='cid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
