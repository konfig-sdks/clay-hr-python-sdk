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

from clay_hr_python_sdk.type.feedback_list_feedback_response_feedback_list_item_assigned_user_model_location_model_address_model_list import FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelList

class RequiredFeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel(TypedDict):
    pass

class OptionalFeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel(TypedDict, total=False):
    locationId: str

    locationName: str

    cid: str

    locationDescription: str

    locationType: str

    address: str

    lattitude: str

    longitude: str

    locationUID: str

    status: str

    workingDays: str

    locationCode: str

    locationLabel: str

    parentLocationId: str

    createuserid: str

    addressModelList: FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelList

class FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel(RequiredFeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel, OptionalFeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel):
    pass
