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


class CustomFieldValueModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cid = schemas.Int32Schema
            createUserId = schemas.Int32Schema
            customFieldId = schemas.Int32Schema
            customFieldObjectId = schemas.Int32Schema
            customFieldValue = schemas.StrSchema
            customFieldValueId = schemas.Int32Schema
            customfieldName = schemas.StrSchema
            __annotations__ = {
                "cid": cid,
                "createUserId": createUserId,
                "customFieldId": customFieldId,
                "customFieldObjectId": customFieldObjectId,
                "customFieldValue": customFieldValue,
                "customFieldValueId": customFieldValueId,
                "customfieldName": customfieldName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createUserId"]) -> MetaOapg.properties.createUserId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldId"]) -> MetaOapg.properties.customFieldId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldObjectId"]) -> MetaOapg.properties.customFieldObjectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldValue"]) -> MetaOapg.properties.customFieldValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customFieldValueId"]) -> MetaOapg.properties.customFieldValueId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["customfieldName"]) -> MetaOapg.properties.customfieldName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cid", "createUserId", "customFieldId", "customFieldObjectId", "customFieldValue", "customFieldValueId", "customfieldName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createUserId"]) -> typing.Union[MetaOapg.properties.createUserId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldId"]) -> typing.Union[MetaOapg.properties.customFieldId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldObjectId"]) -> typing.Union[MetaOapg.properties.customFieldObjectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldValue"]) -> typing.Union[MetaOapg.properties.customFieldValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customFieldValueId"]) -> typing.Union[MetaOapg.properties.customFieldValueId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["customfieldName"]) -> typing.Union[MetaOapg.properties.customfieldName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cid", "createUserId", "customFieldId", "customFieldObjectId", "customFieldValue", "customFieldValueId", "customfieldName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        createUserId: typing.Union[MetaOapg.properties.createUserId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customFieldId: typing.Union[MetaOapg.properties.customFieldId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customFieldObjectId: typing.Union[MetaOapg.properties.customFieldObjectId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customFieldValue: typing.Union[MetaOapg.properties.customFieldValue, str, schemas.Unset] = schemas.unset,
        customFieldValueId: typing.Union[MetaOapg.properties.customFieldValueId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        customfieldName: typing.Union[MetaOapg.properties.customfieldName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldValueModel':
        return super().__new__(
            cls,
            *args,
            cid=cid,
            createUserId=createUserId,
            customFieldId=customFieldId,
            customFieldObjectId=customFieldObjectId,
            customFieldValue=customFieldValue,
            customFieldValueId=customFieldValueId,
            customfieldName=customfieldName,
            _configuration=_configuration,
            **kwargs,
        )
