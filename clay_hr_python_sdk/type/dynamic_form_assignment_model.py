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

from clay_hr_python_sdk.type.candidate_model import CandidateModel
from clay_hr_python_sdk.type.dyna_form_section_assignment_model import DynaFormSectionAssignmentModel
from clay_hr_python_sdk.type.dyna_form_slim_model import DynaFormSlimModel
from clay_hr_python_sdk.type.timestamp import Timestamp
from clay_hr_python_sdk.type.user_model import UserModel
from clay_hr_python_sdk.type.user_view_model import UserViewModel

class RequiredDynamicFormAssignmentModel(TypedDict):
    pass

class OptionalDynamicFormAssignmentModel(TypedDict, total=False):
    allowGrader: bool

    assessmentScore: typing.Union[int, float]

    assignCandidateModel: CandidateModel

    assignUserModel: UserModel

    assignUserViewModel: UserViewModel

    assignmentId: int

    cid: int

    createUserModel: UserModel

    createUserViewModel: UserViewModel

    createts: Timestamp

    dueDate: date

    dynaFormModel: DynaFormSlimModel

    dynaFormSectionAssignmentModel: 'typing.List[DynaFormSectionAssignmentModel]'

    formSummary: str

    graderUserModel: UserModel

    lastupdatets: Timestamp

    optedOutForEmail: bool

    status: str

    testEndts: Timestamp

    testResult: str

    testStartts: Timestamp

    testTimeStatus: str

class DynamicFormAssignmentModel(RequiredDynamicFormAssignmentModel, OptionalDynamicFormAssignmentModel):
    pass
