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

from clay_hr_python_sdk.pydantic.pto_policy_approval_flow_model import PtoPolicyApprovalFlowModel
from clay_hr_python_sdk.pydantic.pto_policy_chain_model import PtoPolicyChainModel
from clay_hr_python_sdk.pydantic.timestamp import Timestamp

class PtoPolicyModel(BaseModel):
    pto_policy_id: int = Field(alias='ptoPolicyId')

    description: typing.Optional[str] = Field(None, alias='description')

    accrual_rate_annual: typing.Optional[typing.Union[int, float]] = Field(None, alias='accrualRateAnnual')

    accrual_rate_annual_unit: typing.Optional[typing.Union[int, float]] = Field(None, alias='accrualRateAnnualUnit')

    accrual_rate_hours: typing.Optional[typing.Union[int, float]] = Field(None, alias='accrualRateHours')

    accrual_rate_unit: typing.Optional[typing.Union[int, float]] = Field(None, alias='accrualRateUnit')

    accrual_threshold_weeks: typing.Optional[int] = Field(None, alias='accrualThresholdWeeks')

    accrual_time: typing.Optional[int] = Field(None, alias='accrualTime')

    accrual_time_span: typing.Optional[str] = Field(None, alias='accrualTimeSpan')

    accrualtype: typing.Optional[str] = Field(None, alias='accrualtype')

    allow_accrual_rate_override: typing.Optional[int] = Field(None, alias='allowAccrualRateOverride')

    allow_request_beyond_bal: typing.Optional[int] = Field(None, alias='allowRequestBeyondBal')

    applicability: typing.Optional[int] = Field(None, alias='applicability')

    bonus: typing.Optional[typing.Union[int, float]] = Field(None, alias='bonus')

    bonus_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='bonusMax')

    carryover_date: typing.Optional[date] = Field(None, alias='carryoverDate')

    carryover_expiration_quantity: typing.Optional[int] = Field(None, alias='carryoverExpirationQuantity')

    carryover_expiration_unit: typing.Optional[str] = Field(None, alias='carryoverExpirationUnit')

    cid: typing.Optional[int] = Field(None, alias='cid')

    create_user_id: typing.Optional[int] = Field(None, alias='createUserId')

    createts: typing.Optional[Timestamp] = Field(None, alias='createts')

    custom_icon: typing.Optional[str] = Field(None, alias='customIcon')

    days_definition: typing.Optional[str] = Field(None, alias='daysDefinition')

    effective_date: typing.Optional[date] = Field(None, alias='effectiveDate')

    expiration_date: typing.Optional[date] = Field(None, alias='expirationDate')

    half_day_allowed: typing.Optional[int] = Field(None, alias='halfDayAllowed')

    has_assignment: typing.Optional[bool] = Field(None, alias='hasAssignment')

    icon: typing.Optional[str] = Field(None, alias='icon')

    is_accrued: typing.Optional[str] = Field(None, alias='isAccrued')

    last_run: typing.Optional[date] = Field(None, alias='lastRun')

    leave_type: typing.Optional[str] = Field(None, alias='leaveType')

    leave_year_start: typing.Optional[str] = Field(None, alias='leaveYearStart')

    leave_year_start_date: typing.Optional[date] = Field(None, alias='leaveYearStartDate')

    next_run_date: typing.Optional[date] = Field(None, alias='nextRunDate')

    paid: typing.Optional[int] = Field(None, alias='paid')

    policy_name: typing.Optional[str] = Field(None, alias='policyName')

    policycondition: typing.Optional[str] = Field(None, alias='policycondition')

    prorated: typing.Optional[int] = Field(None, alias='prorated')

    pto_policy_approval_flow_model: typing.Optional[PtoPolicyApprovalFlowModel] = Field(None, alias='ptoPolicyApprovalFlowModel')

    pto_policy_chain_model: typing.Optional[PtoPolicyChainModel] = Field(None, alias='ptoPolicyChainModel')

    pto_policy_chain_seq_id: typing.Optional[int] = Field(None, alias='ptoPolicyChainSeqId')

    roll_over_max: typing.Optional[typing.Union[int, float]] = Field(None, alias='rollOverMax')

    roll_over_percentage: typing.Optional[typing.Union[int, float]] = Field(None, alias='rollOverPercentage')

    show_in_calendar: typing.Optional[int] = Field(None, alias='showInCalendar')

    tenure_threshold: typing.Optional[typing.Union[int, float]] = Field(None, alias='tenureThreshold')

    threshold_quantity: typing.Optional[int] = Field(None, alias='thresholdQuantity')

    threshold_unit: typing.Optional[str] = Field(None, alias='thresholdUnit')

    unit: typing.Optional[str] = Field(None, alias='unit')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
