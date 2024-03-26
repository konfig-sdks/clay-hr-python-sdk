# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from clay_hr_python_sdk.paths.api_my.get import GetAssignedForms
from clay_hr_python_sdk.paths.api_view.get import GetDetails
from clay_hr_python_sdk.paths.api_getdynaforms.get import GetDynaForm
from clay_hr_python_sdk.paths.api_response_dynamic_form_id.get import GetFormResponse
from clay_hr_python_sdk.paths.api_responselist.get import GetFormResponses
from clay_hr_python_sdk.paths.api_save_form_response.post import SaveFormResponse
from clay_hr_python_sdk.paths.api_save_item_response.post import SubmitItemResponse
from clay_hr_python_sdk.apis.tags.forms_api_raw import FormsApiRaw


class FormsApi(
    GetAssignedForms,
    GetDetails,
    GetDynaForm,
    GetFormResponse,
    GetFormResponses,
    SaveFormResponse,
    SubmitItemResponse,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: FormsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = FormsApiRaw(api_client)
