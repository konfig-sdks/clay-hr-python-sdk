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


class RequiredLeavesAddPtoBalanceRequest(TypedDict):
    # PTO Balance of user.
    ptobalances: str

class OptionalLeavesAddPtoBalanceRequest(TypedDict, total=False):
    pass

class LeavesAddPtoBalanceRequest(RequiredLeavesAddPtoBalanceRequest, OptionalLeavesAddPtoBalanceRequest):
    pass
