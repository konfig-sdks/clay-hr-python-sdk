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


class RequiredSurveyGetAllSurveyResponses403Response(TypedDict):
    pass

class OptionalSurveyGetAllSurveyResponses403Response(TypedDict, total=False):
    message: str

class SurveyGetAllSurveyResponses403Response(RequiredSurveyGetAllSurveyResponses403Response, OptionalSurveyGetAllSurveyResponses403Response):
    pass
