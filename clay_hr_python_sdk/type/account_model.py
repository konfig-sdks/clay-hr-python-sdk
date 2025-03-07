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

from clay_hr_python_sdk.type.contact_model import ContactModel
from clay_hr_python_sdk.type.user_view_model import UserViewModel

class RequiredAccountModel(TypedDict):
    pass

class OptionalAccountModel(TypedDict, total=False):
    accountCreateUserModel: UserViewModel

    accountDescription: str

    accountId: int

    accountName: str

    accountOwnerModel: ContactModel

    cid: int

    id: int

class AccountModel(RequiredAccountModel, OptionalAccountModel):
    pass
