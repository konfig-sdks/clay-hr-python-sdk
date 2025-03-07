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

from clay_hr_python_sdk.pydantic.address_model import AddressModel

class LocationModel(BaseModel):
    address: typing.Optional[str] = Field(None, alias='address')

    address_model_list: typing.Optional[typing.List[AddressModel]] = Field(None, alias='addressModelList')

    cid: typing.Optional[int] = Field(None, alias='cid')

    createuserid: typing.Optional[int] = Field(None, alias='createuserid')

    lattitude: typing.Optional[str] = Field(None, alias='lattitude')

    location_code: typing.Optional[str] = Field(None, alias='locationCode')

    location_description: typing.Optional[str] = Field(None, alias='locationDescription')

    location_id: typing.Optional[int] = Field(None, alias='locationId')

    location_label: typing.Optional[str] = Field(None, alias='locationLabel')

    location_name: typing.Optional[str] = Field(None, alias='locationName')

    location_type: typing.Optional[str] = Field(None, alias='locationType')

    location_u_i_d: typing.Optional[str] = Field(None, alias='locationUID')

    longitude: typing.Optional[str] = Field(None, alias='longitude')

    parent_location_id: typing.Optional[int] = Field(None, alias='parentLocationId')

    status: typing.Optional[str] = Field(None, alias='status')

    working_days: typing.Optional[str] = Field(None, alias='workingDays')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
