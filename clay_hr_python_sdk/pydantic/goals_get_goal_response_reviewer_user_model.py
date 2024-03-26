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

from clay_hr_python_sdk.pydantic.goals_get_goal_response_reviewer_user_model_department_model import GoalsGetGoalResponseReviewerUserModelDepartmentModel
from clay_hr_python_sdk.pydantic.goals_get_goal_response_reviewer_user_model_location_model import GoalsGetGoalResponseReviewerUserModelLocationModel

class GoalsGetGoalResponseReviewerUserModel(BaseModel):
    cid: typing.Optional[str] = Field(None, alias='cid')

    emp_id: typing.Optional[str] = Field(None, alias='empId')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    position: typing.Optional[str] = Field(None, alias='position')

    first_name: typing.Optional[str] = Field(None, alias='firstName')

    short_name: typing.Optional[str] = Field(None, alias='shortName')

    last_name: typing.Optional[str] = Field(None, alias='lastName')

    display_full_name: typing.Optional[str] = Field(None, alias='displayFullName')

    user_startdate: typing.Optional[str] = Field(None, alias='userStartdate')

    email: typing.Optional[str] = Field(None, alias='email')

    cell_phone: typing.Optional[str] = Field(None, alias='cellPhone')

    user_name: typing.Optional[str] = Field(None, alias='userName')

    department_model: typing.Optional[GoalsGetGoalResponseReviewerUserModelDepartmentModel] = Field(None, alias='departmentModel')

    prefix_salutation: typing.Optional[str] = Field(None, alias='prefixSalutation')

    middle_name: typing.Optional[str] = Field(None, alias='middleName')

    family_suffix: typing.Optional[str] = Field(None, alias='familySuffix')

    status: typing.Optional[str] = Field(None, alias='status')

    ptoannual: typing.Optional[str] = Field(None, alias='ptoannual')

    ptobalance: typing.Optional[str] = Field(None, alias='ptobalance')

    worker_type: typing.Optional[str] = Field(None, alias='workerType')

    gender: typing.Optional[str] = Field(None, alias='gender')

    phone: typing.Optional[str] = Field(None, alias='phone')

    im: typing.Optional[str] = Field(None, alias='im')

    createts: typing.Optional[int] = Field(None, alias='createts')

    timezone: typing.Optional[str] = Field(None, alias='timezone')

    profile_id: typing.Optional[str] = Field(None, alias='profileId')

    allocation: typing.Optional[str] = Field(None, alias='allocation')

    lastupdateuserid: typing.Optional[str] = Field(None, alias='lastupdateuserid')

    lastupdatets: typing.Optional[str] = Field(None, alias='lastupdatets')

    userdate_format: typing.Optional[str] = Field(None, alias='userdateFormat')

    hr_portal: typing.Optional[str] = Field(None, alias='hrPortal')

    user_display_name: typing.Optional[str] = Field(None, alias='userDisplayName')

    star: typing.Optional[str] = Field(None, alias='star')

    timecard_period_pref: typing.Optional[str] = Field(None, alias='timecardPeriodPref')

    tos_version: typing.Optional[str] = Field(None, alias='tosVersion')

    guid: typing.Optional[str] = Field(None, alias='guid')

    job_grade: typing.Optional[str] = Field(None, alias='jobGrade')

    calendar_id: typing.Optional[str] = Field(None, alias='calendarId')

    working_days: typing.Optional[str] = Field(None, alias='workingDays')

    has_access: typing.Optional[str] = Field(None, alias='hasAccess')

    notifications: typing.Optional[str] = Field(None, alias='notifications')

    location_model: typing.Optional[GoalsGetGoalResponseReviewerUserModelLocationModel] = Field(None, alias='locationModel')

    is_view: typing.Optional[str] = Field(None, alias='isView')

    view: typing.Optional[str] = Field(None, alias='view')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
