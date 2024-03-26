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


class GoalsGetGoalResponseAssignedUserModelDepartmentModelUserModel(BaseModel):
    user_id: typing.Optional[str] = Field(None, alias='userId')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    name: typing.Optional[str] = Field(None, alias='name')

    phone: typing.Optional[str] = Field(None, alias='phone')

    email: typing.Optional[str] = Field(None, alias='email')

    status: typing.Optional[str] = Field(None, alias='status')

    short_name: typing.Optional[str] = Field(None, alias='shortName')

    thumbnail: typing.Optional[str] = Field(None, alias='thumbnail')

    gender: typing.Optional[str] = Field(None, alias='gender')

    job_title: typing.Optional[str] = Field(None, alias='jobTitle')

    department_id: typing.Optional[str] = Field(None, alias='departmentId')

    location_id: typing.Optional[str] = Field(None, alias='locationId')

    department: typing.Optional[str] = Field(None, alias='department')

    location: typing.Optional[str] = Field(None, alias='location')

    profile_id: typing.Optional[str] = Field(None, alias='profileId')

    timezone: typing.Optional[str] = Field(None, alias='timezone')

    user_startdate: typing.Optional[str] = Field(None, alias='userStartdate')

    user_enddate: typing.Optional[str] = Field(None, alias='userEnddate')

    cell_phone: typing.Optional[str] = Field(None, alias='cellPhone')

    emp_id: typing.Optional[str] = Field(None, alias='empId')

    userdate_of_birth: typing.Optional[str] = Field(None, alias='userdateOfBirth')

    allocation: typing.Optional[str] = Field(None, alias='allocation')

    userdate_format: typing.Optional[str] = Field(None, alias='userdateFormat')

    star: typing.Optional[str] = Field(None, alias='star')

    image_name: typing.Optional[str] = Field(None, alias='imageName')

    notes: typing.Optional[str] = Field(None, alias='notes')

    im: typing.Optional[str] = Field(None, alias='im')

    createuserid: typing.Optional[str] = Field(None, alias='createuserid')

    country_id: typing.Optional[str] = Field(None, alias='countryId')

    cid: typing.Optional[str] = Field(None, alias='cid')

    guid: typing.Optional[str] = Field(None, alias='guid')

    has_access: typing.Optional[str] = Field(None, alias='hasAccess')

    display_name: typing.Optional[str] = Field(None, alias='displayName')

    id: typing.Optional[str] = Field(None, alias='id')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
