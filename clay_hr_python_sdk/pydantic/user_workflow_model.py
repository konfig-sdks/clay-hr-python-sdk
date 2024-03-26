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

from clay_hr_python_sdk.pydantic.candidate_model import CandidateModel
from clay_hr_python_sdk.pydantic.position_model import PositionModel
from clay_hr_python_sdk.pydantic.timestamp import Timestamp
from clay_hr_python_sdk.pydantic.user_model import UserModel
from clay_hr_python_sdk.pydantic.user_view_model import UserViewModel
from clay_hr_python_sdk.pydantic.workflow_model import WorkflowModel

class UserWorkflowModel(BaseModel):
    assign_candidate_model: typing.Optional[CandidateModel] = Field(None, alias='assignCandidateModel')

    assign_position_model: typing.Optional[PositionModel] = Field(None, alias='assignPositionModel')

    assign_user_model: typing.Optional[UserModel] = Field(None, alias='assignUserModel')

    cid: typing.Optional[int] = Field(None, alias='cid')

    coordinator_user_view_model: typing.Optional[UserViewModel] = Field(None, alias='coordinatorUserViewModel')

    create_t_s: typing.Optional[Timestamp] = Field(None, alias='createTS')

    create_user_model: typing.Optional[UserModel] = Field(None, alias='createUserModel')

    launch_status: typing.Optional[str] = Field(None, alias='launchStatus')

    launchts: typing.Optional[Timestamp] = Field(None, alias='launchts')

    opted_out_for_email: typing.Optional[bool] = Field(None, alias='optedOutForEmail')

    status_code: typing.Optional[str] = Field(None, alias='statusCode')

    user_workflow_id: typing.Optional[int] = Field(None, alias='userWorkflowId')

    workflow_model: typing.Optional[WorkflowModel] = Field(None, alias='workflowModel')

    workflow_progress: typing.Optional[typing.Union[int, float]] = Field(None, alias='workflowProgress')

    workflow_status: typing.Optional[str] = Field(None, alias='workflowStatus')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
