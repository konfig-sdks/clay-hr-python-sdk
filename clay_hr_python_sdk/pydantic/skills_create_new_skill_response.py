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

from clay_hr_python_sdk.pydantic.skills_create_new_skill_response_assessment_model import SkillsCreateNewSkillResponseAssessmentModel
from clay_hr_python_sdk.pydantic.skills_create_new_skill_response_skill_type_model import SkillsCreateNewSkillResponseSkillTypeModel

class SkillsCreateNewSkillResponse(BaseModel):
    status: typing.Optional[str] = Field(None, alias='Status')

    description: typing.Optional[str] = Field(None, alias='Description')

    skill_code: typing.Optional[str] = Field(None, alias='SkillCode')

    skill_type_model: typing.Optional[SkillsCreateNewSkillResponseSkillTypeModel] = Field(None, alias='SkillTypeModel')

    assessment_model: typing.Optional[SkillsCreateNewSkillResponseAssessmentModel] = Field(None, alias='AssessmentModel')

    skill_id: typing.Optional[str] = Field(None, alias='SkillId')

    message: typing.Optional[str] = Field(None, alias='message')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
