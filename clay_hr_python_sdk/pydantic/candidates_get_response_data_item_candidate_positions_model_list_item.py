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


class CandidatesGetResponseDataItemCandidatePositionsModelListItem(BaseModel):
    candidate_positions_id: typing.Optional[str] = Field(None, alias='candidatePositionsId')

    candidate_id: typing.Optional[str] = Field(None, alias='candidateId')

    positionid: typing.Optional[str] = Field(None, alias='positionid')

    position_name: typing.Optional[str] = Field(None, alias='positionName')

    position_description: typing.Optional[str] = Field(None, alias='positionDescription')

    responsibilities: typing.Optional[str] = Field(None, alias='responsibilities')

    position_department_id: typing.Optional[str] = Field(None, alias='positionDepartmentId')

    position_location_id: typing.Optional[str] = Field(None, alias='positionLocationId')

    position_project_id: typing.Optional[str] = Field(None, alias='positionProjectId')

    position_profile_id: typing.Optional[str] = Field(None, alias='positionProfileId')

    count: typing.Optional[str] = Field(None, alias='count')

    positioncreatets: typing.Optional[str] = Field(None, alias='positioncreatets')

    position_status_open_closed: typing.Optional[str] = Field(None, alias='positionStatusOpenClosed')

    application_due_date: typing.Optional[str] = Field(None, alias='applicationDueDate')

    application_status_id: typing.Optional[str] = Field(None, alias='applicationStatusId')

    application_status_value: typing.Optional[str] = Field(None, alias='applicationStatusValue')

    sequence: typing.Optional[str] = Field(None, alias='sequence')

    colorcode: typing.Optional[str] = Field(None, alias='colorcode')

    system_reco: typing.Optional[str] = Field(None, alias='systemReco')

    system_reco_help: typing.Optional[str] = Field(None, alias='systemRecoHelp')

    candidate_position_create_ts: typing.Optional[str] = Field(None, alias='candidatePositionCreateTs')

    cid: typing.Optional[str] = Field(None, alias='cid')

    applied_positions: typing.Optional[str] = Field(None, alias='appliedPositions')

    status: typing.Optional[str] = Field(None, alias='status')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
