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

from clay_hr_python_sdk.type.skills_create_new_skill_request_assessment_model import SkillsCreateNewSkillRequestAssessmentModel
from clay_hr_python_sdk.type.skills_create_new_skill_request_skill_type_model import SkillsCreateNewSkillRequestSkillTypeModel

class RequiredSkillsCreateNewSkillRequest(TypedDict):
    # Description of the skill.
    description: str

    # The title of the skill.
    skillCode: str

class OptionalSkillsCreateNewSkillRequest(TypedDict, total=False):
    assessmentModel: SkillsCreateNewSkillRequestAssessmentModel

    skillTypeModel: SkillsCreateNewSkillRequestSkillTypeModel

class SkillsCreateNewSkillRequest(RequiredSkillsCreateNewSkillRequest, OptionalSkillsCreateNewSkillRequest):
    pass
