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

from clay_hr_python_sdk.type.skills_get_user_assigned_skills_response_data_item_skill_model import SkillsGetUserAssignedSkillsResponseDataItemSkillModel

class RequiredSkillsGetUserAssignedSkillsResponseDataItem(TypedDict):
    pass

class OptionalSkillsGetUserAssignedSkillsResponseDataItem(TypedDict, total=False):
    description: str

    skillUserId: str

    skillId: str

    userId: str

    level: str

    cid: str

    lastUpdateUserModel: str

    createUserId: str

    status: str

    createts: str

    performancelevel: str

    candidateid: str

    weightage: str

    targetLevel: str

    targetLevelCreatets: str

    targetLevelCreateUserId: str

    skillCounsellor: str

    yearsOfExperience: str

    dateOfLastUse: str

    skillAcquireDate: str

    skillModel: SkillsGetUserAssignedSkillsResponseDataItemSkillModel

class SkillsGetUserAssignedSkillsResponseDataItem(RequiredSkillsGetUserAssignedSkillsResponseDataItem, OptionalSkillsGetUserAssignedSkillsResponseDataItem):
    pass
