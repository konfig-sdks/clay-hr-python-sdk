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

from clay_hr_python_sdk.pydantic.people_and_permissions_create_or_update_user_details_request_education_list_item import PeopleAndPermissionsCreateOrUpdateUserDetailsRequestEducationListItem

PeopleAndPermissionsCreateOrUpdateUserDetailsRequestEducationList = typing.List[PeopleAndPermissionsCreateOrUpdateUserDetailsRequestEducationListItem]
