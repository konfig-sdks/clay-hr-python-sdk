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


class PeopleAndPermissionsSaveUserAddressRequestRawBodyItem(BaseModel):
    address_line1: typing.Optional[str] = Field(None, alias='addressLine1')

    address_line2: typing.Optional[str] = Field(None, alias='addressLine2')

    address_type: typing.Optional[str] = Field(None, alias='addressType')

    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    city: typing.Optional[str] = Field(None, alias='city')

    # Country Idenifier (should be a number id).
    country_id: typing.Optional[str] = Field(None, alias='countryId')

    state: typing.Optional[str] = Field(None, alias='state')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
