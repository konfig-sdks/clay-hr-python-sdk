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

from clay_hr_python_sdk.type.custom_fields_get_by_id_response_data_custom_field_group_model import CustomFieldsGetByIdResponseDataCustomFieldGroupModel
from clay_hr_python_sdk.type.custom_fields_get_by_id_response_data_custom_field_value_model_list import CustomFieldsGetByIdResponseDataCustomFieldValueModelList

class RequiredCustomFieldsGetByIdResponseData(TypedDict):
    pass

class OptionalCustomFieldsGetByIdResponseData(TypedDict, total=False):
    customFieldId: str

    customFieldName: str

    customFieldType: str

    objectType: str

    sequence: str

    cid: str

    fieldType: str

    defaultValue: str

    cfcode: str

    cfgroupid: str

    style: str

    opValues: str

    fieldFormula: str

    customFieldValueModel: str

    customFieldValueModelList: CustomFieldsGetByIdResponseDataCustomFieldValueModelList

    customFieldGroupModel: CustomFieldsGetByIdResponseDataCustomFieldGroupModel

    objectAccessModel: str

    access: str

    userGroupId: str

    candidateAccess: str

    userAccess: str

    managerAccess: str

    integrationTypeId: str

    helpText: str

    createUserId: str

    createts: int

    customFieldStyleModel: str

    readAccessTypeCode: str

    readUserGroupId: str

    mandatory: str

    masked: str

class CustomFieldsGetByIdResponseData(RequiredCustomFieldsGetByIdResponseData, OptionalCustomFieldsGetByIdResponseData):
    pass
