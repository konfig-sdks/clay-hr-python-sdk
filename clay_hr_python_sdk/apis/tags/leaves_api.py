# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.api_userpto_balance_add.post import AddPtoBalance
from clay_hr_python_sdk.paths.api_leaverequest.post import CreateNewLeave
from clay_hr_python_sdk.paths.api_leaverequests.get import GetLeaveRequestsWithinDateRange
from clay_hr_python_sdk.paths.api_manage_leaves.get import GetLeavesBasedOnRole
from clay_hr_python_sdk.paths.api_leave_hours_credit.get import GetRemainingHoursCredit
from clay_hr_python_sdk.paths.api_process_leave.get import ProcessLeaveById
from clay_hr_python_sdk.apis.tags.leaves_api_raw import LeavesApiRaw


class LeavesApi(
    AddPtoBalance,
    CreateNewLeave,
    GetLeaveRequestsWithinDateRange,
    GetLeavesBasedOnRole,
    GetRemainingHoursCredit,
    ProcessLeaveById,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: LeavesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = LeavesApiRaw(api_client)
