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


class RequiredPeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem(TypedDict):
    pass

class OptionalPeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem(TypedDict, total=False):
    value: typing.Union[int, float]

    # Time period for compensation. HRLY - Hourly, DLY - Daily, WKLY - Weekly, BWKLY - Bi-Weekly, MTHLY - Monthly, BMTH - Bi-Monthly, QTRLY - Quarterly, BYRLY - Bi-Yearly, YRLY - Yearly, ONEF - OneOff
    period: str

    financialType: str

    currencyCode: str

    effectivedate: str

    # Type of compensation. sal - Salary, pay - Compensation, INCTV - Incentive, SVCR - Severance
    compensationType: str

    # Status of compensation. ACTV - Active, ARCHV - Archive, PVNL - Provisional
    status: str

    changeTypeId: int

    changeTypeCode: str

    extAppUID: str

class PeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem(RequiredPeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem, OptionalPeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem):
    pass
