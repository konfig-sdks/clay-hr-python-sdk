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

from clay_hr_python_sdk.type.appraisal_model import AppraisalModel
from clay_hr_python_sdk.type.attachment_model import AttachmentModel
from clay_hr_python_sdk.type.dyna_form_slim_model import DynaFormSlimModel
from clay_hr_python_sdk.type.mail_template_model import MailTemplateModel
from clay_hr_python_sdk.type.position_status_model import PositionStatusModel
from clay_hr_python_sdk.type.training_model import TrainingModel
from clay_hr_python_sdk.type.user_group_model import UserGroupModel
from clay_hr_python_sdk.type.user_model import UserModel
from clay_hr_python_sdk.type.workflow_parameter_model import WorkflowParameterModel
from clay_hr_python_sdk.type.workflow_step_model import WorkflowStepModel

class RequiredWorkflowStepModel(TypedDict):
    pass

class OptionalWorkflowStepModel(TypedDict, total=False):
    appraisalModel: AppraisalModel

    assignee: str

    assigneeModel: UserModel

    attachmentModel: AttachmentModel

    cid: int

    createUserId: int

    dependentStepId: int

    dependentStepModel: "WorkflowStepModel"

    dueDate: str

    dynamicFormModel: DynaFormSlimModel

    fieldToChange: str

    fromPositionStatusModel: PositionStatusModel

    mailTemplateModel: MailTemplateModel

    phaseId: int

    relativeTo: str

    reqApproval: bool

    sequence: int

    stepDesc: str

    stepId: int

    stepName: str

    stepType: str

    toPositionStatusModel: PositionStatusModel

    trainingModel: TrainingModel

    transitionName: str

    userGroupModel: UserGroupModel

    workflowParameterModel: WorkflowParameterModel

class WorkflowStepModel(RequiredWorkflowStepModel, OptionalWorkflowStepModel):
    pass
