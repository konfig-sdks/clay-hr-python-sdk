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

from clay_hr_python_sdk.type.goals_get_goal_response_assigned_user_model_department_model import GoalsGetGoalResponseAssignedUserModelDepartmentModel
from clay_hr_python_sdk.type.goals_get_goal_response_assigned_user_model_location_model import GoalsGetGoalResponseAssignedUserModelLocationModel
from clay_hr_python_sdk.type.goals_get_goal_response_assigned_user_model_user_profile_model import GoalsGetGoalResponseAssignedUserModelUserProfileModel

class RequiredGoalsGetGoalResponseAssignedUserModel(TypedDict):
    pass

class OptionalGoalsGetGoalResponseAssignedUserModel(TypedDict, total=False):
    cid: str

    empId: str

    userId: str

    position: str

    firstName: str

    shortName: str

    lastName: str

    displayFullName: str

    userStartdate: str

    userEnddate: str

    email: str

    cellPhone: str

    userName: str

    userProfileModel: GoalsGetGoalResponseAssignedUserModelUserProfileModel

    departmentModel: GoalsGetGoalResponseAssignedUserModelDepartmentModel

    prefixSalutation: str

    secondLastName: str

    middleName: str

    namePronunciation: str

    familySuffix: str

    status: str

    ptoannual: str

    ptobalance: str

    gender: str

    phone: str

    im: str

    createts: int

    timezone: str

    practiceId: str

    imageName: str

    thumbnail: str

    profileId: str

    allocation: str

    countryId: str

    lastupdateuserid: str

    lastupdatets: str

    workingDaysSchedule: str

    userdateFormat: str

    hrPortal: str

    userDisplayName: str

    star: str

    timecardPeriodPref: str

    languagePreference: str

    tosVersion: str

    guid: str

    jobGrade: str

    paId: str

    workingDays: str

    hasAccess: str

    notifications: str

    locationModel: GoalsGetGoalResponseAssignedUserModelLocationModel

    isView: str

    view: str

class GoalsGetGoalResponseAssignedUserModel(RequiredGoalsGetGoalResponseAssignedUserModel, OptionalGoalsGetGoalResponseAssignedUserModel):
    pass
