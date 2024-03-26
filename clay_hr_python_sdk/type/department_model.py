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

from clay_hr_python_sdk.type.user_view_model import UserViewModel

class RequiredDepartmentModel(TypedDict):
    pass

class OptionalDepartmentModel(TypedDict, total=False):
    description: str

    cid: int

    departmentCode: str

    departmentId: int

    departmentLabel: str

    deptHead: int

    deptHeadName: str

    name: str

    noOfEmployees: int

    parentDepartmentId: int

    parentDepartmentName: str

    userModel: UserViewModel

class DepartmentModel(RequiredDepartmentModel, OptionalDepartmentModel):
    pass
