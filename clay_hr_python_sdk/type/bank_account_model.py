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


class RequiredBankAccountModel(TypedDict):
    pass

class OptionalBankAccountModel(TypedDict, total=False):
    accountCode: str

    accountNumber: str

    accountType: str

    bankAccountId: int

    bankCountryId: int

    branchCode: str

    branchName: str

    cid: int

    countryId: int

    createUserId: int

    name: str

    ownerType: str

    paymentEmail: str

    routingNumber: str

    status: str

    swiftCode: str

    userId: int

class BankAccountModel(RequiredBankAccountModel, OptionalBankAccountModel):
    pass
