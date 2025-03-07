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

from clay_hr_python_sdk.type.timestamp import Timestamp

class RequiredWorkflowParameterModel(TypedDict):
    pass

class OptionalWorkflowParameterModel(TypedDict, total=False):
    cid: int

    createts: Timestamp

    paramName: str

    paramType: str

    workflowArgId: int

    workflowId: int

class WorkflowParameterModel(RequiredWorkflowParameterModel, OptionalWorkflowParameterModel):
    pass
