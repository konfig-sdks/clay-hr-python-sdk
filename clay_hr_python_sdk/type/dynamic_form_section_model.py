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

from clay_hr_python_sdk.type.attachment_model import AttachmentModel
from clay_hr_python_sdk.type.dynamic_form_item_model import DynamicFormItemModel
from clay_hr_python_sdk.type.user_group_model import UserGroupModel
from clay_hr_python_sdk.type.user_model import UserModel

class RequiredDynamicFormSectionModel(TypedDict):
    pass

class OptionalDynamicFormSectionModel(TypedDict, total=False):
    description: str

    assignee: str

    assigneeModel: UserModel

    attachmentModel: AttachmentModel

    cid: int

    createUserId: int

    dynamicFormId: int

    dynamicFormItemModelList: typing.List[DynamicFormItemModel]

    hidden: bool

    name: str

    sectionId: int

    sequence: int

    totalweightage: typing.Union[int, float]

    userGroupModel: UserGroupModel

class DynamicFormSectionModel(RequiredDynamicFormSectionModel, OptionalDynamicFormSectionModel):
    pass
