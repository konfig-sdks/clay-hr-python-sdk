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


class CandidatesGetBasicDetailsResponseDataItem(BaseModel):
    recruit_id: typing.Optional[str] = Field(None, alias='recruitId')

    name: typing.Optional[str] = Field(None, alias='name')

    email: typing.Optional[str] = Field(None, alias='email')

    phone: typing.Optional[str] = Field(None, alias='phone')

    date_of_birth: typing.Optional[str] = Field(None, alias='dateOfBirth')

    statusid: typing.Optional[str] = Field(None, alias='statusid')

    referrer_id: typing.Optional[str] = Field(None, alias='referrerId')

    createts: typing.Optional[str] = Field(None, alias='createts')

    notes: typing.Optional[str] = Field(None, alias='notes')

    source: typing.Optional[str] = Field(None, alias='source')

    userid: typing.Optional[str] = Field(None, alias='userid')

    recruiter_user_id: typing.Optional[str] = Field(None, alias='recruiterUserId')

    summary_by_candidate: typing.Optional[str] = Field(None, alias='summaryByCandidate')

    candidate_lock: typing.Optional[str] = Field(None, alias='candidateLock')

    education_str: typing.Optional[str] = Field(None, alias='educationStr')

    status: typing.Optional[str] = Field(None, alias='status')

    applied_positions: typing.Optional[str] = Field(None, alias='appliedPositions')

    updated_on: typing.Optional[str] = Field(None, alias='updatedOn')

    cid: typing.Optional[str] = Field(None, alias='cid')

    tag_ids: typing.Optional[str] = Field(None, alias='tagIds')

    status_color: typing.Optional[str] = Field(None, alias='statusColor')

    applied_position_ids: typing.Optional[str] = Field(None, alias='appliedPositionIds')

    applied_position_uids: typing.Optional[str] = Field(None, alias='appliedPositionUids')

    recruiter_thumbnail: typing.Optional[str] = Field(None, alias='recruiterThumbnail')

    recruiter_name: typing.Optional[str] = Field(None, alias='recruiterName')

    recruiter_gender: typing.Optional[str] = Field(None, alias='recruiterGender')

    referrer_name: typing.Optional[str] = Field(None, alias='referrerName')

    is_internal_cand: typing.Optional[str] = Field(None, alias='isInternalCand')

    application_status: typing.Optional[str] = Field(None, alias='applicationStatus')

    verified: typing.Optional[str] = Field(None, alias='verified')

    position_name_list: typing.Optional[str] = Field(None, alias='positionNameList')

    internal_candidate: typing.Optional[str] = Field(None, alias='internalCandidate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
