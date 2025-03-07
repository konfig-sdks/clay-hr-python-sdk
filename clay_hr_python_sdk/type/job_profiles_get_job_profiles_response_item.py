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


class RequiredJobProfilesGetJobProfilesResponseItem(TypedDict):
    pass

class OptionalJobProfilesGetJobProfilesResponseItem(TypedDict, total=False):
    cid: str

    profileId: str

    profileName: str

    profileDescription: str

    orgId: str

    profileResponsibilities: str

    profileRequirements: str

    salaryBandMin: str

    salaryBandMax: str

    salaryBandCurrency: str

    managerProfileId: str

    managerProfileName: str

    customFieldValueModelList: str

    numberofUsers: str

    createuserid: str

    status: str

    careerPathwayModelList: str

    objectType: str

    objectName: str

    objectid: str

class JobProfilesGetJobProfilesResponseItem(RequiredJobProfilesGetJobProfilesResponseItem, OptionalJobProfilesGetJobProfilesResponseItem):
    pass
