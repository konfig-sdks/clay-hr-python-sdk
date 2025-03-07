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


class ProjectCreateNewRequest(BaseModel):
    # Name of the project.
    project_name: str = Field(alias='projectName')

    # Description of the project.
    project_desc: str = Field(alias='projectDesc')

    # A unique short code to identify the project.
    short_code: str = Field(alias='shortCode')

    # Start date of the project.
    start_date: date = Field(alias='startDate')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
