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

from clay_hr_python_sdk.pydantic.feedback_list_feedback_response_feedback_list_item_assigned_user_model_location_model_address_model_list import FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelList

class FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModel(BaseModel):
    location_id: typing.Optional[str] = Field(None, alias='locationId')

    location_name: typing.Optional[str] = Field(None, alias='locationName')

    cid: typing.Optional[str] = Field(None, alias='cid')

    location_description: typing.Optional[str] = Field(None, alias='locationDescription')

    location_type: typing.Optional[str] = Field(None, alias='locationType')

    address: typing.Optional[str] = Field(None, alias='address')

    lattitude: typing.Optional[str] = Field(None, alias='lattitude')

    longitude: typing.Optional[str] = Field(None, alias='longitude')

    location_u_i_d: typing.Optional[str] = Field(None, alias='locationUID')

    status: typing.Optional[str] = Field(None, alias='status')

    working_days: typing.Optional[str] = Field(None, alias='workingDays')

    location_code: typing.Optional[str] = Field(None, alias='locationCode')

    location_label: typing.Optional[str] = Field(None, alias='locationLabel')

    parent_location_id: typing.Optional[str] = Field(None, alias='parentLocationId')

    createuserid: typing.Optional[str] = Field(None, alias='createuserid')

    address_model_list: typing.Optional[FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelList] = Field(None, alias='addressModelList')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
