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


class PeopleAndPermissionsCreateOrUpdateUserDetailsRequestFinancialListItem(BaseModel):
    value: typing.Optional[typing.Union[int, float]] = Field(None, alias='value')

    # Time period for compensation. HRLY - Hourly, DLY - Daily, WKLY - Weekly, BWKLY - Bi-Weekly, MTHLY - Monthly, BMTH - Bi-Monthly, QTRLY - Quarterly, BYRLY - Bi-Yearly, YRLY - Yearly, ONEF - OneOff
    period: typing.Optional[Literal["HRLY", "DLY", "WKLY", "BWKLY", "BMTH", "MTHLY", "QTRLY", "BYRLY", "YRLY", "ONEF"]] = Field(None, alias='period')

    financial_type: typing.Optional[Literal["COMP"]] = Field(None, alias='financialType')

    currency_code: typing.Optional[str] = Field(None, alias='currencyCode')

    effectivedate: typing.Optional[str] = Field(None, alias='effectivedate')

    # Type of compensation. sal - Salary, pay - Compensation, INCTV - Incentive, SVCR - Severance
    compensation_type: typing.Optional[Literal["sal", "pay", "bonus", "INCTV", "SVRC", "other"]] = Field(None, alias='compensationType')

    # Status of compensation. ACTV - Active, ARCHV - Archive, PVNL - Provisional
    status: typing.Optional[Literal["ACTV", "ARCHV", "PVNL"]] = Field(None, alias='status')

    change_type_id: typing.Optional[int] = Field(None, alias='changeTypeId')

    change_type_code: typing.Optional[str] = Field(None, alias='changeTypeCode')

    ext_app_u_i_d: typing.Optional[str] = Field(None, alias='extAppUID')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
