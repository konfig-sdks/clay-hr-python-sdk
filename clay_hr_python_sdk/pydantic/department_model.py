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

from clay_hr_python_sdk.pydantic.user_view_model import UserViewModel

class DepartmentModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    cid: typing.Optional[int] = Field(None, alias='cid')

    department_code: typing.Optional[str] = Field(None, alias='departmentCode')

    department_id: typing.Optional[int] = Field(None, alias='departmentId')

    department_label: typing.Optional[str] = Field(None, alias='departmentLabel')

    dept_head: typing.Optional[int] = Field(None, alias='deptHead')

    dept_head_name: typing.Optional[str] = Field(None, alias='deptHeadName')

    name: typing.Optional[str] = Field(None, alias='name')

    no_of_employees: typing.Optional[int] = Field(None, alias='noOfEmployees')

    parent_department_id: typing.Optional[int] = Field(None, alias='parentDepartmentId')

    parent_department_name: typing.Optional[str] = Field(None, alias='parentDepartmentName')

    user_model: typing.Optional[UserViewModel] = Field(None, alias='userModel')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
