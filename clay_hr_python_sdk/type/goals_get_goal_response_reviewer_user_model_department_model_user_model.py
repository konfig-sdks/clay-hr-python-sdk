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


class RequiredGoalsGetGoalResponseReviewerUserModelDepartmentModelUserModel(TypedDict):
    pass

class OptionalGoalsGetGoalResponseReviewerUserModelDepartmentModelUserModel(TypedDict, total=False):
    userId: str

    firstName: str

    lastName: str

    name: str

    phone: str

    email: str

    status: str

    shortName: str

    thumbnail: str

    gender: str

    jobTitle: str

    departmentId: str

    locationId: str

    department: str

    location: str

    profileId: str

    profileName: str

    timezone: str

    userStartdate: str

    userEnddate: str

    cellPhone: str

    empId: str

    userdateOfBirth: str

    allocation: str

    userdateFormat: str

    star: str

    imageName: str

    notes: str

    im: str

    createuserid: str

    countryId: str

    cid: str

    guid: str

    hasAccess: str

    displayName: str

    id: str

class GoalsGetGoalResponseReviewerUserModelDepartmentModelUserModel(RequiredGoalsGetGoalResponseReviewerUserModelDepartmentModelUserModel, OptionalGoalsGetGoalResponseReviewerUserModelDepartmentModelUserModel):
    pass
