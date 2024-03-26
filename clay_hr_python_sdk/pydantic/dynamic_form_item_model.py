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

from clay_hr_python_sdk.pydantic.attachment_model import AttachmentModel
from clay_hr_python_sdk.pydantic.custom_list_model import CustomListModel
from clay_hr_python_sdk.pydantic.dyna_form_item_option_model import DynaFormItemOptionModel
from clay_hr_python_sdk.pydantic.timestamp import Timestamp

class DynamicFormItemModel(BaseModel):
    attachment_model: typing.Optional[AttachmentModel] = Field(None, alias='attachmentModel')

    cid: typing.Optional[int] = Field(None, alias='cid')

    correct_feedback: typing.Optional[str] = Field(None, alias='correctFeedback')

    create_user_id: typing.Optional[int] = Field(None, alias='createUserId')

    createts: typing.Optional[Timestamp] = Field(None, alias='createts')

    custom_list_model: typing.Optional[CustomListModel] = Field(None, alias='customListModel')

    dyna_form_item_option_model_list: typing.Optional[typing.List[DynaFormItemOptionModel]] = Field(None, alias='dynaFormItemOptionModelList')

    dynamic_form_id: typing.Optional[int] = Field(None, alias='dynamicFormId')

    dynamic_form_item_id: typing.Optional[int] = Field(None, alias='dynamicFormItemId')

    expected_value: typing.Optional[str] = Field(None, alias='expectedValue')

    field_type: typing.Optional[str] = Field(None, alias='fieldType')

    field_type_item: typing.Optional[str] = Field(None, alias='fieldTypeItem')

    help_text: typing.Optional[str] = Field(None, alias='helpText')

    incorrect_feedback: typing.Optional[str] = Field(None, alias='incorrectFeedback')

    mandatory: typing.Optional[int] = Field(None, alias='mandatory')

    mapped_entity_item: typing.Optional[str] = Field(None, alias='mappedEntityItem')

    name: typing.Optional[str] = Field(None, alias='name')

    numbering_style: typing.Optional[str] = Field(None, alias='numberingStyle')

    option_random: typing.Optional[bool] = Field(None, alias='optionRandom')

    option_values: typing.Optional[str] = Field(None, alias='optionValues')

    section_id: typing.Optional[int] = Field(None, alias='sectionId')

    sequence: typing.Optional[int] = Field(None, alias='sequence')

    weightage: typing.Optional[typing.Union[int, float]] = Field(None, alias='weightage')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
