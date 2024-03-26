# coding: utf-8

"""
    Expense Reports

    API Documentation

    The version of the OpenAPI document: 1.0
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from clay_hr_python_sdk import schemas  # noqa: F401


class FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            departmentId = schemas.StrSchema
            name = schemas.StrSchema
            deptHead = schemas.StrSchema
            cid = schemas.StrSchema
            departmentCode = schemas.StrSchema
            departmentLabel = schemas.StrSchema
            parentDepartmentId = schemas.StrSchema
            parentDepartmentName = schemas.StrSchema
            deptHeadName = schemas.StrSchema
            noOfEmployees = schemas.StrSchema
        
            @staticmethod
            def userModel() -> typing.Type['FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel']:
                return FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel
            __annotations__ = {
                "description": description,
                "departmentId": departmentId,
                "name": name,
                "deptHead": deptHead,
                "cid": cid,
                "departmentCode": departmentCode,
                "departmentLabel": departmentLabel,
                "parentDepartmentId": parentDepartmentId,
                "parentDepartmentName": parentDepartmentName,
                "deptHeadName": deptHeadName,
                "noOfEmployees": noOfEmployees,
                "userModel": userModel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentId"]) -> MetaOapg.properties.departmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deptHead"]) -> MetaOapg.properties.deptHead: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentCode"]) -> MetaOapg.properties.departmentCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departmentLabel"]) -> MetaOapg.properties.departmentLabel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentDepartmentId"]) -> MetaOapg.properties.parentDepartmentId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["parentDepartmentName"]) -> MetaOapg.properties.parentDepartmentName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deptHeadName"]) -> MetaOapg.properties.deptHeadName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["noOfEmployees"]) -> MetaOapg.properties.noOfEmployees: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userModel"]) -> 'FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "departmentId", "name", "deptHead", "cid", "departmentCode", "departmentLabel", "parentDepartmentId", "parentDepartmentName", "deptHeadName", "noOfEmployees", "userModel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentId"]) -> typing.Union[MetaOapg.properties.departmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deptHead"]) -> typing.Union[MetaOapg.properties.deptHead, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentCode"]) -> typing.Union[MetaOapg.properties.departmentCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departmentLabel"]) -> typing.Union[MetaOapg.properties.departmentLabel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentDepartmentId"]) -> typing.Union[MetaOapg.properties.parentDepartmentId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["parentDepartmentName"]) -> typing.Union[MetaOapg.properties.parentDepartmentName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deptHeadName"]) -> typing.Union[MetaOapg.properties.deptHeadName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["noOfEmployees"]) -> typing.Union[MetaOapg.properties.noOfEmployees, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userModel"]) -> typing.Union['FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "departmentId", "name", "deptHead", "cid", "departmentCode", "departmentLabel", "parentDepartmentId", "parentDepartmentName", "deptHeadName", "noOfEmployees", "userModel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        departmentId: typing.Union[MetaOapg.properties.departmentId, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        deptHead: typing.Union[MetaOapg.properties.deptHead, str, schemas.Unset] = schemas.unset,
        cid: typing.Union[MetaOapg.properties.cid, str, schemas.Unset] = schemas.unset,
        departmentCode: typing.Union[MetaOapg.properties.departmentCode, str, schemas.Unset] = schemas.unset,
        departmentLabel: typing.Union[MetaOapg.properties.departmentLabel, str, schemas.Unset] = schemas.unset,
        parentDepartmentId: typing.Union[MetaOapg.properties.parentDepartmentId, str, schemas.Unset] = schemas.unset,
        parentDepartmentName: typing.Union[MetaOapg.properties.parentDepartmentName, str, schemas.Unset] = schemas.unset,
        deptHeadName: typing.Union[MetaOapg.properties.deptHeadName, str, schemas.Unset] = schemas.unset,
        noOfEmployees: typing.Union[MetaOapg.properties.noOfEmployees, str, schemas.Unset] = schemas.unset,
        userModel: typing.Union['FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModel':
        return super().__new__(
            cls,
            *args,
            description=description,
            departmentId=departmentId,
            name=name,
            deptHead=deptHead,
            cid=cid,
            departmentCode=departmentCode,
            departmentLabel=departmentLabel,
            parentDepartmentId=parentDepartmentId,
            parentDepartmentName=parentDepartmentName,
            deptHeadName=deptHeadName,
            noOfEmployees=noOfEmployees,
            userModel=userModel,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.feedback_list_feedback_response_feedback_list_item_assigned_user_model_department_model_user_model import FeedbackListFeedbackResponseFeedbackListItemAssignedUserModelDepartmentModelUserModel
