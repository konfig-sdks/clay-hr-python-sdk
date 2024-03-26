# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.expensereport.post import CreateNewRaw
from clay_hr_python_sdk.paths.expenseitem.post import CreateNewExpenseItemRaw
from clay_hr_python_sdk.paths.expensereport_delete.post import DeleteExpenseReportRaw
from clay_hr_python_sdk.paths.expensereports.get import GetByUserIdRaw
from clay_hr_python_sdk.paths.currencylist.get import GetCurrenciesRaw
from clay_hr_python_sdk.paths.expensetypes.get import GetExpenseTypesRaw
from clay_hr_python_sdk.paths.expensereport.get import GetReportDetailsRaw
from clay_hr_python_sdk.paths.expensereport_submit_expense_report_id.post import SubmitExpenseReportRaw


class ExpenseReportsApiRaw(
    CreateNewRaw,
    CreateNewExpenseItemRaw,
    DeleteExpenseReportRaw,
    GetByUserIdRaw,
    GetCurrenciesRaw,
    GetExpenseTypesRaw,
    GetReportDetailsRaw,
    SubmitExpenseReportRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
