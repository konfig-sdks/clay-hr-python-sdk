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

from clay_hr_python_sdk.pydantic.timestamp import Timestamp

class CertificationModel(BaseModel):
    certification_number: typing.Optional[str] = Field(None, alias='CertificationNumber')

    authority: typing.Optional[str] = Field(None, alias='authority')

    candidate_id: typing.Optional[int] = Field(None, alias='candidateId')

    certification_id: typing.Optional[int] = Field(None, alias='certificationId')

    certification_number: typing.Optional[str] = Field(None, alias='certificationNumber')

    cid: typing.Optional[int] = Field(None, alias='cid')

    comments: typing.Optional[str] = Field(None, alias='comments')

    create_user_id: typing.Optional[int] = Field(None, alias='createUserId')

    createts: typing.Optional[Timestamp] = Field(None, alias='createts')

    expire_date: typing.Optional[date] = Field(None, alias='expireDate')

    issue_date: typing.Optional[date] = Field(None, alias='issueDate')

    issue_state: typing.Optional[str] = Field(None, alias='issueState')

    type: typing.Optional[str] = Field(None, alias='type')

    user_id: typing.Optional[int] = Field(None, alias='userId')

    valid_state: typing.Optional[str] = Field(None, alias='validState')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
