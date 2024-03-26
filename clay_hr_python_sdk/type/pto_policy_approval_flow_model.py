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

from clay_hr_python_sdk.type.pto_policy_approval_flow_model_pto_policy_list import PtoPolicyApprovalFlowModelPtoPolicyList
from clay_hr_python_sdk.type.pto_policy_approval_model import PtoPolicyApprovalModel
from clay_hr_python_sdk.type.timestamp import Timestamp

class RequiredPtoPolicyApprovalFlowModel(TypedDict):
    pass

class OptionalPtoPolicyApprovalFlowModel(TypedDict, total=False):
    description: str

    cid: int

    createts: Timestamp

    flowId: int

    flowName: str

    ptoPolicyApprovalModelList: typing.List[PtoPolicyApprovalModel]

    ptoPolicyList: PtoPolicyApprovalFlowModelPtoPolicyList

class PtoPolicyApprovalFlowModel(RequiredPtoPolicyApprovalFlowModel, OptionalPtoPolicyApprovalFlowModel):
    pass
