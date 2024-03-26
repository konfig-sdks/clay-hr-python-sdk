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

from clay_hr_python_sdk.pydantic.pto_policy_approval_flow_model_pto_policy_list import PtoPolicyApprovalFlowModelPtoPolicyList
from clay_hr_python_sdk.pydantic.pto_policy_approval_model import PtoPolicyApprovalModel
from clay_hr_python_sdk.pydantic.timestamp import Timestamp

class PtoPolicyApprovalFlowModel(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    cid: typing.Optional[int] = Field(None, alias='cid')

    createts: typing.Optional[Timestamp] = Field(None, alias='createts')

    flow_id: typing.Optional[int] = Field(None, alias='flowId')

    flow_name: typing.Optional[str] = Field(None, alias='flowName')

    pto_policy_approval_model_list: typing.Optional[typing.List[PtoPolicyApprovalModel]] = Field(None, alias='ptoPolicyApprovalModelList')

    pto_policy_list: typing.Optional[PtoPolicyApprovalFlowModelPtoPolicyList] = Field(None, alias='ptoPolicyList')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
