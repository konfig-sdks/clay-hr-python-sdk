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

from clay_hr_python_sdk.type.skill_model import SkillModel
from clay_hr_python_sdk.type.timestamp import Timestamp
if TYPE_CHECKING:
    from clay_hr_python_sdk.type.user_model import UserModel

class RequiredSkillUserModel(TypedDict):
    pass

class OptionalSkillUserModel(TypedDict, total=False):
    description: str

    candidateid: int

    cid: int

    createUserId: int

    createts: Timestamp

    dateOfLastUse: date

    lastUpdateUserModel: 'UserModel'

    level: typing.Union[int, float]

    performancelevel: typing.Union[int, float]

    skillAcquireDate: date

    skillCounsellor: bool

    skillId: int

    skillModel: SkillModel

    skillUserId: int

    status: str

    targetLevel: typing.Union[int, float]

    targetLevelCreateUserId: int

    targetLevelCreatets: Timestamp

    userId: int

    weightage: typing.Union[int, float]

    yearsOfExperience: int

class SkillUserModel(RequiredSkillUserModel, OptionalSkillUserModel):
    pass
