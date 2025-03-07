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


class RequiredTimesheetsGetPreferencesByCidResponse(TypedDict):
    pass

class OptionalTimesheetsGetPreferencesByCidResponse(TypedDict, total=False):
    timesheetStartDay: str

    billablePrefValue: str

    futureTcPrefValue: str

    endDate: str

    projectAreaPrefValue: str

    complianceMsg: str

    activityTypePrefValue: str

    mobileAppClockInPrefValue: str

    allocatedProjectPrefValue: str

    addEditTcPrefValue: str

    backdatedTcReasonPrefValue: str

    timesheetPeriod: str

    categoryPrefValue: str

    startTimeEndTimeRequired: str

    workingHrsPerDay: str

    kioskAppClockInPrefValue: str

    qrCodeClockInPrefValue: str

    tcApprovalReasonPrefValue: str

    clockInOutsideGeofencePreferenceValue: str

    startDate: str

    tcRejectionReasonPrefValue: str

class TimesheetsGetPreferencesByCidResponse(RequiredTimesheetsGetPreferencesByCidResponse, OptionalTimesheetsGetPreferencesByCidResponse):
    pass
