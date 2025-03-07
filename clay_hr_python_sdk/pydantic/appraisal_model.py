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

from clay_hr_python_sdk.pydantic.assessment_model import AssessmentModel
from clay_hr_python_sdk.pydantic.user_model import UserModel
from clay_hr_python_sdk.pydantic.user_view_model import UserViewModel

class AppraisalModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    appraisal_id: typing.Optional[int] = Field(None, alias='appraisalId')

    appraisal_name: typing.Optional[str] = Field(None, alias='appraisalName')

    appraisal_type: typing.Optional[str] = Field(None, alias='appraisalType')

    candidate_position_id: typing.Optional[int] = Field(None, alias='candidatePositionId')

    cid: typing.Optional[int] = Field(None, alias='cid')

    completion_date: typing.Optional[date] = Field(None, alias='completionDate')

    create_user_id: typing.Optional[int] = Field(None, alias='createUserId')

    create_user_model: typing.Optional[UserModel] = Field(None, alias='createUserModel')

    createts: typing.Optional[date] = Field(None, alias='createts')

    end_date: typing.Optional[date] = Field(None, alias='endDate')

    final_comment: typing.Optional[str] = Field(None, alias='finalComment')

    final_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='finalValue')

    final_value_str: typing.Optional[str] = Field(None, alias='finalValueStr')

    manager_id: typing.Optional[int] = Field(None, alias='managerId')

    manager_user_model: typing.Optional[UserModel] = Field(None, alias='managerUserModel')

    obtype: typing.Optional[str] = Field(None, alias='obtype')

    pre_final_comment: typing.Optional[str] = Field(None, alias='preFinalComment')

    pre_final_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='preFinalValue')

    pre_final_value_str: typing.Optional[str] = Field(None, alias='preFinalValueStr')

    review_mode: typing.Optional[str] = Field(None, alias='reviewMode')

    save_for_later: typing.Optional[int] = Field(None, alias='saveForLater')

    score_template_id: typing.Optional[int] = Field(None, alias='scoreTemplateId')

    score_template_model: typing.Optional[AssessmentModel] = Field(None, alias='scoreTemplateModel')

    show_final_value: typing.Optional[int] = Field(None, alias='showFinalValue')

    show_weighted_total: typing.Optional[int] = Field(None, alias='showWeightedTotal')

    start_date: typing.Optional[date] = Field(None, alias='startDate')

    status: typing.Optional[str] = Field(None, alias='status')

    status_code: typing.Optional[str] = Field(None, alias='statusCode')

    user_id: typing.Optional[int] = Field(None, alias='userId')

    user_model: typing.Optional[UserModel] = Field(None, alias='userModel')

    user_view_model: typing.Optional[UserViewModel] = Field(None, alias='userViewModel')

    workflow_id: typing.Optional[int] = Field(None, alias='workflowId')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
