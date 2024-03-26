# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.customfield.get import GetByIdRaw
from clay_hr_python_sdk.paths.customfields.get import GetCustomFieldsRaw
from clay_hr_python_sdk.paths.customlist.get import GetCustomListsRaw
from clay_hr_python_sdk.paths.customfieldvalues.get import GetValueRaw
from clay_hr_python_sdk.paths.customfieldvalues.post import UpdateValueRaw


class CustomFieldsApiRaw(
    GetByIdRaw,
    GetCustomFieldsRaw,
    GetCustomListsRaw,
    GetValueRaw,
    UpdateValueRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
