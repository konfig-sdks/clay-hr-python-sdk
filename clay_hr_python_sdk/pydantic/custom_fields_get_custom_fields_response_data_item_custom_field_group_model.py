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


class CustomFieldsGetCustomFieldsResponseDataItemCustomFieldGroupModel(BaseModel):
    cfgroupid: typing.Optional[str] = Field(None, alias='cfgroupid')

    cfgroupname: typing.Optional[str] = Field(None, alias='cfgroupname')

    cid: typing.Optional[str] = Field(None, alias='cid')

    object_type: typing.Optional[str] = Field(None, alias='objectType')

    access: typing.Optional[str] = Field(None, alias='access')

    layout: typing.Optional[str] = Field(None, alias='layout')

    usergroupid: typing.Optional[str] = Field(None, alias='usergroupid')

    createts: typing.Optional[int] = Field(None, alias='createts')

    sequence: typing.Optional[str] = Field(None, alias='sequence')

    has_custom_fields: typing.Optional[str] = Field(None, alias='hasCustomFields')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
