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

from clay_hr_python_sdk.pydantic.feedback_list_feedback_response_feedback_list_item_assigned_user_model_location_model_address_model_list_item_country_model import FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelListItemCountryModel

class FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelListItem(BaseModel):
    address_id: typing.Optional[str] = Field(None, alias='addressId')

    address_line1: typing.Optional[str] = Field(None, alias='addressLine1')

    address_line2: typing.Optional[str] = Field(None, alias='addressLine2')

    city: typing.Optional[str] = Field(None, alias='city')

    current_status: typing.Optional[str] = Field(None, alias='currentStatus')

    state: typing.Optional[str] = Field(None, alias='state')

    zip_code: typing.Optional[str] = Field(None, alias='zipCode')

    createts: typing.Optional[str] = Field(None, alias='createts')

    cid: typing.Optional[str] = Field(None, alias='cid')

    user_id: typing.Optional[str] = Field(None, alias='userId')

    candidate_id: typing.Optional[str] = Field(None, alias='candidateId')

    address_type: typing.Optional[str] = Field(None, alias='addressType')

    location_id: typing.Optional[str] = Field(None, alias='locationId')

    contact_id: typing.Optional[str] = Field(None, alias='contactId')

    country_id: typing.Optional[str] = Field(None, alias='countryId')

    country_model: typing.Optional[FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelLocationModelAddressModelListItemCountryModel] = Field(None, alias='countryModel')

    status: typing.Optional[str] = Field(None, alias='status')

    verification_status: typing.Optional[str] = Field(None, alias='verificationStatus')

    cust_id: typing.Optional[str] = Field(None, alias='custId')

    map_url: typing.Optional[str] = Field(None, alias='mapUrl')

    create_user_id: typing.Optional[str] = Field(None, alias='createUserId')

    ext_app_u_i_d: typing.Optional[str] = Field(None, alias='extAppUID')

    country_code: typing.Optional[str] = Field(None, alias='countryCode')

    countryid: typing.Optional[str] = Field(None, alias='countryid')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
