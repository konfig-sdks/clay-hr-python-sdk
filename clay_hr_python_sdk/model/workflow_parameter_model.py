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


class WorkflowParameterModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cid = schemas.Int32Schema
        
            @staticmethod
            def createts() -> typing.Type['Timestamp']:
                return Timestamp
            paramName = schemas.StrSchema
            paramType = schemas.StrSchema
            workflowArgId = schemas.Int32Schema
            workflowId = schemas.Int32Schema
            __annotations__ = {
                "cid": cid,
                "createts": createts,
                "paramName": paramName,
                "paramType": paramType,
                "workflowArgId": workflowArgId,
                "workflowId": workflowId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createts"]) -> 'Timestamp': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramName"]) -> MetaOapg.properties.paramName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paramType"]) -> MetaOapg.properties.paramType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowArgId"]) -> MetaOapg.properties.workflowArgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workflowId"]) -> MetaOapg.properties.workflowId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cid", "createts", "paramName", "paramType", "workflowArgId", "workflowId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createts"]) -> typing.Union['Timestamp', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramName"]) -> typing.Union[MetaOapg.properties.paramName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paramType"]) -> typing.Union[MetaOapg.properties.paramType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowArgId"]) -> typing.Union[MetaOapg.properties.workflowArgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workflowId"]) -> typing.Union[MetaOapg.properties.workflowId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cid", "createts", "paramName", "paramType", "workflowArgId", "workflowId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createts: typing.Union['Timestamp', schemas.Unset] = schemas.unset,
        paramName: typing.Union[MetaOapg.properties.paramName, str, schemas.Unset] = schemas.unset,
        paramType: typing.Union[MetaOapg.properties.paramType, str, schemas.Unset] = schemas.unset,
        workflowArgId: typing.Union[MetaOapg.properties.workflowArgId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        workflowId: typing.Union[MetaOapg.properties.workflowId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'WorkflowParameterModel':
        return super().__new__(
            cls,
            *args,
            cid=cid,
            createts=createts,
            paramName=paramName,
            paramType=paramType,
            workflowArgId=workflowArgId,
            workflowId=workflowId,
            _configuration=_configuration,
            **kwargs,
        )

from clay_hr_python_sdk.model.timestamp import Timestamp
