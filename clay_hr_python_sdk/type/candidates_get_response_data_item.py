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

from clay_hr_python_sdk.type.candidates_get_response_data_item_candidate_positions_model_list import CandidatesGetResponseDataItemCandidatePositionsModelList

class RequiredCandidatesGetResponseDataItem(TypedDict):
    pass

class OptionalCandidatesGetResponseDataItem(TypedDict, total=False):
    recruitId: str

    name: str

    referrerId: str

    referrer: str

    recruiter: str

    score: str

    updatedOn: str

    status: str

    notes: str

    dateOfBirth: str

    joiningDate: str

    cid: str

    email: str

    phone: str

    createts: str

    templateId: str

    recruiterUserId: str

    workflowId: str

    statusid: str

    workflowModel: str

    candidateStatusModel: str

    assessmentModel: str

    workflowName: str

    employmentModelList: str

    educationModelList: str

    customFieldValueModelList: str

    addressModelList: str

    skillModelList: str

    positionName: str

    candidatePositionsModelList: CandidatesGetResponseDataItemCandidatePositionsModelList

    createuserid: str

    lastupdateuserid: str

    accessCode: str

    source: str

    passwordHash: str

    acceptance1: str

    acceptance2: str

    summaryByCandidate: str

    systemReco: str

    systemRecoHelp: str

    candidateLock: str

    salaryCurrencyCode: str

    salaryAmount: str

    educationStr: str

    languagePreference: str

    userId: str

    verified: str

    verificationCode: str

    isInternalCand: str

    isNewCand: str

    timezone: str

    trainingAccess: str

    customfieldvalue: str

    cloudSearchSync: str

    jobBoardAccess: str

    bgScreeningOrderGuid: str

    bgScreeningOrderCreateDate: str

    checkrCandidateId: str

    positionModel: str

    certificationModelList: str

    attachmentModelList: str

class CandidatesGetResponseDataItem(RequiredCandidatesGetResponseDataItem, OptionalCandidatesGetResponseDataItem):
    pass
