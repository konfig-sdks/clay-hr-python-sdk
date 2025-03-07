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

from clay_hr_python_sdk.type.address_model import AddressModel
from clay_hr_python_sdk.type.assessment_model import AssessmentModel
from clay_hr_python_sdk.type.attachment_model import AttachmentModel
from clay_hr_python_sdk.type.candidate_applications_model import CandidateApplicationsModel
from clay_hr_python_sdk.type.candidate_status_model import CandidateStatusModel
from clay_hr_python_sdk.type.certification_model import CertificationModel
from clay_hr_python_sdk.type.custom_field_value_model import CustomFieldValueModel
from clay_hr_python_sdk.type.education_model import EducationModel
from clay_hr_python_sdk.type.employment_model import EmploymentModel
if TYPE_CHECKING:
    from clay_hr_python_sdk.type.position_model import PositionModel
from clay_hr_python_sdk.type.skill_user_model import SkillUserModel
from clay_hr_python_sdk.type.timestamp import Timestamp
from clay_hr_python_sdk.type.workflow_model import WorkflowModel

class RequiredCandidateModel(TypedDict):
    pass

class OptionalCandidateModel(TypedDict, total=False):
    acceptance1: bool

    acceptance2: bool

    accessCode: str

    addressModelList: typing.List[AddressModel]

    assessmentModel: AssessmentModel

    attachmentModelList: 'typing.List[AttachmentModel]'

    candidateLock: int

    candidatePositionsModelList: typing.List[CandidateApplicationsModel]

    candidateStatusModel: CandidateStatusModel

    certificationModelList: typing.List[CertificationModel]

    cid: int

    cloudSearchSync: int

    createts: Timestamp

    createuserid: int

    customFieldValueModelList: typing.List[CustomFieldValueModel]

    customfieldvalue: typing.List[CustomFieldValueModel]

    dateOfBirth: date

    educationModelList: typing.List[EducationModel]

    educationStr: str

    email: str

    employmentModelList: typing.List[EmploymentModel]

    isInternalCand: bool

    isNewCand: bool

    languagePreference: str

    lastupdateuserid: int

    name: str

    notes: str

    passwordHash: str

    phone: str

    positionModel: 'PositionModel'

    positionName: str

    recruitId: int

    recruiter: str

    recruiterUserId: int

    referrer: str

    referrerId: int

    salaryAmount: int

    salaryCurrencyCode: str

    score: typing.Union[int, float]

    skillModelList: 'typing.List[SkillUserModel]'

    source: str

    status: str

    statusid: int

    summaryByCandidate: str

    systemReco: str

    systemRecoHelp: str

    templateId: int

    timezone: str

    trainingAccess: bool

    updatedOn: Timestamp

    userId: int

    verificationCode: int

    verified: str

    workflowId: int

    workflowModel: WorkflowModel

    workflowName: str

class CandidateModel(RequiredCandidateModel, OptionalCandidateModel):
    pass
