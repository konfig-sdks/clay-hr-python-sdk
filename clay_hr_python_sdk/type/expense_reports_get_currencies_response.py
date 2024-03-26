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

from clay_hr_python_sdk.type.expense_reports_get_currencies_response_data import ExpenseReportsGetCurrenciesResponseData

class RequiredExpenseReportsGetCurrenciesResponse(TypedDict):
    pass

class OptionalExpenseReportsGetCurrenciesResponse(TypedDict, total=False):
    data: ExpenseReportsGetCurrenciesResponseData

    message: str

class ExpenseReportsGetCurrenciesResponse(RequiredExpenseReportsGetCurrenciesResponse, OptionalExpenseReportsGetCurrenciesResponse):
    pass
