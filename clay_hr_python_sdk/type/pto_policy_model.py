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

from clay_hr_python_sdk.type.pto_policy_approval_flow_model import PtoPolicyApprovalFlowModel
from clay_hr_python_sdk.type.pto_policy_chain_model import PtoPolicyChainModel
from clay_hr_python_sdk.type.timestamp import Timestamp

class RequiredPtoPolicyModel(TypedDict):
    ptoPolicyId: int

class OptionalPtoPolicyModel(TypedDict, total=False):
    description: str

    accrualRateAnnual: typing.Union[int, float]

    accrualRateAnnualUnit: typing.Union[int, float]

    accrualRateHours: typing.Union[int, float]

    accrualRateUnit: typing.Union[int, float]

    accrualThresholdWeeks: int

    accrualTime: int

    accrualTimeSpan: str

    accrualtype: str

    allowAccrualRateOverride: int

    allowRequestBeyondBal: int

    applicability: int

    bonus: typing.Union[int, float]

    bonusMax: typing.Union[int, float]

    carryoverDate: date

    carryoverExpirationQuantity: int

    carryoverExpirationUnit: str

    cid: int

    createUserId: int

    createts: Timestamp

    customIcon: str

    daysDefinition: str

    effectiveDate: date

    expirationDate: date

    halfDayAllowed: int

    hasAssignment: bool

    icon: str

    isAccrued: str

    lastRun: date

    leaveType: str

    leaveYearStart: str

    leaveYearStartDate: date

    nextRunDate: date

    paid: int

    policyName: str

    policycondition: str

    prorated: int

    ptoPolicyApprovalFlowModel: PtoPolicyApprovalFlowModel

    ptoPolicyChainModel: PtoPolicyChainModel

    ptoPolicyChainSeqId: int

    rollOverMax: typing.Union[int, float]

    rollOverPercentage: typing.Union[int, float]

    showInCalendar: int

    tenureThreshold: typing.Union[int, float]

    thresholdQuantity: int

    thresholdUnit: str

    unit: str

class PtoPolicyModel(RequiredPtoPolicyModel, OptionalPtoPolicyModel):
    pass
