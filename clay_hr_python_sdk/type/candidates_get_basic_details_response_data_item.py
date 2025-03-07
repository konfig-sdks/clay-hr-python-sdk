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


class RequiredCandidatesGetBasicDetailsResponseDataItem(TypedDict):
    pass

class OptionalCandidatesGetBasicDetailsResponseDataItem(TypedDict, total=False):
    recruitId: str

    name: str

    email: str

    phone: str

    dateOfBirth: str

    statusid: str

    referrerId: str

    createts: str

    notes: str

    source: str

    userid: str

    recruiterUserId: str

    summaryByCandidate: str

    candidateLock: str

    educationStr: str

    status: str

    appliedPositions: str

    updatedOn: str

    cid: str

    tagIds: str

    statusColor: str

    appliedPositionIds: str

    appliedPositionUids: str

    recruiterThumbnail: str

    recruiterName: str

    recruiterGender: str

    referrerName: str

    isInternalCand: str

    applicationStatus: str

    verified: str

    positionNameList: str

    internalCandidate: str

class CandidatesGetBasicDetailsResponseDataItem(RequiredCandidatesGetBasicDetailsResponseDataItem, OptionalCandidatesGetBasicDetailsResponseDataItem):
    pass
