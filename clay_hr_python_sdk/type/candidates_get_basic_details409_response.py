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


class RequiredCandidatesGetBasicDetails409Response(TypedDict):
    pass

class OptionalCandidatesGetBasicDetails409Response(TypedDict, total=False):
    message: str

class CandidatesGetBasicDetails409Response(RequiredCandidatesGetBasicDetails409Response, OptionalCandidatesGetBasicDetails409Response):
    pass
