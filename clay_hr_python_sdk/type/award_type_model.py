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

from clay_hr_python_sdk.type.currency_model import CurrencyModel
from clay_hr_python_sdk.type.department_model import DepartmentModel
from clay_hr_python_sdk.type.location_model import LocationModel
from clay_hr_python_sdk.type.timestamp import Timestamp
from clay_hr_python_sdk.type.user_view_model import UserViewModel

class RequiredAwardTypeModel(TypedDict):
    pass

class OptionalAwardTypeModel(TypedDict, total=False):
    description: str

    amount: typing.Union[int, float]

    amountType: str

    awardTypeId: int

    budget: typing.Union[int, float]

    cid: int

    code: str

    createUserId: int

    createts: Timestamp

    currencyCode: str

    currencyModel: CurrencyModel

    departmentModel: DepartmentModel

    locationModel: LocationModel

    managerUserViewModel: UserViewModel

class AwardTypeModel(RequiredAwardTypeModel, OptionalAwardTypeModel):
    pass
