# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.resume.post import ExtractPdfResumeRaw
from clay_hr_python_sdk.paths.root.get import GetRaw
from clay_hr_python_sdk.paths._list.get import GetBasicDetailsRaw
from clay_hr_python_sdk.paths.detail_recruitid.get import GetCandidateDetailByRecruitidRaw
from clay_hr_python_sdk.paths.root.post import SubmitNewCandidateRaw


class CandidatesApiRaw(
    ExtractPdfResumeRaw,
    GetRaw,
    GetBasicDetailsRaw,
    GetCandidateDetailByRecruitidRaw,
    SubmitNewCandidateRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
