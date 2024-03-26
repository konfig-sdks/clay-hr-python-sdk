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


class PeopleAndPermissionsCreateOrUpdateUserDetailsRequestContactListItem(BaseModel):
    name: typing.Optional[str] = Field(None, alias='name')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    relation_to_user: typing.Optional[Literal["Spouse", "Parent", "Child", "Other"]] = Field(None, alias='relationToUser')

    contact_type: typing.Optional[Literal["DEP", "ECON", "ACCT"]] = Field(None, alias='contactType')

    gender: typing.Optional[Literal["M", "F", "H"]] = Field(None, alias='gender')

    tax_number: typing.Optional[str] = Field(None, alias='taxNumber')

    date_of_birth: typing.Optional[str] = Field(None, alias='dateOfBirth')

    status: typing.Optional[Literal["AP", "WA"]] = Field(None, alias='status')

    ext_app_u_i_d: typing.Optional[str] = Field(None, alias='extAppUID')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
