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

from clay_hr_python_sdk.pydantic.goals_get_goal_response_assigned_user_model_location_model_address_model_list_item import GoalsGetGoalResponseAssignedUserModelLocationModelAddressModelListItem

GoalsGetGoalResponseAssignedUserModelLocationModelAddressModelList = typing.List[GoalsGetGoalResponseAssignedUserModelLocationModelAddressModelListItem]
