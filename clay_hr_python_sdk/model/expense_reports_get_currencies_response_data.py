# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clay_hr_python_sdk import schemas  # noqa: F401


class ExpenseReportsGetCurrenciesResponseData(
    schemas.ListSchema
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['ExpenseReportsGetCurrenciesResponseDataItem']:
            return ExpenseReportsGetCurrenciesResponseDataItem

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple['ExpenseReportsGetCurrenciesResponseDataItem'], typing.List['ExpenseReportsGetCurrenciesResponseDataItem']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ExpenseReportsGetCurrenciesResponseData':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'ExpenseReportsGetCurrenciesResponseDataItem':
        return super().__getitem__(i)

from clay_hr_python_sdk.model.expense_reports_get_currencies_response_data_item import ExpenseReportsGetCurrenciesResponseDataItem
