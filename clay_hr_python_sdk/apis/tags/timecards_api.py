# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.timecard_clock_out.get import ClockOut
from clay_hr_python_sdk.paths.timecard_clockin.post import CreatePastTimecard
from clay_hr_python_sdk.paths.timecard_addtimecard.post import CreateTimecard
from clay_hr_python_sdk.paths.api_user_timecard.get import GetByUserId
from clay_hr_python_sdk.paths.api_user_timecards.get import GetByUserId0
from clay_hr_python_sdk.paths.api_timecards_details_timecard_id.get import GetDetailsByTimecardId
from clay_hr_python_sdk.paths.verify_tvc.get import GetTvcForClockinWithQrCodeUsingCid
from clay_hr_python_sdk.paths.timecard.get import GetUserById
from clay_hr_python_sdk.paths.register.post import RegisterDeviceForClockInWithAssetModel
from clay_hr_python_sdk.paths.verify_device.get import VerifyDeviceWithDeviceUuid
from clay_hr_python_sdk.paths.verify_user.get import VerifyUserWithUserid
from clay_hr_python_sdk.apis.tags.timecards_api_raw import TimecardsApiRaw


class TimecardsApi(
    ClockOut,
    CreatePastTimecard,
    CreateTimecard,
    GetByUserId,
    GetByUserId0,
    GetDetailsByTimecardId,
    GetTvcForClockinWithQrCodeUsingCid,
    GetUserById,
    RegisterDeviceForClockInWithAssetModel,
    VerifyDeviceWithDeviceUuid,
    VerifyUserWithUserid,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: TimecardsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = TimecardsApiRaw(api_client)
