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

from clay_hr_python_sdk.pydantic.appraisal_model import AppraisalModel
from clay_hr_python_sdk.pydantic.attachment_model import AttachmentModel
from clay_hr_python_sdk.pydantic.dyna_form_slim_model import DynaFormSlimModel
from clay_hr_python_sdk.pydantic.mail_template_model import MailTemplateModel
from clay_hr_python_sdk.pydantic.position_status_model import PositionStatusModel
from clay_hr_python_sdk.pydantic.training_model import TrainingModel
from clay_hr_python_sdk.pydantic.user_group_model import UserGroupModel
from clay_hr_python_sdk.pydantic.user_model import UserModel
from clay_hr_python_sdk.pydantic.workflow_parameter_model import WorkflowParameterModel
from clay_hr_python_sdk.pydantic.workflow_step_model import WorkflowStepModel

class WorkflowStepModel(BaseModel):
    appraisal_model: typing.Optional[AppraisalModel] = Field(None, alias='appraisalModel')

    assignee: typing.Optional[str] = Field(None, alias='assignee')

    assignee_model: typing.Optional[UserModel] = Field(None, alias='assigneeModel')

    attachment_model: typing.Optional[AttachmentModel] = Field(None, alias='attachmentModel')

    cid: typing.Optional[int] = Field(None, alias='cid')

    create_user_id: typing.Optional[int] = Field(None, alias='createUserId')

    dependent_step_id: typing.Optional[int] = Field(None, alias='dependentStepId')

    dependent_step_model: typing.Optional["WorkflowStepModel"] = Field(None, alias='dependentStepModel')

    due_date: typing.Optional[str] = Field(None, alias='dueDate')

    dynamic_form_model: typing.Optional[DynaFormSlimModel] = Field(None, alias='dynamicFormModel')

    field_to_change: typing.Optional[str] = Field(None, alias='fieldToChange')

    from_position_status_model: typing.Optional[PositionStatusModel] = Field(None, alias='fromPositionStatusModel')

    mail_template_model: typing.Optional[MailTemplateModel] = Field(None, alias='mailTemplateModel')

    phase_id: typing.Optional[int] = Field(None, alias='phaseId')

    relative_to: typing.Optional[str] = Field(None, alias='relativeTo')

    req_approval: typing.Optional[bool] = Field(None, alias='reqApproval')

    sequence: typing.Optional[int] = Field(None, alias='sequence')

    step_desc: typing.Optional[str] = Field(None, alias='stepDesc')

    step_id: typing.Optional[int] = Field(None, alias='stepId')

    step_name: typing.Optional[str] = Field(None, alias='stepName')

    step_type: typing.Optional[str] = Field(None, alias='stepType')

    to_position_status_model: typing.Optional[PositionStatusModel] = Field(None, alias='toPositionStatusModel')

    training_model: typing.Optional[TrainingModel] = Field(None, alias='trainingModel')

    transition_name: typing.Optional[str] = Field(None, alias='transitionName')

    user_group_model: typing.Optional[UserGroupModel] = Field(None, alias='userGroupModel')

    workflow_parameter_model: typing.Optional[WorkflowParameterModel] = Field(None, alias='workflowParameterModel')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
