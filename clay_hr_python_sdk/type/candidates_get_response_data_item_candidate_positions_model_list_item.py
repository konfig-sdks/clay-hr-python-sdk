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


class RequiredCandidatesGetResponseDataItemCandidatePositionsModelListItem(TypedDict):
    pass

class OptionalCandidatesGetResponseDataItemCandidatePositionsModelListItem(TypedDict, total=False):
    candidatePositionsId: str

    candidateId: str

    positionid: str

    positionName: str

    positionDescription: str

    responsibilities: str

    positionDepartmentId: str

    positionLocationId: str

    positionProjectId: str

    positionProfileId: str

    count: str

    positioncreatets: str

    positionStatusOpenClosed: str

    applicationDueDate: str

    applicationStatusId: str

    applicationStatusValue: str

    sequence: str

    colorcode: str

    systemReco: str

    systemRecoHelp: str

    candidatePositionCreateTs: str

    cid: str

    appliedPositions: str

    status: str

class CandidatesGetResponseDataItemCandidatePositionsModelListItem(RequiredCandidatesGetResponseDataItemCandidatePositionsModelListItem, OptionalCandidatesGetResponseDataItemCandidatePositionsModelListItem):
    pass
