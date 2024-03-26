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

class ContactModel(BaseModel):
    address_model_list: typing.Optional[typing.List[AddressModel]] = Field(None, alias='addressModelList')

    candidate_id: typing.Optional[int] = Field(None, alias='candidateId')

    cid: typing.Optional[int] = Field(None, alias='cid')

    contact_type: typing.Optional[str] = Field(None, alias='contactType')

    contactid: typing.Optional[int] = Field(None, alias='contactid')

    createuserid: typing.Optional[int] = Field(None, alias='createuserid')

    date_of_birth: typing.Optional[date] = Field(None, alias='dateOfBirth')

    email1: typing.Optional[str] = Field(None, alias='email1')

    gender: typing.Optional[str] = Field(None, alias='gender')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    name: typing.Optional[str] = Field(None, alias='name')

    notes: typing.Optional[str] = Field(None, alias='notes')

    other_relation_to_user: typing.Optional[str] = Field(None, alias='otherRelationToUser')

    phone1: typing.Optional[str] = Field(None, alias='phone1')

    phone1type: typing.Optional[str] = Field(None, alias='phone1type')

    phone2: typing.Optional[str] = Field(None, alias='phone2')

    phone2type: typing.Optional[str] = Field(None, alias='phone2type')

    phone3: typing.Optional[str] = Field(None, alias='phone3')

    phone3type: typing.Optional[str] = Field(None, alias='phone3type')

    relation_to_user: typing.Optional[str] = Field(None, alias='relationToUser')

    status: typing.Optional[str] = Field(None, alias='status')

    tax_number: typing.Optional[str] = Field(None, alias='taxNumber')

    user_id: typing.Optional[int] = Field(None, alias='userId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
