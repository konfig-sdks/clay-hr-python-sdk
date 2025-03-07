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


class CustomListEntryModel(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            cid = schemas.Int32Schema
            entryCode = schemas.StrSchema
            entryId = schemas.Int32Schema
            entryValue = schemas.StrSchema
            listId = schemas.Int32Schema
            __annotations__ = {
                "cid": cid,
                "entryCode": entryCode,
                "entryId": entryId,
                "entryValue": entryValue,
                "listId": listId,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cid"]) -> MetaOapg.properties.cid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entryCode"]) -> MetaOapg.properties.entryCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entryId"]) -> MetaOapg.properties.entryId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["entryValue"]) -> MetaOapg.properties.entryValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["listId"]) -> MetaOapg.properties.listId: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cid", "entryCode", "entryId", "entryValue", "listId", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cid"]) -> typing.Union[MetaOapg.properties.cid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entryCode"]) -> typing.Union[MetaOapg.properties.entryCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entryId"]) -> typing.Union[MetaOapg.properties.entryId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["entryValue"]) -> typing.Union[MetaOapg.properties.entryValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["listId"]) -> typing.Union[MetaOapg.properties.listId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cid", "entryCode", "entryId", "entryValue", "listId", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        cid: typing.Union[MetaOapg.properties.cid, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        entryCode: typing.Union[MetaOapg.properties.entryCode, str, schemas.Unset] = schemas.unset,
        entryId: typing.Union[MetaOapg.properties.entryId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        entryValue: typing.Union[MetaOapg.properties.entryValue, str, schemas.Unset] = schemas.unset,
        listId: typing.Union[MetaOapg.properties.listId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomListEntryModel':
        return super().__new__(
            cls,
            *args,
            cid=cid,
            entryCode=entryCode,
            entryId=entryId,
            entryValue=entryValue,
            listId=listId,
            _configuration=_configuration,
            **kwargs,
        )
