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


class PeopleAndPermissionsGetBasicUserDetailsResponseItem(BaseModel):
    user_id: typing.Optional[str] = Field(None, alias='userId')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    name: typing.Optional[str] = Field(None, alias='name')

    phone: typing.Optional[str] = Field(None, alias='phone')

    email: typing.Optional[str] = Field(None, alias='email')

    status: typing.Optional[str] = Field(None, alias='status')

    short_name: typing.Optional[str] = Field(None, alias='shortName')

    timezone: typing.Optional[str] = Field(None, alias='timezone')

    user_start_date: typing.Optional[str] = Field(None, alias='userStartDate')

    cell_phone: typing.Optional[str] = Field(None, alias='cellPhone')

    allocation: typing.Optional[str] = Field(None, alias='allocation')

    user_date_format: typing.Optional[str] = Field(None, alias='userDateFormat')

    star: typing.Optional[str] = Field(None, alias='star')

    createuserid: typing.Optional[str] = Field(None, alias='createuserid')

    cid: typing.Optional[str] = Field(None, alias='cid')

    guid: typing.Optional[str] = Field(None, alias='guid')

    has_access: typing.Optional[str] = Field(None, alias='hasAccess')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
