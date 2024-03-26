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

from clay_hr_python_sdk.pydantic.skills_get_user_assigned_skills_response_data_item_skill_model_assessment_model import SkillsGetUserAssignedSkillsResponseDataItemSkillModelAssessmentModel

class SkillsGetUserAssignedSkillsResponseDataItemSkillModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    skill_id: typing.Optional[str] = Field(None, alias='skillId')

    skill_code: typing.Optional[str] = Field(None, alias='skillCode')

    cid: typing.Optional[str] = Field(None, alias='cid')

    skill_type_model: typing.Optional[str] = Field(None, alias='skillTypeModel')

    assessment_model: typing.Optional[SkillsGetUserAssignedSkillsResponseDataItemSkillModelAssessmentModel] = Field(None, alias='assessmentModel')

    sequence: typing.Optional[str] = Field(None, alias='sequence')

    skill_type_name: typing.Optional[str] = Field(None, alias='skillTypeName')

    user_skill_level: typing.Optional[str] = Field(None, alias='userSkillLevel')

    status: typing.Optional[str] = Field(None, alias='status')

    create_user_id: typing.Optional[str] = Field(None, alias='createUserId')

    createts: typing.Optional[str] = Field(None, alias='createts')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
