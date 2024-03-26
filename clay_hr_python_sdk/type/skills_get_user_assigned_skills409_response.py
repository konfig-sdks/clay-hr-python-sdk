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


class RequiredSkillsGetUserAssignedSkills409Response(TypedDict):
    pass

class OptionalSkillsGetUserAssignedSkills409Response(TypedDict, total=False):
    message: str

class SkillsGetUserAssignedSkills409Response(RequiredSkillsGetUserAssignedSkills409Response, OptionalSkillsGetUserAssignedSkills409Response):
    pass
