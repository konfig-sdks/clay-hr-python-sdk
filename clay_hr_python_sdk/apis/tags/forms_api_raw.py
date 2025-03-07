# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.api_my.get import GetAssignedFormsRaw
from clay_hr_python_sdk.paths.api_view.get import GetDetailsRaw
from clay_hr_python_sdk.paths.api_getdynaforms.get import GetDynaFormRaw
from clay_hr_python_sdk.paths.api_response_dynamic_form_id.get import GetFormResponseRaw
from clay_hr_python_sdk.paths.api_responselist.get import GetFormResponsesRaw
from clay_hr_python_sdk.paths.api_save_form_response.post import SaveFormResponseRaw
from clay_hr_python_sdk.paths.api_save_item_response.post import SubmitItemResponseRaw


class FormsApiRaw(
    GetAssignedFormsRaw,
    GetDetailsRaw,
    GetDynaFormRaw,
    GetFormResponseRaw,
    GetFormResponsesRaw,
    SaveFormResponseRaw,
    SubmitItemResponseRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
